#!/usr/bin/env python

import os
from subprocess import call
import sys
import platform


def main():
#rootcheck
uid = os.getuid()
if uid != 0:
	print "This script must be run as root or sudo if you have it!"
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



def webserverdebian():
print "Choose a webserver to install, your choices are Apache, Lightttpd, nginx, or Cherokee"
prompt = ">"
answer = raw_input(prompt)
if answer == "Apache" or answer == "apache":
	installprocessapache = call("apt-get install --assume-yes mysql-server mysql-client apache2 apache2-doc php5 php5-mysql libapache2-mod-php5")
	print "Stopping started LAMP services so you can configure them properly."
	stopservicesapache = call ("/etc/init.d/apache stop && /etc/init.d/mysql stop")
elif answer == "Lighttpd" or answer == "lighttpd":
	installprocesslighttpd = call ("apt-get install --assume-yes lighttpd mysql-server mysql-client php5-mysql")
	print "Stopping started LAMP services so you can configure them properly."
	stopserviceslighttpd = call ("/etc/init.d/lighttpd stop && /etc/init.d/mysql stop")
	print "Look at http://goo.gl/i4NlE for instructions on how to configure lighttpd."
elif answer == "nginx" or answer == "Nginx":
	installprocessnginx = call ("apt-get install --assume-yes nginx php5-cli php5-cgi spawn-fcgi mysql-server mysql-client php5-mysql")
	print "Stopping services so you can configure them properly"
	stopservicesnginx = call ("/etc/init.d/nginx stop && /etc/init.d/mysql stop")
	print "Look at http://goo.gl/tQBe7 for instructions on how to configure php-fastcgi"
elif answer == "Cherokee" or answer == "cherokee":
	installprocesscherokee = call ("apt-get install --assume-yes cherokee mysql-server mysql-client php5-mysql openssl")
	print "Stopping services so you can configure them properly"
	stopservicescherokee = call ("/etc/init.d/cherokee stop && /etc/init.d/mysql stop")
else:
	print "Input is invalid, please retry!"
	webserverdebian()



def webserverfedora():
print "Choose a webserver to install, your choices are Apache, Lightttpd, nginx, or Cherokee"
prompt = ">"
answer = raw_input(prompt)
if answer == "Apache" or answer == "apache":
	installprocessapache = call ("yum install httpd mysql mysql-server php php-mysql")
	print "Stopping services so you can configure them properly"
	stopservicesapache = call ("/sbin/service httpd stop")
	print "Adding httpd to autostart"
	autostartapache = call ("/sbin/chkconfig httpd on")
else:
	print "other webservers are not supported at the moment sorry. Support will be added in the future"



def webserverarch():



def installcpdebian():
print "Do you want to install a control panel (Webmin and/or phpmyAdmin)?"
prompt = ">"
answer = raw_input(prompt)
if answer == "No" or "no":
	print "Alright then, exiting."
	sys.exit()
elif answer == "Yes" or "yes":
	print "Do you want to install phpmyAdmin?"
	promptpma = ">"
	answerpma = raw_input(promptpma)
	if answerpma == "Yes" or answerpma == "yes":
		installcppma = call ("apt-get install --assume-yes phpmyadmin")
	elif answerpma == "No" or answerpma == "no":
		print "Alright then!"
	else:
		installcpdebian()
	print "Do you want to install Webmin?"
	promptwebmin ">"
	answerwebmin = raw_input(promptwebmin)
	if answerwebmin == "Yes" or answerwebmin "yes":
		print "installing Webmin"
		getkey = call ("wget http://www.webmin.com/jcameron-key.asc && apt-key add jcameron-key.asc")
		print "Adding Webmin repo to sources list"
		addsource = call ("echo 'deb http://download.webmin.com/download/repository sarge contrib' >> /etc/apt/sources.list")
		aptupdate = call ("apt-get update")
		installwebmin = call ("apt-get install --assume-yes webmin")
	elif answerwebmin == "No" or answerwebmin == "no":
		print "Alright then, we are done here. Exiting."
		sys.exit()
	else:
		installcpdebian()
else:
	installcpdebian()





def installcpfedora():



def installcparch():



