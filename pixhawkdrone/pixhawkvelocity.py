from dronekit import connect,VehicleMode,LocationGlobalRelative
import time
from pymavlink import mavutil
import argparse
import dronekit_sitl
def connectcopter():
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
		print("waiting running")
		time.sleep(1)

	print("vehicle is now armable")

	vehicle.mode=VehicleMode("GUIDED")
	while vehicle.mode!="GUIDED":
		print("waiting to change into guided")
		time.sleep(1)
	print("vehicle is no in guided")

	vehicle.armed=True
	while vehicle.armed!=True:
		print("vehicle arming wait--")
		time.sleep(1)
	print("VEHICLE ARMED")


	vehicle.simple_takeoff(targetheight)

	while True:
		print(vehicle.location.global_relative_frame.alt)
		if vehicle.location.global_relative_frame.alt>=0.95*targetheight:
			time.sleep(2)
			break
		time.sleep(1)
	print("reached")
	print(vehicle.location.global_relative_frame.alt)
	print("*******")
	return None


def vehiclevelocity(vx,vy,vz):
	msg=vehicle.message_factory.set_position_target_local_ned_encode(0,0,0,mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED,0b0000111111000111,0,0,0,vx,vy,vz,0,0,0,0,0)
	vehicle.send_mavlink(msg)
	vehicle.flush()


vehicle=connectcopter()
armandtakeoff(10)

counter=0
while counter<1:
	vehiclevelocity(0,0,-0.25)
	print("vehicle moving")
	counter=counter+1
	time.sleep(1)
print(vehicle.location.global_relative_frame.alt)

while True:
	time.sleep(1)