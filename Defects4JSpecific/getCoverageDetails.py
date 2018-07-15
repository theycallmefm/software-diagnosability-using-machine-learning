# PURPOSE:script to get coverage of test suite for Defects4J defects
# INPUT: script requires <path-to-defects4j> as command line argument
# OUTPUT: output of the script is Defects4JCoverage.csv that lists Project, DefectId, and StatementCoverage for all the defects of Defects4J 
# HOW TO RUN: run the script using command: python getCoverageDetails.py <path-to-defects4j>
# REQUIREMENTS AND DEPENDENCIES: script requires Defects4J installed on system"

import os
import subprocess
import sys

if len(sys.argv) < 2:
	print ("ERROR: Please provide path to Defects4J directory")
	sys.exit()

defects4jpath = str(sys.argv[1])                           # path to Defects4J 
outputfile = open("Defects4JCoverage_2.csv", 'a')			
outputfile.write("Project,DefectId,StatementCoverage\n")
projects = [ "Closure"] 
noofdefects = {}
#noofdefects["Chart"] = 26
noofdefects["Closure"] = 133
#noofdefects["Lang"] = 65
#noofdefects["Math"] = 106
#noofdefects["Time"] = 27

for proj in projects: 
	for i in range(118,noofdefects[proj]+1):
		command = defects4jpath + "/framework/bin/defects4j checkout -p " + proj + " -v " + str(i) + "b -w /Users/handekaratay/Desktop/defects4j/tmp/" + proj.lower() + "_" + str(i) + "_buggy"
		print (command)
		checkoutput = subprocess.getoutput(command)
		if checkoutput:
			os.chdir("/Users/handekaratay/Desktop/defects4j/tmp/" + proj.lower() + "_" + str(i) + "_buggy")
			command = defects4jpath + "/framework/bin/defects4j coverage"
			print (command)
			covoutput = subprocess.getoutput(command)
			print(covoutput)
			lines=covoutput.split('\n')
			found=0
			for l in lines:
		 		if l.find("Line coverage:")!=-1 :
		 			found=1
		 			stmtcoverage = l[l.find(":")+2:len(l)]
			if found==1:
				outline = proj + "," + str(i) + "," + str(stmtcoverage)
				outputfile.write(outline)
				outputfile.write('\n')
		
outputfile.close()
