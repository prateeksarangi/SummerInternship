#!/bin/sh
echo "Executing the program..."

echo "Path of the image:- "
read path

echo "====================================================================================="
echo "Installing virtual environment..."
sudo apt-get install python3-pip
alias pip='pip3'
pip install virtualenv

echo "====================================================================================="
echo "Activating virtual environment..."
virtualenv env
source env/bin/activate

echo "====================================================================================="
echo "Installing required packages..."
pip install -r requirements.txt
alias python=python3

echo "====================================================================================="
echo "Running the program..."
python ObjectDetection.py -i "$path"

echo "====================================================================================="
echo "Obtaining informatioin..."
python ReadData.py