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


def webserverdebian():



def webserverfedora():


def webserverarch():

def installcp():