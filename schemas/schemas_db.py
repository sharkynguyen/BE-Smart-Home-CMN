from models.energy_in import EnergyInModel
from models.engergy_out import EnergyOutModel
from models.message import MessageModel

def toJsonDevice(device) -> dict:
    return {
        'id': str(device['_id']),
        'name': str(device['name']),
        'description': str(device['description']),
        'status': int(device['status']),
        'updated_time': str(device['updated_time']),
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
        'batPercent': float(energy_out_model['batPercent']),
        'whP': float(energy_out_model['whP']),
        'updated_time': str(energy_out_model['updated_time']),
    }

def toJsonMessageModel(message: MessageModel) -> dict:
    return {
        'role': int(message['role']),
        'message': str(message['message']),
        'updated_time': str(message['updated_time']),
    }

def get_device_collection(devices) -> list:
    return [toJsonDevice(device) for device in devices]

def get_sensor_collection(sensorData) -> list:
    return [toJsonSensor(data) for data in sensorData]

def get_energy_in_collection(sensorData) -> list:
    return [toJsonEnergyInModel(data) for data in sensorData]

def get_energy_out_collection(sensorData) -> list:
    return [toJsonEnergyOutModel(data) for data in sensorData]

def get_message_collection(messages) -> list:
    return [toJsonMessageModel(data) for data in messages]
