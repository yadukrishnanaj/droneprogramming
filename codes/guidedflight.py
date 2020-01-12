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
	return None

def get_distannce(targetlocation,currentlocation):
	dlat=targetlocation.lat-currentlocation.lat
	dlong=targetlocation.lon-currentlocation.lat

	return math.sqrt((dlat*dlat)+(dlong*dlong))*1.113195e5

def goto(targetlocation):
	distance=get_distannce(targetlocation,vehicle.location.global_relative_frame)
	vehicle.simple_goto(targetlocation)
	while vehicle.mode.name=="GUIDED":
		currentdistnce=get_distannce(targetlocation,vehicle.location.global_relative_frame)
		if currentdistnce<=0.01*distance:
			print("reachde")
			break
			time.sleep(2)
		time.sleep(1)
	return None





wp1=LocationGlobalRelative(10.12057624,76.35245919,10)
vehicle=connectmy()
armandtakeoff(10)
goto(wp1)
