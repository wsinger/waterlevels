from lxml import etree
from subprocess import call
import tarfile

# import the ciop functions (e.g. copy, log)
import cioppy 
ciop = cioppy.Cioppy()
#==============================================================================

#get params from xml
startdate   = ciop.getparam("startdate") 
enddate     = ciop.getparam("enddate")
minpoints   = ciop.getparam("minpoints")
maxstderror = ciop.getparam("maxstderror")
plotname    = ciop.getparam("plotname") 

variables = " minpoints = " + str(minpoints) + ";"
variables = variables + " max_stderror = " + str(maxstderror) + ";"
variables = variables + " plotName = " + str(plotName) + ";"
variables = variables + " startdate = " + str(startdate) + ";"
variables = variables + " enddate = " + str(enddate) + ";"

#run matlab script/application
subprocess.call("cd ./resources")
command = "matlab -nodesktop -nosplash -r \"addpath(\'functions\',\'plotting\',\'read_data\');" + variables + " structs; exit()\""
subprocess.call(command)
subprocess.call("cd ..")

#publish everything in /outputs
ciop.publish("./resources/outputs",recursive=True,metalink=True)
#clear /outputs
command = "rm ./resources/outputs/*"
subprocess.call(command)

