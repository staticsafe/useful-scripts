#!/bin/bash
# Name : antichinarulesgen.sh
# Purpose : Generates a nice little anti-China rules list that can be used with iptables-restore or cafejunkie's block_china.pl

# a die function as always
die() {
printf '%s\n' "$@" >&2
exit 1
}

# Get CIDR file with Chinese subnets
wget -O chinacidr.txt http://www.okean.com/chinacidr.txt || die 'failed to download cidr file, please try again later.'

# Check if there is an existing access.list file
if [[ -f ./access.list ]]; then
        mv ./access.list access.list.bak
else
        printf '%s\n' "access.list file doesn't exist, continuing."
fi

# sed operations
cat chinacidr.txt | sed -e '1,4d' | sed -e 's/China//' | sed -e 's/^/INPUT -s /' | sed -e 's/^\(.*\) .*/\1/' | sed -e 's/$/-p tcp -j DROP/' > access.list

# add some rules for psad, you may omit this if you don't need it
printf '%s\n' 'INPUT -j LOG' >> access.list
printf '%s\n' 'FORWARD -j LOG' >> access.list