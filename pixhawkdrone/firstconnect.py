from dronekit import connect,VehicleMode,LocationGlobalRelative,APIException
import socket
import time
import math
import argparse
import dronekit_sitl


def connectto_copter():
	sitl=dronekit_sitl.start_default()
	connection_string=sitl.connection_string()

	vehicle=connect(connection_string,wait_ready=True)

	return vehicle

vehicle=connectto_copter()
vehicle.close()
