from dronekit import connect,VehicleMode,LocationGlobalRelative,APIException
import time
import argparse
import os
import dronekit_sitl
a=os.getcwd()
print(a)


def connectmycopter():
	parser=argparse.ArgumentParser(description='commands')
	parser.add_argument("--connect")
	args=parser.parse_args()
	connection_string=args.connect
	if not connection_string:
		sitl=dronekit_sitl.start_default()
		connection_string=sitl.connection_string()
	vehicle=connect(connection_string,wait_ready=True)
	return vehicle

vehicle=connectmycopter()
print("version")
print(vehicle.version)
print("attitude")
print(vehicle.attitude)
print("velocity")
print(vehicle.velocity)
print("loation global")
print(vehicle.location.global_relative_frame)
print("vehicle local")
print(vehicle.location.global_frame)
print("locayion local fram")
print(vehicle.location.local_frame)
print("vehicle batery")
print(vehicle.battery)
print("vehicel home location")
print(vehicle.home_location)
print("vehicel status")
print(vehicle.system_status)
vehicle.close()

