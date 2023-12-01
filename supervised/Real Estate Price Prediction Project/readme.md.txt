This data science project series walks through step by step process of how to build a real estate price prediction website. We will first build a model using sklearn and linear regression using banglore home prices dataset from kaggle.com. Second step would be to write a python flask server that uses the saved model to serve http requests. Third component is the website built in html, css and javascript that allows user to enter home square ft area, bedrooms etc and it will call python flask server to retrieve the predicted price. During model building we will cover almost all data science concepts such as data load and cleaning, outlier detection and removal, feature engineering, dimensionality reduction, gridsearchcv for hyperparameter tunning, k fold cross validation etc. Technology and tools wise this project covers,

Python
Numpy and Pandas for data cleaning
Matplotlib for data visualization
Sklearn for model building
Jupyter notebook, visual studio code and pycharm as IDE
Python flask for http server
HTML/CSS/Javascript for UI
AWS (EC2) Deploy

Import nessasry packages

load the data

read the data using pandas dataframe

clean the data 
 drop unwanted columns
 check blank cells 
 drop nan values
 
room size have messy value so split the value into the new column as ['BHK']

home area square feet convert in to float value
some value are in range so apply function take average value of square feet and convert into float

applying feature engineering heare inthis stage
creating new feature for outlayer detection and removel

creating new column as [prize per square feet] = price x 100000 / total square feet

location have 1304 unique values so that an issue called
diamantionality curse
so geting diamantionality problem in ml model (we need to reduce the value here)

apply groupby agg function in the location column

manage and clean unuseal data
ex. 600sqft 6 bedroom its not posible
so this kind of outliers need to remove


heare im remove properties where for same location, the price of (for excample) 3 bedroom apartment is less then 2 bedroom appartment (with same square ft area). what we will do is for a given location, we will build a dictionary of stats per bhk, i.e.

{
    '1': {
        'mean': 4000,
        'std': 2000,
        'count': 34
    },
    {
        '2': {
            'mean': 4300,
            'std': 2300,
            'count': 22
        },
}

Now im remove those 2BHK apartments whose price_per_sqft is less then mean price_per_sqft of 1BHK apartment


Deployment machine learning model to AWS (EC2 instance)

Architecture of application in EC2 instance


AAAAAAAAAAAAAAAAAAAAArchecture image paste here


Deploy this app to cloud (AWS EC2)
Create EC2 instance using amazon console, also in security group add a rule to allow HTTP incoming traffic
Now connect to your instance using a command like this,
    ssh -i "C:\Users\Arjun\.ssh\bhk.pem" ubuntu@ec2-13-53-40-185.eu-north-1.compute.amazonaws.com
    nginx setup
    Install nginx on EC2 instance using these commands,
    sudo apt-get update
    sudo apt-get install nginx
Above will install nginx as well as run it. Check status of nginx using
    sudo service nginx status
Here are the commands to start/stop/restart nginx
    sudo service nginx start
    sudo service nginx stop
    sudo service nginx restart
Now when you load cloud url in browser you will see a message saying "welcome to nginx" This means your nginx is setup and running.
Now you need to copy all your code to EC2 instance. You can do this either using git or copy files using winscp. We will use winscp. You can download winscp from here: https://winscp.net/eng/download.php
Once you connect to EC2 instance from winscp (instruction in a youtube video), you can now copy all code files into /home/ubuntu/ folder. The full path of your root folder is now: /home/ubuntu/Home Price Predction ML
After copying code on EC2 server now we can point nginx to load our property website by default. For below steps,
Create this file /etc/nginx/sites-available/bhp.conf. The file content looks like this,
server {
    listen 80;
        server_name bhp;
        root /home/ubuntu/Home Price Predction ML/client;
        index app.html;
        location /api/ {
             rewrite ^/api(.*) $1 break;
             proxy_pass http://127.0.0.1:5000;
        }
}
Create symlink for this file in /etc/nginx/sites-enabled by running this command,
    sudo ln -v -s /etc/nginx/sites-available/bhp.conf
Remove symlink for default file in /etc/nginx/sites-enabled directory,
    sudo unlink default
Restart nginx,
    sudo service nginx restart
Now install python packages and start flask server
    sudo apt-get install python3-pip
    sudo pip3 install -r /home/ubuntu/Home Price Predction ML/server/requirements.txt
python3 /home/ubuntu/Home Price Predction ML/client/server.py
Running last command above will prompt that server is running on port 5000.
Now just load your cloud url in browser (for me it was http://ec2-13-53-40-185.eu-north-1.compute.amazonaws.com/) 
and this will be fully functional website running in production cloud environment.