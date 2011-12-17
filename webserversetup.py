#!/usr/bin/env python

import os
from subprocess import call
import sys


def main():
#rootcheck
uid = os.getuid()
if uid != 0:
	print "This script must be run as root or sudo if you have it!"
	sys.exit()
#distrocheck
if os.path.isfile(/etc/fedora-release) = True:
	webserverfedora()
	installcpfedora()
elif os.path.isfile(/etc/debian_version) = True:
	webserverdebian()
	installcpfedora()
elif os.path.isfile(/etc/arch-release) = True:
	webserverarch()
	installcparch()
else:
	print "This is script is not supported for your OS, exiting."
	sys.exit()



def webserverdebian():



def webserverfedora():



def webserverarch():



def installcpdebian():



def installcpfedora():



def installcparch():



