from pymongo import MongoClient
from pymongo.server_api import ServerApi

import certifi

def mongo_client():
    uri =  "mongodb+srv://admin:Sharky_01675@cluster0.ze83k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    client = MongoClient(uri, tlsCAFile=certifi.where(), serverSelectionTimeoutMS=5000)

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    return client

mg_client = mongo_client()

def my_db():
    return mg_client.smart_home_db

mongo_db = my_db()

def led_collection():
    led_collection = mongo_db['led_collection']

    return led_collection

def motor_collection():
    motor_collection = mongo_db['motor_collection']

    return motor_collection

def sensor_collection():
    sensor_collection = mongo_db['sensor_collection']

    return sensor_collection

def heartOxygen_collection():
    heart_Oxygen_collection = mongo_db['heart_oxygen']

    return heart_Oxygen_collection


def advice_collection():
    advice = mongo_db['advices']

    return advice

def lastest_advice_collection():
    lastest_advice = mongo_db['lastest_advices']

    return lastest_advice

def personal_information_collection():
    advice = mongo_db['personal_information']

    return advice

def energy_collection():
    energy = mongo_db['energy']

    return energy
