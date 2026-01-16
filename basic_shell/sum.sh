#this will give the sum of n number from 1 
echo "enter the number:"
read N
for((i=1;i<=$N;i++));
do
	sum=$((sum+i))
done
echo "sum of $N number is: $sum"

