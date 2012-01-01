#!/usr/bin/env python

#Web server setup for Debian/Ubuntu, Fedora, Arch Linux
#NOTE - DOES NOT CONFIGURE WEBSERVERS
#Thanks to cafejunkie & BiriBiri for all their help <3.

#Feature to-dos:
#	-CLI arguments
#	-Support more webservers for Fedora 

import os
from subprocess import call
import platform
import re

#Debian
def webserverdebian():

	print 'Choose a webserver to install, your choices are Apache, Lightttpd, nginx, or Cherokee'
	prompt = ">"
	answer = raw_input(prompt)
	regexa = re.match(r'apache', answer, re.M|re.I)
	if answer == regexa:
		installprocessapache = call("apt-get install --assume-yes mysql-server mysql-client apache2 apache2-doc php5 php5-mysql libapache2-mod-php5", shell=True)
		print "Stopping started LAMP services so you can configure them properly."
		stopservicesapache = call ("/etc/init.d/apache2 stop && /etc/init.d/mysql stop", shell=True)
	elif answer == "Lighttpd" or answer == "lighttpd":
		installprocesslighttpd = call ("apt-get install --assume-yes lighttpd mysql-server mysql-client php5-mysql", shell=True)
		print "Stopping services so you can configure them properly."
		stopserviceslighttpd = call ("/etc/init.d/lighttpd stop && /etc/init.d/mysql stop", shell=True)
		print "Look at http://goo.gl/i4NlE for instructions on how to configure lighttpd."
	elif answer == "nginx" or answer == "Nginx":
		userdistro = platform.linux_distribution()
		if userdistro[0] == "debian":
			print 'adding nginx repo to sources'
			addnginxsource = call ("echo 'deb http://packages.dotdeb.org stable all' >> /etc/apt/sources.list", shell=True)
			addnginxkey = call ("wget http://www.dotdeb.org/dotdeb.gpg && cat dotdeb.gpg | sudo apt-key add -", shell=True)
			installnginxdebian = call ("apt-get update && apt-get install --assume-yes nginx php5 php5-fpm php-pear php5-common php5-mcrypt php5-mysql php5-cli php5-gd mysql-server mysql-client", shell=True)
			print "Stopping services so you can configure them properly"
			stopservicesnginx = call ("/etc/init.d/nginx stop && /etc/init.d/mysql stop", shell=True)
			print "Look at http://goo.gl/dyihP for instructions on how to configure nginx"
		elif userdistro[0] == "Ubuntu":
			installprocessnginx = call ("apt-get install --assume-yes nginx php5-fpm mysql-server mysql-client php5-mysql", shell=True)
			print "Stopping services so you can configure them properly"
			stopservicesnginx2 = call ("/etc/init.d/nginx stop && /etc/init.d/mysql stop", shell=True)
			print "Look at http://goo.gl/dyihP for instructions on how to configure nginx"
		else:
			webserverdebian()
	elif answer == "Cherokee" or answer == "cherokee":
		userdistro2 = platform.linux_distribution()
		if userdistro2[0] == "debian":
			print 'adding cherokee repo to sources'
			addnginxsource = call ("echo 'deb http://packages.dotdeb.org stable all' >> /etc/apt/sources.list", shell=True)
			addnginxkey = call ("wget http://www.dotdeb.org/dotdeb.gpg && cat dotdeb.gpg | sudo apt-key add -", shell=True)
			updatingsources = call ("apt-get update", shell=True)
			installprocesscherokee = call ("apt-get install --assume-yes cherokee php5-fpm mysql-server mysql-client php5-mysql libcherokee-mod-mysql libcherokee-mod-libssl", shell=True)
			print "Stopping services so you can configure them properly"
			stopservicescherokee = call ("/etc/init.d/cherokee stop && /etc/init.d/mysql stop", shell=True)
		elif userdistro2[0] == "Ubuntu":
			installprocesscherokee2 = call ("apt-get install --assume-yes cherokee php5-fpm mysql-server mysql-client php5-mysql libcherokee-mod-mysql libcherokee-mod-libssl", shell=True)
			print "Stopping services so you can configure them properly"
			stopservicescherokee2 = call ("/etc/init.d/cherokee stop && /etc/init.d/mysql stop", shell=True)
		else:
			webserverdebian()
	else:
		print "Input is invalid, please retry!"
		webserverdebian()

def installcpdebian():

	print 'Do you want to install a control panel (Webmin and/or phpmyAdmin)?'
	prompt = ">"
	answer = raw_input(prompt)
	if answer == "No" or answer == "no":
		print "Alright then, exiting."
		raise SystemExit
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
		raise SystemExit
	else:
		installcpdebian()

	raise SystemExit

# Fedora
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
	elif answer == "Lighttpd" or answer == "lighttpd":
		print "lolwait"
	else:
		webserverfedora()
		

