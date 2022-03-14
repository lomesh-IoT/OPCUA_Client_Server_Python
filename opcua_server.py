from time import sleep
import random
from opcua import Server

server =  Server()
server.set_endpoint("opc.tcp://192.168.0.102:4840")
server.register_namespace("Room1")

objects = server.get_objects_node()

tempsens = objects.add_object('ns=2; s="TS1"', "temperature Sensor 1")

temp = tempsens.add_variable('ns=2;s="TS1_Temperature"', "TS1 Temperature", 20)

temperature = 20.0

try:
    print("Start Server")
    server.start()
    print("Server Online")
    while True:
        temperature += random.uniform(0, 1)
        temp.set_value(temperature)
        print("New Temperature: " +str(temp.get_value()))
        sleep(2)
finally:
    server.stop()
    print("Server Offline")

