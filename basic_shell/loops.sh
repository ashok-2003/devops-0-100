#so this is the while loop in the shell script
x=2
while [ $x -lt 12 ]
do
	echo $x 
	x=`expr $x + 1`
done
# so this is how the while loop executed in the sh file 
echo "while loop is tested above"
# testing the for over the variable here 
for var in 2 4 6 8 11 152 "string"
do
	echo $var
done

echo "for loop is tested"

