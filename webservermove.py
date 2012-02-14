#!/usr/bin/env python

# This script helps in the moving process of web servers (files, databases)

import ConfigParser, os, requests
from subprocess import call

# global vars
currentdir = os.getcwd()
configfile = os.path.join(currentdir, "webservermove.ini")

def getdefaultconfig():
	# Downloads a example config
	r = requests.get("https://raw.github.com/staticsafe/useful-scripts/master/webservermove.ini")
	
	file_name = "webservermove.ini"
	f = open(file_name, wb)

	f.write(r.content)
	f.close()

	print "Config file downloaded!"
	main()

def setvalues():
	# global vars...again
	global srcusername
	global srcpassword
	global srchostname
	global srcfiledir
	global srcdbname
	global srcmysqlrootpw

	global destusername
	global destpassword
	global desthostname
	global destfiledir
	global destdbdir

	# Get values from config file
	srcconfig = ConfigParser.ConfigParser()
	srcconfig.read('webservermove.ini')

	srcusername = srcconfig.get('SOURCEHOST', 'srcusername')
	srcpassword = srcconfig.get('SOURCEHOST', 'srcpassword')
	srchostname = srcconfig.get('SOURCEHOST', 'srchostname')
	srcfiledir = srcconfig.get('SOURCEHOST', 'srcfiledir')
	srcdbname = srcconfig.get('SOURCEHOST', 'srcdbname')
	srcmysqlrootpw = srcconfig.get('SOURCEHOST', 'srcmysqlrootpw')

	destconfig = ConfigParser.ConfigParser()
	destconfig.read('webservermove.ini')

	destusername = destconfig.get('DESTHOST', 'destusername')
	destpassword = destconfig.get('DESTHOST', 'destpassword')
	desthostname = destconfig.get('DESTHOST', 'desthostname')
	destfiledir = destconfig.get('DESTHOST', 'destfiledir')
	destdbdir = destconfig.get('DESTHOST', 'destdbdir')

def filemove():
	print "placeholder"

def dbmove():
	print "placeholder"

def main():
	# check existence of config file
	if os.path.isfile(configfile) == False:
		print "A config file does not exist, downloading a example config now!"
		getdefaultconfig()
	else:
		print "Config file exists, using it!"

	setvalues()
	filemove()
	dbmove()

if __name__ == "__main__":
	main()