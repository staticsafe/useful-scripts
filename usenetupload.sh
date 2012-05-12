#!/usr/bin/env bash
# Written by staticsafe
# Needed sofware - par2, rar, newspost
# RAR Linux binary can be obtained from here - http://www.rarlab.com/download.htm
# newspost source can be found here - https://github.com/PietjeBell88/newspost (needs to be compiled)

# Some variables

rarbinary=""
newspostbinary=""
uploaddir="$HOME/uploads"

# vars needed for newspost
username=""
password=""
server=""
newsgroup=""
poster=""
email=""
subject=""

# Do the stuff

$rarbinary a "$uploaddir/{$0}" -v10m -m0 $0
par2create -r10 -n7 $0 $uploaddir/*.rar*
$newspostbinary -i $server -u $username -p $password -f $email -n $newsgroup -y -s $subject "$uploaddir/*.part*" "$uploaddir/*.par*"


