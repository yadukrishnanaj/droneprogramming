from dronekit import connect,VehicleMode,LocationGlobalRelative,APIException
import dronekit_sitl
import time
import argparse
import math
def connectmycopter():
	parser=argparse.ArgumentParser(description="commands")
	parser.add_argument("--connect")
	args=parser.parse_args()
	connection_string=args.connect
	if not connection_string:
		sitl=dronekit_sitl.start_default()
		connection_string=sitl.connection_string()
	vehicle=connect(connection_string,wait_ready=True)
	return vehicle


def armandtakeoff(targethieght):
	while vehicle.is_armable!=True:
		print("carrying outprearmchecks")
		time.sleep(1)
	print("prearm check finished")

	vehicle.mode=VehicleMode("GUIDED")
	while vehicle.mode!="GUIDED":
		print("waiting to change int guided")
		time.sleep(1)
	print("vehiclenow in guided")

	vehicle.armed=True
	while vehicle.armed!=True:
		print("waiting or vehicle to change to arm")
		time.sleep(1)
	print("vehiclearmed")

	vehicle.simple_takeoff(targethieght)

	while True:
		print(vehicle.location.global_relative_frame.alt)
		if vehicle.location.global_relative_frame.alt>=0.95*targethieght:
			break
		time.sleep(1)
	print("target reached")
	return None

def calculatedistance(target,current):
	dlat=target.lat-current.lat
	dlon=target.lon-current.lat
	return math.sqrt((dlon*dlon)+(dlat*dlat))*1.113195e5


def carrymission(target):
	actualdistance=calculatedistance(target,vehicle.location.global_relative_frame)
	vehicle.simple_goto(target)
	while vehicle.mode=="GUIDED":
		currentdist=calculatedistance(target,vehicle.location.global_relative_frame)
		if currentdist<0.01*actualdistance:
			time.sleep(2)
			break
			time.sleep(2)
		time.sleep(1)
	print("target reached")
	return None

wp1=LocationGlobalRelative(10.12057624,76.35245919,10)
vehicle=connectmycopter()
armandtakeoff(10)
carrymission(wp1)
vehicle.mode=VehicleMode("LAND")

while vehicle.mode!="LAND":
	print("waiting to change to land")
print("changedtoland")
while true:
	sleep(1)
vehicle.close()


