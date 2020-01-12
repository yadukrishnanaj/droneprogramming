from dronekit import connect,VehicleMode,LocationGlobalRelative,APIException
import time
import argparse
from pymavlink import mavutil
import dronekit_sitl

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
		print("running prearmchecks")
		time.sleep(1)
	print("vehicle now armable")

	vehicle.mode=VehicleMode("GUIDED")
	while vehicle.mode!="GUIDED":
		print("waiting to get guide")
		time.sleep(1)
	print("mode changed to guided")

	vehicle.armed=True
	while vehicle.armed!=True:
		print("vehicle waiting to get armed")
		time.sleep(1)
	print("vehicle armed")

	

def send_local_ned_velocity(vx,vy,vz):
	msg=vehicle.message_factory.set_position_target_local_ned_encode(0,0,0,mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED,0b0000111111000111,0,0,0,vx,vy,vz,0,0,0,0,0)
	vehicle.send_mavlink(msg)
	vehicle.flush()


def send_global_ned_velocity(vx,vy,vz):
	msg=vehicle.message_factory.set_position_target_local_ned_encode(0,0,0,mavutil.mavlink.MAV_FRAME_LOCAL_OFFSET_NED,0b0000111111000111,0,0,0,vx,vy,vz,0,0,0,0,0)
	vehicle.send_mavlink(msg)
	vehicle.flush()

vehicle=connectmycopter()
armandtakeoff(10)
counter=0
while counter<5:
	send_local_ned_velocity(5,0,0)
	print("moving")
	time.sleep(1)
	counter=counter+1

while True:
	time.sleep(1)


