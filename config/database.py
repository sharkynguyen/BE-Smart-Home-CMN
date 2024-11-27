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

def device_collection():
    device_collection = mongo_db['device_collection']

    return device_collection

def sensor_collection():
    sensor_collection = mongo_db['sensor_collection']

    return sensor_collection

def energy_in_collection():
    energy = mongo_db['energy_in']

    return energy

def energy_out_collection():
    energy = mongo_db['energy_out']

    return energy
