#!/usr/bin/env perl

# Originally written by cafejunkie, modified by staticsafe

my @RULES = ( );

if ( -e "./access.list" ) {
    open( LIST, "< ./access.list" );
}
else {
    die "access.list does not exist, terminating.\n"
}

while( <LIST> ){
        next if $_ =~ /^\#/ || $_ =~ /^$/;
        push( @RULES, $_ );
}

close( LIST );


if ( scalar( @ARGV ) <= 0 ) {
        system("iptables -L -n");
}
else {
        if ( $ARGV[0] eq "--enable" ) {
                foreach ( @RULES ) {
                        my $cmd = "iptables -A " . $_;
                        system( $cmd );
                }
        }
        elsif ( $ARGV[0] eq "--disable" ) {
                my $cmd = "iptables -F";
                system( $cmd );
        }
        system("iptables -L -n");
}

exit;
