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
    motor_collection = mongo_db['sensor_collection']

    return motor_collection
