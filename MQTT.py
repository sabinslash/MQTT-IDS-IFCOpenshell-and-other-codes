"""import time 
from paho.mqtt import client as mqtt
def on_connect(client, userdata, flags, rc): 
    client.subscribe("test")
def on_message(client, userdata, msg):
    print(f"Received {str(msg.payload)} from {msg.topic}")
    
client = mqtt.Client() 
client.on_connect = on_connect 
client.on_message = on_message
client.connect("xrdevmqtt.edu.metropolia.fi", 1883, 60)
client.loop_start()
for m in range(10):
    time.sleep(3)
client.publish("test", f"Message {m}") 
print(f"Published message {m} to test")
client.loop_stop()
"""
from paho.mqtt import client as mqtt
# 1. Create a client instance
client = mqtt.Client()
# 2. Define callback function
def on_connect(client, userdata, flags, rc):
    client.subscribe("M-bus/Electricity/Current L2")
def on_message(client, userdata, msg):
         print(msg.topic+" "+str(msg.payload))
client.on_connect = on_connect
client.on_message = on_message
# 1. Connect to a broker with one of the connect*() functions
client.connect("xrdevmqtt.edu.metropolia.fi", 1883, 60)
# 1. Call one of the loop*() functions to maintain network traffic flow with the broker
client.loop_forever()