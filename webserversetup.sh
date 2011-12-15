#!/bin/bash
#Sets up webserver on a Debian based server

#Feature wishlist:
#Ask user if he/she wants to install mysql/php or not for a minimal install [Priority = High]
#Make a Fedora (yum) version [Priority = Low]


#a die function as always
die() {
printf '%s\n' "$@" >&2
exit 1
}

#Root check
if  [[ "$(/usr/bin/whoami)" != "root" ]]; then
	printf '%s\n' 'Run this script as root or using sudo if you have it!'
	die 'exiting'
fi

#Update repos and check for any update(s)

apt-get update
apt-get upgrade

#Install webserver packages
#Needs to be more user-friendly, add links to docs etc.

installwebserver() {
#Choose webserver
printf '%s\n' 'Choose a webserver to install, your choices are Apache, Lightttpd, nginx, Cherokee'
read webserver
if [[ "$webserver" ==  "Apache" || "$webserver" == "apache" ]]; then
	printf '%s\n' 'Installing LAMP packages now'
	apt-get install mysql-server mysql-client apache2 apache2-doc php5 php5-mysql libapache2-mod-php5
	printf '%s\n' 'Stopping started LAMP services so you can configure them properly.'
	/etc/init.d/mysql stop
	/etc/init.d/apache2 stop
	printf '%s\n' 'Done! :)'
elif [["$webserver" == "nginx" || "$webserver" == "Nginx" ]]; then
	printf '%s\n' 'Installing nginx based webserver now'
	apt-get install nginx php5-cli php5-cgi spawn-fcgi mysql-server mysql-client php5-mysql
	printf '%s\n' 'Stopping started services so you can configure them properly.'
	/etc/init.d/mysql stop
	/etc/init.d/nginx stop
	printf '%s\n' 'Look at http://goo.gl/tQBe7 for instructions on how to configure php-fastcgi'
	printf '%s\n' 'Done! :)'
elif [["$webserver" == "Lighttpd" || "$webserver" == "lighttpd" ]]; then
	printf '%s\n' 'Installing lighttpd based webserver now'
	apt-get install lighttpd mysql-server mysql-client php5-mysql
	printf '%s\n' 'Stopping started services so you can configure them properly.'
	/etc/init.d/mysql stop
	/etc/init.d/nginx stop
	printf '%s\n' 'Look at http://goo.gl/i4NlE for instructions on how to configure lighttpd.'
	printf '%s\n' 'Done! :)'
elif [["$webserver" == "cherokee" || "$webserver" == "Cherokee" ]]; then
	printf '%s\n' 'Installing Cherokee based webserver now'
	apt-get install cherokee mysql-server mysql-client php5-mysql openssl
	printf '%s\n' 'Done! :)'
else
	installwebserver
fi
}



#Control Panels

installcp(){
printf '%s\n' 'Do you want to install a control panel (Webmin and.or phpmyAdmin)?'
read cpinput

if [["$cpinput" == "No" || "$cpinput" == "no" ]]; then
	printf '%s\n' 'Alright then! Exiting'
	exit
elif [["$cpinput" == "Yes" || "$cpinput" == "Yes" ]]; then
	#PMA part
	printf '%s\n' 'Do you want to install phpmyAdmin?'
	read cppma
		if [["$cppma" == "No" || "$cppma" == "no"]]; then
			printf '%s\n' 'Alright, not installing phpmyAdmin.'
		elif [["$cppma" == "Yes" || "$cppma" == "yes" ]]; then
			printf '%s\n' 'Installing phpmyAdmin!'
			apt-get install phpmyadmin
		else
			installcp
		fi
	#Webmin part
	printf '%s\n' 'Do you want to install Webmin?'
	read cpwebmin
		if [["$cpwebmin" == "No" || "$cpwebmin" == "no" ]]; then
			printf '%s\n' 'Alright, not installing Webmin, exiting'
			exit
		elif [["$cpwebmin" == "Yes" || "$cpwebmin" == "yes" ]]; then
			printf '%s\n' 'Installing Webmin!'
			wget http://www.webmin.com/jcameron-key.asc
			apt-key add jcameron-key.asc
			printf '%s\n' 'Adding Webmin APT repo to sources.list'
			echo 'deb http://download.webmin.com/download/repository sarge contrib' >> /etc/apt/sources.list
			apt-get update
			apt-get install webmin
		else
			installcp
		fi
else
	installcp
fi
}

#Calling functions

installwebserver
installcp
