from fastapi import APIRouter, status, WebSocket
from models.energy_in import EnergyInModel
from models.engergy_out import EnergyOutModel
from schemas.schemas_db import  get_device_collection, get_energy_in_collection, get_energy_out_collection, get_sensor_collection, toJsonEnergyInModel, toJsonEnergyOutModel
from models.senor import SensorModel
from config.database import device_collection, energy_in_collection, energy_out_collection, sensor_collection
from schemas.schemas_client import get_name_of_all_feeds, get_sensor, mqqt_client, get_led, get_motor,  update_device, update_light, update_motor
from models.device import DeviceModel
from datetime import datetime

router = APIRouter()
mqttClient = mqqt_client()

@router.get('/', status_code=status.HTTP_202_ACCEPTED)
async def connect():
    mqqt_client()


    return {
        'status_code': status.HTTP_202_ACCEPTED,
        'msg': 'connected to Adfruit and MongoDB',
    }

@router.get('/feeds', status_code=status.HTTP_200_OK)
async def get_all_feeds():
    feeds = get_name_of_all_feeds()

    return {
        'status_code': status.HTTP_200_OK,
        'msg': 'success',
        'data': feeds
    }

#############################################################################

@router.get('/feed/lastest_led/{id}', status_code=status.HTTP_200_OK)
async def get_led_data(id: str):
    ledData = get_led(id)

    return {
        'status_code': status.HTTP_200_OK,
        'msg': 'success',
        'data': ledData,
    }

@router.get('/feed/lastest_motor/{id}', status_code=status.HTTP_200_OK)
async def get_motor_data(id: str):
    motor = get_motor(id)

    return {
        'status_code': status.HTTP_200_OK,
        'msg': 'success',
        'data': motor,
    }

@router.get('/feed/lastest_sensor', status_code=status.HTTP_200_OK)
async def get_lastest_sensor():
    data = get_sensor()

    return {
        'status_code': status.HTTP_200_OK,
        'msg': 'success',
        'data': data,
    }

@router.get('/energy_in', status_code=status.HTTP_200_OK)
async def get_energ_in():
    data = get_energy_in_collection(energy_in_collection().find())

    return {
        'status_code': status.HTTP_200_OK,
        'msg': 'success',
        'data': data,
    }

@router.get('/energy_in_lastest', status_code=status.HTTP_200_OK)
async def get_energ_in():

    last_document = energy_in_collection().find_one(sort=[('_id', -1)])

    data = toJsonEnergyInModel(last_document) if last_document else None

    return {
        'status_code': status.HTTP_200_OK,
        'msg': 'success',
        'data': data,
    }

@router.get('/energy_out', status_code=status.HTTP_200_OK)
async def get_energ_out():
    data = get_energy_out_collection(energy_out_collection().find())

    return {
        'status_code': status.HTTP_200_OK,
        'msg': 'success',
        'data': data,
    }

@router.get('/energy_out_lastest', status_code=status.HTTP_200_OK)
async def get_energ_out():

    last_document = energy_out_collection().find_one(sort=[('_id', -1)])

    data = toJsonEnergyOutModel(last_document) if last_document else None

    return {
        'status_code': status.HTTP_200_OK,
        'msg': 'success',
        'data': data,
    }
#############################################################################

@router.put('/feed/devices/{id}',status_code=status.HTTP_200_OK)
async def update_device_data(id: str, data: int):
    update_device(mqttClient, id, data)

    device = DeviceModel(
        name=id,
        description=id,
        status=data,
        updated_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

    device_collection().insert_one(dict(device))

    return {
        'status_code': status.HTTP_200_OK,
        'msg': 'updated data',
        'data': data
    }

#############################################################################

@router.post('/feed/devices', status_code=status.HTTP_200_OK)
async def insert_device_document(device: DeviceModel):

    device_collection().insert_one(dict(device))

    return {
        'status_code': 200,
        'msg': 'success',
    }

@router.post('/feed/sensor', status_code=status.HTTP_200_OK)
async def insert_sensor_document(sensor: SensorModel):

    sensor_collection().insert_one(dict(sensor))

    return {
        'status_code': 200,
        'msg': 'success',
    }

@router.post('/energy_in', status_code=status.HTTP_200_OK)
async def insertEnergyInPoint(energy: EnergyInModel):
    energy_in_collection().insert_one(dict(energy))

    return {
        'status_code': 200,
        'msg': 'success',
        'data': energy
    }

@router.post('/energy_out', status_code=status.HTTP_200_OK)
async def insertEnergyOutPoint(energy: EnergyOutModel):
    energy_out_collection().insert_one(dict(energy))

    return {
        'status_code': 200,
        'msg': 'success',
        'data': energy
    }

#############################################################################

@router.get('/feed/devices', status_code=status.HTTP_200_OK)
async def get_leds():
    devices = get_device_collection(device_collection().find())

    return {
        'status_code': 200,
        'msg': 'success',
        'data': devices
    }

@router.get('/feed/sensors', status_code=status.HTTP_200_OK)
async def get_motors():
    sensorData = get_sensor_collection(sensor_collection().find())

    return {
        'status_code': 200,
        'msg': 'success',
        'data': sensorData
    }

#############################################################################
