import Tkinter as Tkinter
from dronekit import connect,VehicleMode,LocationGlobalRelative,APIException
import dronekit_sitl
import time
from pymavlink import mavutil
import Tkinter as tk
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
		print("running prearm checks")
		time.sleep(1)
	vehicle.mode=VehicleMode("GUIDED")
	while vehicle.mode!="GUIDED":
		print("waiting to guided")
		time.sleep(1)

	vehicle.armed=True
	while vehicle.armed!=True:
		print("waiting to get in rmed")
		time.sleep(1)
	print("armed ready")

	vehicle.simple_takeoff(targetheight)

	while True:
		print(vehicle.location.global_relative_frame.alt)
		if vehicle.location.global_relative_frame.alt>=0.95*targetheight:
			time.sleep(2)
			break
		time.sleep(1)
	print("altitude reached")

	return None

def setvelocity(vehicle,vx,vy,vz):
    msg=vehicle.message_factory.set_position_target_local_ned_encode(0,0,0,mavutil.mavlink.MAV_FRAME_BODY_NED,0b0000111111000111,0,0,0,vx,vy,vz,0,0,0,0,0)
    vehicle.send_mavlink(msg)
    vehicle.flush()

def key(event):
    if event.char==event.keysym:
        if event.keysym=="r":
            print("mode land")
            vehicle.mode=VehicleMode("RTL")
        elif event.keysym=="u":
        	print("movin up")
        	setvelocity(vehicle,5,0,0)
        elif event.keysym=="j":
        	setvelocity(vehicle,-5,0,0)
        	print("moving down")
        elif event.keysym=="h":
        	print("moving left")
        	setvelocity(vehicle,0,-5,0)
        elif event.keysym=="k":
        	print("moving right")
        	setvelocity(vehicle,0,5,0)


vehicle=connectmycopter()

armandtakeoff(10)

root = tk.Tk()
print(">> Control the drone with the arrow keys. Press r for RTL mode")
root.bind_all('<Key>', key)
root.mainloop()