def installcpfedora():

	print 'Do you want to install a control panel (Webmin and/or phpmyAdmin)?'
	prompt = ">"
	answer = raw_input(prompt)
	if answer == "No" or answer == "no":
		print "Alright then, exiting."
		raise SystemExit
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
		getrepofile = call ("wget -O /etc/yum.repos.d/webmin.repo https://raw.github.com/staticsafe/useful-scripts/master/webmin.repo", shell=True)
		getkey = call("wget http://www.webmin.com/jcameron-key.asc && rpm --import jcameron-key.asc", shell=True)
		installwebmin = call("yum install -y webmin", shell=True)
	elif answerwebmin == "No" or answerwebmin == "no":
		print "Alright then, we are done here. Exiting."
		raise SystemExit
	else:
		installcpfedora()

	raise SystemExit

#Arch Linux

def webserverarch():
	print 'Choose a webserver to install, your choices are Apache, Lightttpd, nginx, or Cherokee'
	prompt = ">"
	answer = raw_input(prompt)
	if answer == "Apache" or answer == "apache":
		installprocessapache = call("pacman --noconfirm -S apache php php-apache mysql", shell=True)
		print "Stopping started LAMP services so you can configure them properly."
		stopservicesapache = call ("/etc/rc.d/apache2 stop && /etc/rc.d/mysql stop", shell=True)
		print "READ THIS WIKI PAGE TO CONFIGURE LAMP PROPERLY - https://wiki.archlinux.org/index.php/LAMP"
	elif answer == "Lighttpd" or answer == "lighttpd":
		installprocesslighttpd = call ("pacman --noconfirm -S lighttpd fcgi php php-cgi mysql", shell=True)
		print "Stopping started LAMP services so you can configure them properly."
		stopserviceslighttpd = call ("/etc/rc.d/lighttpd stop && /etc/rc.d/mysql stop", shell=True)
		print "READ THIS WIKI PAGE TO CONFIGURE LIGHTTPD PROPERLY - https://wiki.archlinux.org/index.php/Lighttpd"
	elif answer == "nginx" or answer == "Nginx":
		installprocessnginx = call ("pacman --noconfirm -S nginx php-fpm mysql", shell=True)
		print "Stopping services so you can configure them properly"
		stopservicesnginx = call ("/etc/rc.d/nginx stop && /etc/rc.d/mysql stop", shell=True)
		print "READ THIS WIKI PAGE TO CONFIGURE NGINX PROPERLY - https://wiki.archlinux.org/index.php/Nginx"
	elif answer == "Cherokee" or answer == "cherokee":
		installprocesscherokee = call ("pacman --noconfirm -S cherokee php-fpm mysql", shell=True)
		print "Stopping services so you can configure them properly"
		stopservicescherokee = call ("/etc/rc.d/cherokee stop && /etc/rc.d/mysql stop", shell=True)
	else:
		print "Input is invalid, please retry!"
		webserverarch()

def installcparch():
	print 'Do you want to install a control panel (Webmin and/or phpmyAdmin)?'
	prompt = ">"
	answer = raw_input(prompt)
	if answer == "No" or answer == "no":
		print "Alright then, exiting."
		raise SystemExit
	elif answer == "Yes" or answer == "yes":
		print "Do you want to install phpmyAdmin?"
		promptpma = ">"
		answerpma = raw_input(promptpma)
	else:
		installcparch()
		
	if answerpma == "Yes" or answerpma == "yes":
		installcppma = call ("pacman --noconfirm -S phpmyadmin", shell=True)
	elif answerpma == "No" or answerpma == "no":
		print "Alright then!"
	else:
		installcparch()

	
	print "Do you want to install Webmin?"
	promptwebmin = ">"
	answerwebmin = raw_input(promptwebmin)
	if answerwebmin == "Yes" or answerwebmin == "yes":
		installwebmin = call("pacman --noconfirm -S webmin", shell=True)
	elif answerwebmin == "No" or answerwebmin == "no":
		print "Alright then, we are done here. Exiting."
		raise SystemExit
	else:
		installcparch()

	raise SystemExit

def main():
	#rootcheck
	uid = os.getuid()
	if uid != 0:
		print 'This script must be run as root or sudo if you have it!'
		raise SystemExit
	#distrocheck
	userdistro = platform.linux_distribution()

	if userdistro[0] == "Fedora":
		webserverfedora()
		installcpfedora()
	elif userdistro[0] == "debian":
		webserverdebian()
		installcpdebian()
	elif userdistro[0] == "Arch" or os.path.isfile("/etc/arch-release") == True:
		webserverarch()
		installcparch()
	elif userdistro[0] == "Ubuntu":
		webserverdebian()
		installcpdebian()
	else:
		print "This script is not supported for your distro, exiting."
		raise SystemExit

if __name__ == "__main__":
	main()





