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

#Update repos and check for any update(s)

sudo apt-get update
sudo apt-get upgrade

#Choose webserver
printf '%s\n' 'Choose a webserver to install, your choices are Apache, Lightttpd, nginx, Cherokee'
read webserver

#Install webserver packages
#Needs to be more user-friendly, add links to docs etc.

if [[ "$webserver" ==  "Apache" || "$webserver" == "apache" ]]; then
	printf '%s\n' 'Installing LAMP packages now'
	sudo apt-get install mysql-server mysql-client apache2 apache2-doc php5 php5-mysql libapache2-mod-php5
	printf '%s\n' 'Stopping started LAMP services so you can configure them properly.'
	sudo /etc/init.d/mysql stop
	sudo /etc/init.d/apache2 stop
	printf '%s\n' 'Done! :)'
elif [["$webserver" == "nginx" || "$webserver" == "Nginx" ]]; then
	printf '%s\n' 'Installing nginx based webserver now'
	sudo apt-get install nginx php5-cli php5-cgi spawn-fcgi mysql-server mysql-client php5-mysql
	printf '%s\n' 'Stopping started services so you can configure them properly.'
	sudo /etc/init.d/mysql stop
	sudo /etc/init.d/nginx stop
	printf '%s\n' 'Look at http://goo.gl/tQBe7 for instructions on how to configure php-fastcgi'
	printf '%s\n' 'Done! :)'
elif [["$webserver" == "Lighttpd" || "$webserver" == "lighttpd" ]]; then
	printf '%s\n' 'Installing lighttpd based webserver now'
	sudo apt-get install lighttpd mysql-server mysql-client php5-mysql
	printf '%s\n' 'Stopping started services so you can configure them properly.'
	sudo /etc/init.d/mysql stop
	sudo /etc/init.d/nginx stop
	printf '%s\n' 'Look at http://goo.gl/i4NlE for instructions on how to configure lighttpd.'
	printf '%s\n' 'Done! :)'
elif [["$webserver" == "cherokee" || "$webserver" == "Cherokee" ]]; then
	printf '%s\n' 'Installing Cherokee based webserver now'
	sudo apt-get install cherokee mysql-server mysql-client php5-mysql openssl
	printf '%s\n' 'Done! :)'
else
	die 'Input webserver properly! Exiting now!'
fi

#Control Panels

printf '%s\n' 'Do you want to install a control panel (Webmin and/or phpmyAdmin)? (Yes/No)'
read cpinput

if [["$cpinput" == "No" || "$cpinput" == "no"]]; then
	printf '%s\n' 'Alright then! Exiting'
	exit
elif [["$cpinput" == "Yes" || "$cpinput" == "Yes"]]; then
	#PMA part
	printf '%s\n' 'Do you want to install phpmyAdmin? (Yes/No)'
	read cppma
	if [["$cppma" == "No" || "$cppma" == "no"]]; then
		printf '%s\n' 'Alright, not installing phpmyAdmin.'
	elif [["$cppma" == "Yes" || "$cppma" == "yes"]]; then
		printf '%s\n' 'Installing phpmyAdmin!'
		sudo apt-get install phpmyadmin
	fi
	#Webmin part
	printf '%s\n' 'Do you want to install Webmin? (Yes/No)'
	read cpwebmin
	if [["$cpwebmin" == "No" || "$cpwebmin" == "no"]]; then
		printf '%s\n' 'Alright, not installing Webmin, exiting'
		exit
	elif [["$cpwebmin" == "Yes" || "$cpwebmin" == "yes"]]; then
		printf '%s\n' 'Installing Webmin!'
		wget http://www.webmin.com/jcameron-key.asc
		sudo apt-key add jcameron-key.asc
		printf '%s\n' 'Adding Webmin APT repo to sources.list'
		cp /etc/apt/sources.list $HOME/sources.list
		sudo chmod 777 $HOME/sources.list
		echo 'deb http://download.webmin.com/download/repository sarge contrib' >> $HOME/sources.list
		sudo mv $HOME/sources.list /etc/apt/sources.list
		sudo chmod 644 /etc/apt/sources.list
		sudo chown root:root /etc/apt/sources.list
		sudo apt-get update
		sudo apt-get install webmin
		sudo -k
		# I realize this can be done in a better way, but meh I'll improve it later.
	else
		die 'Invalid input! Exiting now!'
	fi
else
	die 'Invalid input! Exiting now!'
fi

