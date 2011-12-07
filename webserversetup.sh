#!/bin/bash
#Sets up webserver on a Debian based server

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
elif [["$webserver" == "Lighttpd" || "$webserver" == "lighttpd" ]]; then
		printf '%s\n' 'Installing lighttpd based webserver now'
		sudo apt-get install lighttpd mysql-server mysql-client php5-mysql
		printf '%s\n' 'Stopping started services so you can configure them properly.'
		sudo /etc/init.d/mysql stop
		sudo /etc/init.d/nginx stop
		printf '%s\n' 'Look at http://goo.gl/i4NlE for instructions on how to configure lighttpd.'
elif [["$webserver" == "cherokee" || "$webserver" == "Cherokee" ]]; then
		printf '%s\n' 'Installing Cherokee based webserver now'
fi
