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


def get_led_collection(leds) -> list:
    return [toJsonLed(led) for led in leds]

def get_motor_collection(motors) -> list:
    return [toJsonMotor(motor) for motor in motors]

def get_sensor_collection(sensorData) -> list:
    return [toJsonSensor(data) for data in sensorData]


