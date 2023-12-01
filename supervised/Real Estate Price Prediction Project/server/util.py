import json
import pickle
import sklearn
import numpy as np
import warnings
warnings.filterwarnings('ignore')

__data_columns = None
__loacations = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
        print('**********100**********',loc_index)
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    print('**********100**********',x)
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loding saved artifacts...start")
    global __data_columns
    global __loacations
    
    
    with open("C:\\Users\\ARJUN\\Downloads\\Home Price Predction ML\\server\\artifacts\\columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __loacations = __data_columns[3:]

    global __model
    if __model is None:
        with open("C:\\Users\\ARJUN\\Downloads\\Home Price Predction ML\\server\\artifacts\\house_rent_prediction.pickle", 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts....done")

def get_location_names():
    return __loacations

def get_location_names():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st block jayanagar',1000, 3, 3))
    print(get_estimated_price('1st block jayanagar', 1000, 2, 2))
