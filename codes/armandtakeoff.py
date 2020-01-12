from dronekit import VehicleMode,LocationGlobalRelative,connect,APIException
import socket
import time
import exceptions
import math
import argparse

def connectmycopter():
	import dronekit_sitl
	sitl=dronekit_sitl.start_default()
	connection_string=sitl.connection_string()
	vehicle=connect(connection_string,wait_ready=True)
	return vehicle

def armandtakeoff(targetheight):
	while vehicle.is_armable == False:
		print("waiting")
		time.sleep(1)
	print("ready")

	vehicle.mode=VehicleMode("GUIDED")
	while vehicle.mode !="GUIDED":
		time.sleep(1)
		print("waitng to cahan")
	print("mode guide")

	vehicle.armed=True
	while vehicle.armed == False:
		print("waiting for armin")
		time.sleep(1)
	print("vehicle armed")
	vehicle.simple_takeoff(targetheight)
	while True:
		print(vehicle.location.global_relative_frame.alt)
		if vehicle.location.global_relative_frame.alt>=.95*targetheight:
			print(vehicle.location.global_relative_frame.alt)
			break
		time.sleep(1)

	print("reached")
	return None

vehicle=connectmycopter()
armandtakeoff(10)