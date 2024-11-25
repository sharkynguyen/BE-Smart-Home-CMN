from models.energy_in import EnergyInModel
from models.engergy_out import EnergyOutModel


def toJsonLed(led) -> dict:
    return {
        'id': str(led['_id']),
        'name': str(led['name']),
        'description': str(led['description']),
        'status': int(led['status']),
        'updated_time': str(led['updated_time']),
    }

def toJsonMotor(motor) -> dict:
    return {
        'id': str(motor['_id']),
        'name': str(motor['name']),
        'description': str(motor['description']),
        'status': int(motor['status']),
        'updated_time': str(motor['updated_time']),
    }

def toJsonSensor(sensor) -> dict:
    return {
        'id': str(sensor['_id']),
        'name': str(sensor['name']),
        'description': str(sensor['description']),
        'temp': int(sensor['temp']),
        'humidity': int(sensor['humidity']),
        'updated_time': str(sensor['updated_time']),
    }

def toJsonHeartOxygen(sensor) -> dict:
    return {
        'id': str(sensor['_id']),
        'name': str(sensor['name']),
        'description': str(sensor['description']),
        'heart': float(sensor['heart']),
        'oxygen': float(sensor['oxygen']),
        'updated_time': str(sensor['updated_time']),
    }


def toJsonAdvice(sensor) -> dict:
    return {
        'msg': str(sensor['msg']),
        'heart': float(sensor['heart']),
        'oxygen': float(sensor['oxygen']),
        'updated_time': str(sensor['updated_time']),
    }

def toJsonPersonalInfo(sensor) -> dict:
    return {
        'id': str(sensor['_id']),
        'age': str(sensor['age']),
        'gender': str(sensor['gender']),
        'heartDesease': str(sensor['heartDesease']),
        'otherDease': str(sensor['otherDease']),
        'heart': float(sensor['heart']),
        'oxygen': float(sensor['oxygen']),
        'weight': float(sensor['weight']),
        'height': float(sensor['height']),
        'isPlayingSports': bool(sensor['isPlayingSports']),
        'sport': str(sensor['sport']),
    }


def toJsonEnergyInModel(energy_model: EnergyInModel) -> dict:
    return {
        'id': str(energy_model['_id']),
        'vMin': float(energy_model['vMin']),
        'vMax': float(energy_model['vMax']),
        'l': float(energy_model['l']),
        'temperatureFan': float(energy_model['temperatureFan']),
        'temperatureMax': float(energy_model['temperatureMax']),
        'updated_time': str(energy_model['updated_time']),
    }

def toJsonEnergyOutModel(energy_out_model: EnergyOutModel) -> dict:
    return {
        'vIn': float(energy_out_model['vIn']),
        'vOut': float(energy_out_model['vOut']),
        'iIn': float(energy_out_model['iIn']),
        'iOut': float(energy_out_model['iOut']),
        'pOut': float(energy_out_model['pOut']),
        'pIn': float(energy_out_model['pIn']),
        'temperature': float(energy_out_model['temperature']),
        'updated_time': str(energy_out_model['updated_time']),
    }

def get_led_collection(leds) -> list:
    return [toJsonLed(led) for led in leds]

def get_motor_collection(motors) -> list:
    return [toJsonMotor(motor) for motor in motors]

def get_sensor_collection(sensorData) -> list:
    return [toJsonSensor(data) for data in sensorData]

def get_heart_oxygen_collection(sensorData) -> list:
    return [toJsonHeartOxygen(data) for data in sensorData]

def get_advice_collection(sensorData) -> list:
    return [toJsonAdvice(data) for data in sensorData]

def get_lastest_advice_collection(sensorData) -> list:
    return [toJsonAdvice(data) for data in sensorData]

def get_personal_info_collection(sensorData) -> list:
    return [toJsonPersonalInfo(data) for data in sensorData]

def get_personal_collection(sensorData) -> list:
    return [toJsonPersonalInfo(data) for data in sensorData]

def get_energy_in_collection(sensorData) -> list:
    return [toJsonEnergyInModel(data) for data in sensorData]

def get_energy_out_collection(sensorData) -> list:
    return [toJsonEnergyOutModel(data) for data in sensorData]
