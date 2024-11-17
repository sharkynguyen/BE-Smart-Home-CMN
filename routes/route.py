from fastapi import APIRouter, status, WebSocket
from models.advice import AdviceModel
from models.heart_oxygen import HeartOxyGen
from models.personal_info import PersonalInfo
from schemas.schemas_db import get_advice_collection, get_heart_oxygen_collection, get_led_collection, get_motor_collection, get_personal_collection, get_sensor_collection
from models.senor import SensorModel
from models.motor import MotorModel
from config.database import advice_collection, heartOxygen_collection, led_collection, motor_collection, personal_information_collection, sensor_collection
from schemas.schemas_client import generateAdvice, get_name_of_all_feeds, get_sensor, mqqt_client, get_led, get_motor,  update_led, update_light, update_motor
from models.led import LedModel
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


#############################################################################

@router.put('/feed/led/{id}',status_code=status.HTTP_200_OK)
async def update_led_data(id: str, data: int):
    update_led(mqttClient, id, data)

    led = LedModel(
        name=id,
        description=id,
        status=data,
        updated_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

    led_collection().insert_one(dict(led))

    return {
        'status_code': status.HTTP_200_OK,
        'msg': 'updated data',
        '_id': id,
        'data': data
    }

@router.put('/feed/motor/{id}', status_code=status.HTTP_200_OK)
async def update_motor_data(id: str, data: int):
    update_motor(mqttClient, id, data)

    motor = MotorModel(
        name=id,
        description=id,
        status=data,
        updated_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

    motor_collection().insert_one(dict(motor))

    return {
        'status_code': status.HTTP_200_OK,
        'msg': 'updated data',
        '_id': id,
        'data': data
    }

@router.put('/feed/light',status_code=status.HTTP_200_OK)
async def update_light_data(id: str, data: int):
    update_light(mqttClient, id, data)

    return {
        'status_code': status.HTTP_200_OK,
        'msg': 'updated data',
        '_id': id,
        'data': data
    }


#############################################################################

@router.post('/feed/led', status_code=status.HTTP_200_OK)
async def insert_led_document(led: LedModel):

    led_collection().insert_one(dict(led))

    return {
        'status_code': 200,
        'msg': 'success',
    }

@router.post('/feed/motor', status_code=status.HTTP_200_OK)
async def insert_motor_document(motor: MotorModel):

    motor_collection().insert_one(dict(motor))

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

@router.post('/feed/heart_beat_oxygen', status_code=status.HTTP_200_OK)
async def insert_heart_oxygen_document(heartOxygen: HeartOxyGen):

    heartOxygen_collection().insert_one(dict(heartOxygen))

    return {
        'status_code': 200,
        'msg': 'success',
    }

@router.post('/feed/personal_info', status_code=status.HTTP_200_OK)
async def updatePersonalInfo(info: PersonalInfo):
    personal_information_collection().delete_many({})

    personal_information_collection().insert_one(dict(info))

    return {
        'status_code': 200,
        'msg': 'success',
    }


#############################################################################
@router.get('/feed/leds', status_code=status.HTTP_200_OK)
async def get_leds():
    leds = get_led_collection(led_collection().find())

    return {
        'status_code': 200,
        'msg': 'success',
        'data': leds
    }

@router.get('/feed/motors', status_code=status.HTTP_200_OK)
async def get_motors():
    motors = get_motor_collection(motor_collection().find())

    return {
        'status_code': 200,
        'msg': 'success',
        'data': motors
    }

@router.get('/feed/heart_oxygen', status_code=status.HTTP_200_OK)
async def get_heart_oxygen():
    heartOxygenData = get_heart_oxygen_collection(heartOxygen_collection().find())

    return {
        'status_code': 200,
        'msg': 'success',
        'data': heartOxygenData
    }

@router.get('/feed/advice', status_code=status.HTTP_200_OK)
async def get_advice(hr: float, oxygen: float):
    if hr == 0 or oxygen == 0:
        return {
            'status_code': 200,
            'msg': 'success',
            'data': 'thinking...',
        }
    else:
        personal_info =  get_personal_collection(personal_information_collection().find())

        msg =  generateAdvice(personal_info, hr, oxygen)

        advice = AdviceModel(
            msg=msg,
            heart=hr,
            oxygen=oxygen,
            updated_time=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
        )

        advice_collection().insert_one(dict(advice))

        return {
            'status_code': 200,
            'msg': 'success',
            'data': msg,
        }

@router.get('/feed/advices', status_code=status.HTTP_200_OK)
async def get_advices():
    advices =  get_advice_collection(advice_collection().find())

    return {
        'status_code': 200,
        'msg': 'success',
        'data': advices
    }

@router.get('/feed/personal', status_code=status.HTTP_200_OK)
async def getPersonalInfo():
    personal_info =  get_personal_collection(personal_information_collection().find())

    return {
        'status_code': 200,
        'msg': 'success',
        'data': personal_info
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
