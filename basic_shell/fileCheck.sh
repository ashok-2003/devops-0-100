#so this is used to find the file that you want 
echo "enter the file name which you want to find:"

read file

if [ -e "$file" ]
then
	echo "file found : $file"
else
	echo "file not found: $file"
fi

