from dronekit import connect,VehicleMode,LocationGlobalRelative,APIException
import socket
import time
import exceptions
import math
import argparse

def connectmy():
	parser=argparse.ArgumentParser(description="commands")
	parser.add_argument('--connect')
	args=parser.parse_args()
	connection_string=args.connect
	if not connection_string:
		import dronekit_sitl
		sitl=dronekit_sitl.start_default()
		connection_string=sitl.connection_string()
	vehicle=connect(connection_string,wait_ready=True)
	return vehicle

vehicle=connectmy()
print("vehicleversion%s",vehicle.version)
print("vehic;capba%s",vehicle.capabilities.set_attitude_target_local_ned)
print("vehicle location%s",vehicle.location.global_relative_frame)
print("vehicleattitude%s",vehicle.attitude)
print("vehiclevelocity%s",vehicle.velocity)
print("vehicleground%s",vehicle.groundspeed)
print("ekd",vehicle.armed)
#vehicle=connectmy()
vehicle.close()