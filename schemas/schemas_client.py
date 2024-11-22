from Adafruit_IO import Client, Feed
import os
from Adafruit_IO import MQTTClient
import sys
from models.personal_info import PersonalInfo
from models.senor import SensorModel
from datetime import datetime
from dotenv import load_dotenv
# import google.generativeai as genai
import os

load_dotenv()

ADAFRUIT_AIO_USERNAME = os.getenv("ADAFRUIT_AIO_USERNAME")
ADAFRUIT_AIO_KEY = os.getenv("ADAFRUIT_AIO_KEY")
ID_Temperature_FEED = os.getenv('ID_Temperature_FEED')
ID_Humidity_FEED = os.getenv('ID_Humidity_FEED')
IO_FEED_USERNAME = os.getenv('IO_FEED_USERNAME')
IO_Led1_FEED_USERNAME = os.getenv('IO_Led1_FEED_USERNAME')
IO_Led2_FEED_USERNAME = os.getenv('IO_Led2_FEED_USERNAME')
IO_Motor_FEED_USERNAME = os.getenv('IO_Motor_FEED_USERNAME')
IO_Light_FEED_USERNAME = os.getenv('IO_Light_FEED_USERNAME')
IO_Mask_Detection_FEED_USERNAME = os.getenv('IO_Mask_Detection_FEED_USERNAME')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

def mqqt_client():
    genai.configure(api_key=GEMINI_API_KEY)

    mqttClient = MQTTClient(ADAFRUIT_AIO_USERNAME, ADAFRUIT_AIO_KEY)

    mqttClient.on_connect       =   connected
    mqttClient.on_disconnect    =   disconnected
    mqttClient.on_message       =   message

    mqttClient.connect()
    mqttClient.loop_background()

    return mqttClient

def adfruit_client():
    client = Client(ADAFRUIT_AIO_USERNAME, ADAFRUIT_AIO_KEY)
    return client

def update_led(client, id: str, data: int):
    mqqt_client().publish(id, data, IO_FEED_USERNAME)

def update_light(client, id: str, data: int):
    mqqt_client().publish(id, data, IO_FEED_USERNAME)

def update_mask_detection(client, id: str, data: int):
    mqqt_client().publish(IO_Mask_Detection_FEED_USERNAME, data, IO_FEED_USERNAME)

def update_motor(client, id: str, data: int):
    mqqt_client().publish(id, data, IO_FEED_USERNAME)

def connected(client):
    print('CONNECTED TO ADFRUIT!!!!!!!\n')
    client.subscribe(IO_Led1_FEED_USERNAME)
    client.subscribe(IO_Led2_FEED_USERNAME)
    client.subscribe(IO_Motor_FEED_USERNAME)
    client.subscribe(ID_Humidity_FEED)
    client.subscribe(ID_Temperature_FEED)

def disconnected(client):
    print('DISCONNECTED TO ADFRUIT!!!!!!!\n')
    sys.exit(1)

def unsubscribe(client):
    print('DISCONNECTED TO ADFRUIT!!!!!!!\n')

    client.unsubscribe(IO_Led1_FEED_USERNAME)
    client.unsubscribe(IO_Led2_FEED_USERNAME)
    client.unsubscribe(IO_Motor_FEED_USERNAME)
    client.unsubscribe(ID_Humidity_FEED)
    client.unsubscribe(ID_Temperature_FEED)

    sys.exit(1)

def message(client, feed_id, payload):

    if feed_id == IO_Led1_FEED_USERNAME:
        print(f"LED1 Feed has new value: {payload}")
    elif feed_id == IO_Led2_FEED_USERNAME:
        print(f"LED2 Feed has new value: {payload}")
    elif feed_id == IO_Motor_FEED_USERNAME:
        print(f"Motor has new value: {payload}")
    elif feed_id == ID_Temperature_FEED:
        print(f"Temperature has new value: {payload}")
    elif feed_id == ID_Humidity_FEED:
        print(f"Humidity has new value: {payload}")
    elif feed_id == IO_Light_FEED_USERNAME:
        print(f"Light has new value: {payload}")
    elif feed_id == IO_Mask_Detection_FEED_USERNAME:
        print(f"Mask Detection has new value: {payload}")

    else:
        print(f"Feed {feed_id} received new value: {payload}")

def get_name_of_all_feeds():
    names = []
    feeds = adfruit_client().feeds()

    for f in feeds:
        names.append(f)

    return names

def get_led(id: str):
    led = adfruit_client().receive(id)
    return led.value

def get_motor(id: str):
    motor = adfruit_client().receive(id)
    return motor.value

def get_sensor():
    temp = adfruit_client().receive(ID_Temperature_FEED)
    humidity = adfruit_client().receive(ID_Humidity_FEED)

    sensor = SensorModel (
        name =  'sensor',
        description =  'sensor',
        temp = temp.value,
        humidity = humidity.value,
        updated_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        )

    return sensor

# def generateAdvice(info: str, hr: float, oxygen: float) -> str:
#     model = genai.GenerativeModel("gemini-1.5-flash")

#     # Format the prompt
#     prompt = (
#         f"I need advice about my health in about 10 words. "
#         f"Personal Information: {info}. "
#         f"Heart rate: {hr}. Oxygen level: {oxygen}."
#         f"I am doing exercise"
#     )

#     # Generate response
#     try:
#         response = model.generate_content(prompt)
#         print(response.text)
#         return response.text
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return "Unable to generate advice at this time."

