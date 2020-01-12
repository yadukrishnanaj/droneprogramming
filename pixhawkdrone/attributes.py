from dronekit import connect,VehicleMode,LocationGlobalRelative,APIException
import dronekit_sitl
import time
import socket

import math

def connectmycopter():
	sitl=dronekit_sitl.start_default()
	connection_string=sitl.connection_string()
	vehicle=connect(connection_string,wait_ready=True)
	return vehicle



vehicle=connectmycopter()
vehicle.wait_ready('autopilot_version')
print(vehicle.version)
print("vehicle attitude")
print(vehicle.attitude.pitch)
print(vehicle.attitude.roll)
print(vehicle.attitude.yaw)
print(vehicle.airspeed)
print(vehicle.groundspeed)
print(vehicle.mode.name)
print(vehicle.location.global_relative_frame)
print(vehicle.last_heartbeat)
print(vehicle.velocity[0])
vehicle.close()