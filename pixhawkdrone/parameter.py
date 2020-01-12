import dronekit_sitl
from dronekit import connect,VehicleMode,LocationGlobalRelative,APIException
import time
import socket

def connectmycopter():
    sitl=dronekit_sitl.start_default()
    connection_string=sitl.connection_string()
    vehicle=connect(connection_string,wait_ready=True)
    return vehicle


vehicle=connectmycopter()
gps=vehicle.parameters['GPS_TYPE']
print(gps)
vehicle.close()
