#!/usr/bin/env python

import os
from subprocess import call
import sys
import platform

def webserverdebian():

	print 'Choose a webserver to install, your choices are Apache, Lightttpd, nginx, or Cherokee'
	prompt = ">"
	answer = raw_input(prompt)
	if answer == "Apache" or answer == "apache":
		installprocessapache = call("apt-get install --assume-yes mysql-server mysql-client apache2 apache2-doc php5 php5-mysql libapache2-mod-php5", shell=True)
		print "Stopping started LAMP services so you can configure them properly."
		stopservicesapache = call ("/etc/init.d/apache2 stop && /etc/init.d/mysql stop", shell=True)
	elif answer == "Lighttpd" or answer == "lighttpd":
		installprocesslighttpd = call ("apt-get install --assume-yes lighttpd mysql-server mysql-client php5-mysql", shell=True)
		print "Stopping started LAMP services so you can configure them properly."
		stopserviceslighttpd = call ("/etc/init.d/lighttpd stop && /etc/init.d/mysql stop", shell=True)
		print "Look at http://goo.gl/i4NlE for instructions on how to configure lighttpd."
	elif answer == "nginx" or answer == "Nginx":
		installprocessnginx = call ("apt-get install --assume-yes nginx php5-cli php5-cgi spawn-fcgi mysql-server mysql-client php5-mysql", shell=True)
		print "Stopping services so you can configure them properly"
		stopservicesnginx = call ("/etc/init.d/nginx stop && /etc/init.d/mysql stop", shell=True)
		print "Look at http://goo.gl/tQBe7 for instructions on how to configure php-fastcgi"
	elif answer == "Cherokee" or answer == "cherokee":
		installprocesscherokee = call ("apt-get install --assume-yes cherokee mysql-server mysql-client php5-mysql openssl", shell=True)
		print "Stopping services so you can configure them properly"
		stopservicescherokee = call ("/etc/init.d/cherokee stop && /etc/init.d/mysql stop", shell=True)
	else:
		print "Input is invalid, please retry!"
		webserverdebian()

def installcpdebian():

	print 'Do you want to install a control panel (Webmin and/or phpmyAdmin)?'
	prompt = ">"
	answer = raw_input(prompt)
	if answer == "No" or answer == "no":
		print "Alright then, exiting."
		sys.exit()
	elif answer == "Yes" or answer == "yes":
		print "Do you want to install phpmyAdmin?"
		promptpma = ">"
		answerpma = raw_input(promptpma)
	else:
		installcpdebian()
		
	if answerpma == "Yes" or answerpma == "yes":
		installcppma = call ("apt-get install --assume-yes phpmyadmin", shell=True)
	elif answerpma == "No" or answerpma == "no":
		print "Alright then!"
	else:
		installcpdebian()

	
	print "Do you want to install Webmin?"
	promptwebmin = ">"
	answerwebmin = raw_input(promptwebmin)
	if answerwebmin == "Yes" or answerwebmin == "yes":
		print "installing Webmin"
		getkey = call ("wget http://www.webmin.com/jcameron-key.asc && apt-key add jcameron-key.asc", shell=True)
		print "Adding Webmin repo to sources list"
		addsource = call ("echo 'deb http://download.webmin.com/download/repository sarge contrib' >> /etc/apt/sources.list", shell=True)
		aptupdate = call ("apt-get update", shell=True)
		installwebmin = call ("apt-get install --assume-yes webmin", shell=True)
	elif answerwebmin == "No" or answerwebmin == "no":
		print "Alright then, we are done here. Exiting."
		sys.exit()
	else:
		installcpdebian()

	sys.exit()

def webserverfedora():

	print "Choose a webserver to install, your choices are Apache, Lightttpd, nginx, or Cherokee"
	prompt = ">"
	answer = raw_input(prompt)
	if answer == "Apache" or answer == "apache":
		installprocessapache = call ("yum install -y httpd mysql mysql-server php php-mysql", shell=True)
		print "Stopping services so you can configure them properly"
		stopservicesapache = call ("/sbin/service httpd stop", shell=True)
		print "Adding httpd to autostart"
		autostartapache = call ("/sbin/chkconfig httpd on", shell=True)
	else:
		print "other webservers are not supported at the moment sorry. Support will be added in the future"

def installcpfedora():

	print 'Do you want to install a control panel (Webmin and/or phpmyAdmin)?'
	prompt = ">"
	answer = raw_input(prompt)
	if answer == "No" or answer == "no":
		print "Alright then, exiting."
		sys.exit()
	elif answer == "Yes" or answer == "yes":
		print "Do you want to install phpmyAdmin?"
		promptpma = ">"
		answerpma = raw_input(promptpma)
	else:
		installcpfedora()
		
	if answerpma == "Yes" or answerpma == "yes":
		installcppma = call ("yum install -y phpmyadmin", shell=True)
	elif answerpma == "No" or answerpma == "no":
		print "Alright then!"
	else:
		installcpfedora()

	
	print "Do you want to install Webmin?"
	promptwebmin = ">"
	answerwebmin = raw_input(promptwebmin)
	if answerwebmin == "Yes" or answerwebmin == "yes":
		print "Adding Webmin Repo"
		getrepofile = call ("wget -O /etc/yum.repos.d/webmin.repo http://dl.dropbox.com/u/2888062/Docs/webmin.repo", shell=True)
		getkey = call("wget http://www.webmin.com/jcameron-key.asc && rpm --import jcameron-key.asc", shell=True)
		installwebmin = call("yum install -y webmin", shell=True)
	elif answerwebmin == "No" or answerwebmin == "no":
		print "Alright then, we are done here. Exiting."
		sys.exit()
	else:
		installcpfedora()

	sys.exit()

def main():
	#rootcheck
	uid = os.getuid()
	if uid != 0:
		print 'This script must be run as root or sudo if you have it!'
		sys.exit()
	#distrocheck
	userdistro = platform.linux_distribution()

	if userdistro[0] == "Fedora":
		webserverfedora()
		installcpfedora()
	elif userdistro[0] == "debian":
		webserverdebian()
		installcpdebian()
	elif userdistro[0] == "Arch":
		webserverarch()
		installcparch()
	elif userdistro[0] == "Ubuntu":
		webserverdebian()
		installcpdebian()
	else:
		print "This is script is not supported for your distro, exiting."
		sys.exit()

if __name__ == "__main__":
	main()





