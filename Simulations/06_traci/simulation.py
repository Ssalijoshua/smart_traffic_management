#!/usr/bin/env python
import os
import sys
import subprocess

# we need to import python modules from the $SUMO_HOME/tools directory
sys.path.append(os.path.join(os.environ["SUMO_HOME"], "tools"))
from sumolib import checkBinary
import traci

PORT = 8816

# select whether to start the graphical or the batch simulation
sumoExe = checkBinary("sumo-gui") if len(sys.argv) == 1 else checkBinary("sumo")
# start the simulation 
sumoProcess = subprocess.Popen([sumoExe, "-c", "osm.sumocfg", "--remote-port", str(PORT)],
                               stdout=sys.stdout, stderr=sys.stderr)
# connect to the simulation
traci.init(PORT)

traci.simulationStep(80000)
traci.route.add("r", "290619181#3 290619181#4".split())
traci.vehicle.add("x", "r")
traci.simulationStep()
traci.vehicle.setSpeedMode("x", 0) # disable all checks
traci.vehicle.setSpeed("x", 20)
traci.simulationStep(2000000)

# disconnect from the simulation
traci.close()
sumoProcess.wait()
