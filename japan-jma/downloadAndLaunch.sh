#!/bin/bash
mkdir output
filename='filelist1.txt'
n=1
while read line; do
# reading each line
echo "File $n : $line.zip"
wget https://www.data.jma.go.jp/svd/eqev/data/bulletin/data/hypo/"$line.zip"
unzip "$line.zip"
rm -rf "$line.zip"
echo "Starting Python parser"
python3 parser.py "$line" 0
echo "Finished Python parser"
rm -rf "$line"
n=$((n+1))
done < $filename
