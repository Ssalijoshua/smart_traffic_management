#!/usr/bin/env python
import os
import sys
import subprocess

# we need to import python modules from the $SUMO_HOME/tools directory
sys.path.append(os.path.join(os.environ["SUMO_HOME"], "tools"))
from sumolib import checkBinary
import traci
# the port used for communicating with your sumo instance
PORT = 8873
TLS_ID = "1814203922"

# this is the main entry point of this script
# this is the normal way of using traci. sumo is started as a
# subprocess and then the python script connects and runs
sumoProcess = subprocess.Popen([checkBinary("sumo-gui"), "-c", "osm.sumocfg", "--remote-port", str(PORT)],
                               stdout=sys.stdout, stderr=sys.stderr)
traci.init(PORT)
while traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()
    if traci.trafficlights.getPhase(TLS_ID) == 0:
        # we are not already switching
        if traci.inductionloop.getLastStepVehicleNumber("0") > 0:
            # there is a vehicle from the west, switch
            traci.trafficlights.setPhase(TLS_ID, 1)
        else:
            # otherwise try to keep green for the north
            traci.trafficlights.setPhase(TLS_ID, 0)
traci.close()
sumoProcess.wait()
