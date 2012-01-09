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

# USAGE: /listsaver [<server>]
sub cmd_listsaver {
	my ($data, $server, $witem) = @_;
	my $filename = $ENV{HOME} . '/.irssi/channel_list';
	#if (!$server || !$server->{connected}) {
	#	Irssi::print("Not connected to server");
	#	return;
	#}

	$server->redirect_event("list", 1, $data, -1, undef, {"event 322" => "redir list", "" => "event empty"});
	$server->send_raw("LIST" :$data)
}
Irssi::command_bind('listsaver', 'cmd_listsaver');