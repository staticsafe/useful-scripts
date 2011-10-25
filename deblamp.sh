#!/bin/bash
#Sets up LAMP on a Debian based server

#Update repos and check for any update

sudo apt-get update
sudo apt-get upgrade

#Install LAMP packages

printf '%s\n' 'Installing LAMP packages now'

sudo apt-get install mysql-server mysql-client apache2 apache2-doc php5 php5-mysql libapache2-mod-php5

printf '%s\n' 'Stopping started LAMP services so you can configure them properly.'

sudo /etc/init.d/mysql stop
sudo /etc/init.d/apache2 stop

printf '%s\n' 'All LAMP packages have been now installed. Look in /etc/apache2 for apache\'s config files.'

#Optional Packages

#printf '%s\n' 'You probably want phpmyadmin to manage your DBs from the web browser'

#sudo apt-get install phpmyadmin