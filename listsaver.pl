#!/usr/bin/env perl
# This irssi script saves the output of /LIST to a file of your choice.
# This prevents the spamming of your (status) window for large networks.

use strict;
use Irssi;
use Fcntl qw(:flock);
use vars qw($VERSION %IRSSI);

$VERSION = "0.1";
%IRSSI = (
	authors		=>	'staticsafe',
	name		=>	'listsaver',
	description	=>	'Saves the output of /LIST to a file of your choice'
	license		=>	'BSD License',
	changed		=>	'NA',
);

