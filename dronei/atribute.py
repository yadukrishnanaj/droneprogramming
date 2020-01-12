from dronekit import connect,VehicleMode,LocationGlobalRelative,APIException
import time
import socket
import exceptions
import math
import argparse
def connectMycopter():
    parser=argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect')
    args=parser.parse_args()
    connection_string=args.connect
    if not connection_string:
        import dronekit_sitl
        sitl=dronekit_sitl.start_default()
        connection_string=sitl.connection_string()

    vehicle=connect(connection_string,wait_ready=True)
    return vehicle

vehicle=connectMycopter()
vehicle.wait_ready('autopilot_version')
print("autopilotversion :%s"%vehicle.version)
print("altitude:%s" %vehicle.capabilities.set_attitude_target_local_ned)
print("altitude",vehicle.attitude)
print("velocity",vehicle.velocity)
