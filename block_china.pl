#!/usr/bin/perl -w

# Originally written by cafejunkie, modified by staticsafe

my @RULES = ( );

open( LIST, "< ./access.list" );

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
