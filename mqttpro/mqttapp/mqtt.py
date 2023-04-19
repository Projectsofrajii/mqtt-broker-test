import paho.mqtt.client as mqtt
from django.conf import settings


def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
        mqtt_client.subscribe('MQTT-broker-assignment')
    else:
        print('Bad connection. Code:', rc)

def on_message(mqtt_client, userdata, msg):
    print(f'Received message on topic: {msg.topic} with payload: {msg.payload}')


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(settings.MQTT_USERNAME, settings.MQTT_PASSWORD)
client.connect(
    host=settings.MQTT_BROKER_HOST,
    port=settings.MQTT_BROKER_PORT,
    keepalive=settings.MQTT_KEEPALIVE
)
client.loop_start()