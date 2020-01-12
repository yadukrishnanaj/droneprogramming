from dronekit import connect,VehicleMode,APIException,LocationGlobalRelative
import dronekit_sitl
import time
import argparse

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

def armandtakeoff(targetheight):
	while vehicle.is_armable!=True:
		print("waiting to ge int armable")
		time.sleep(1)
	print("vehcle is now armable")

	vehicle.mode=VehicleMode("GUIDED")
	while vehicle.mode!="GUIDED":
		print("waiting to getint guided")
		time.sleep(1)
	print("mode cjanged to guide")

	vehicle.armed=True

	while vehicle.armed!=True:
		print("waiting to ge into armed")
		time.sleep(1)
	print("vehicle armed")

	vehicle.simple_takeoff(targetheight)

	while True:
		print(vehicle.location.global_relative_frame.alt)
		if vehicle.location.global_relative_frame.alt>=0.95*targetheight:
			break
		time.sleep(1)
	print("tarhet reached")
	vehicle.mode=VehicleMode("LAND")
	while vehicle.mode!="LAND":
		print("waitin to change to land")
		time.sleep(1)
	print("mode cahnged to land")
	while True:
		print(vehicle.location.global_relative_frame.alt)
		if vehicle.location.global_relative_frame.alt<=0:
			break
		time.sleep(1)
	print("vehicllanded")
	return None
     
vehicle=connectmycopter()
armandtakeoff(10)
vehicle.close()





