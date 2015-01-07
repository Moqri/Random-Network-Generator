#!/usr/bin/perl
use 5.010;
use strict;
use warnings;
open (MYFILE, '>02 Random Networks.txt'); 
my $n=5;my $m;
my @precs;my @dirprecs; my @indprecs;	

for my $count(1..1000){
$m=int(rand($n*($n-1)/2))+1;
@precs=();@dirprecs=();@indprecs=();	
for (my $row=1;$row<=$n-1;$row++){
	for (my $col=$row+1;$col<=$n;$col++){
		my @prec=($row,$col);
		push(@precs,\@prec);
	}
}
finddir();
while (scalar@precs>$m){
	my $edge= int(rand(scalar@dirprecs));
	#print ("$edge;$dirprecs[$edge]->[0];$dirprecs[$edge]->[1]\n");
	delet(($dirprecs[$edge]->[0],$dirprecs[$edge]->[1]));
	finddir();
}
printgraph();
}

sub delet {
my @del=@_;	
my $index = 0;
$index++ until $precs[$index][0] eq $del[0] and $precs[$index][1] eq $del[1];
splice(@precs, $index, 1);
}
sub finddir{
@dirprecs=(); @indprecs=();	
foreach my $prec (@precs){
	my $type='dir';
#	say $prec->[0];
	foreach my $p1(@precs){
		if ($p1->[0]eq$prec->[0]){
			foreach my $p2(@precs){
				if ($p2->[0]eq$p1->[1] and $p2->[1]eq$prec->[1]){
					$type='ind';										
				}
			}
		}
	}
	if ($type eq'ind'){
		push(@indprecs,$prec);										
	}else{
		push(@dirprecs,$prec);		
	}										
}
}
sub printgraph{
my %s; my %t; 
for (my $Act=1;$Act<=$n;$Act++){
	$s{$Act} = 1;
	$t{$Act} = 1;
}

foreach my $prec (@dirprecs){

	if(exists($s{$prec->[1]})) { 
		delete $s{$prec->[1]};
	}
	if(exists($t{$prec->[0]})) { 
		delete $t{$prec->[0]};
	}
}


printf MYFILE "0-$_ " for (keys %s);

foreach(@dirprecs){
printf MYFILE "$_->[0]-$_->[1] ";
}
printf MYFILE "$_-6 " for (keys %t);
printf MYFILE "; $m";
printf MYFILE "\n";
}