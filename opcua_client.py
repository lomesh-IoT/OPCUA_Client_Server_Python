from opcua import Client
from time import sleep


client = Client("opc.tcp://127.0.0.1:12345")

client.connect()

objects = client.get_objects_node()

client.get_namespace_array()

objects = client.get_objects_node()

tempsens = objects.get_children()[1]

tempsens.get_children()

temp = client.get_node('ns=2;s="TS1_Temperature"')

try:
    while True:
        print(temp.get_value())
        sleep(2)

finally:
    client.close_session()



