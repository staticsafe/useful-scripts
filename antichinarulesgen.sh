#!/usr/bin/env bash
# Name : antichinarulesgen.sh
# Purpose : Generates a nice little anti-China rules list that can be used with cafejunkie's block_china.pl

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
sed -e '1,4d;s/China//;s/^/INPUT -s /;s/^\(.*\) .*/`\1/;s/$/-p tcp -j DROP/' ./chinacidr.txt > access.list

# add some rules for psad, you may omit this if you don't need it
#printf '%s\n' 'INPUT -j LOG' >> access.list
#printf '%s\n' 'FORWARD -j LOG' >> access.list
