from dronekit import connect,VehicleMode,APIException,LocationGlobalRelative,Command
import dronekit_sitl
import time
import argparse
from pymavlink import mavutil 
#standard version
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
	print("mode changed to guide")

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
	print("target reached")
	'''vehicle.mode=VehicleMode("LAND")
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
	return None'''
     
vehicle=connectmycopter()
whome=vehicle.location.global_relative_frame
cmd1=Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,whome.lat,whome.lon,whome.alt)
cmd2=Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,10.027709,76.328377,10)
cmd3=Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,10.027559,76.328475,10)
cmd4=Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,10.027799,76.32861,10)
cmd5=Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH,0,0,0,0,0,0,0,0,0)
cmds=vehicle.commands
cmds.download()
cmds.wait_ready()
cmds.clear()
cmds.add(cmd1)
cmds.add(cmd2)
cmds.add(cmd3)
cmds.add(cmd4)
cmds.add(cmd5)


vehicle.commands.upload()
armandtakeoff(10)
print("after arm and takeoof")
vehicle.mode=VehicleMode("AUTO")
while vehicle.mode!="AUTO":
    print("waiting to get in auto")
    time.sleep(1)



while vehicle.location.global_relative_frame.alt>2:
    print("drone is executing mission")
    time.sleep(1)



#vehicle.close()





