apt-get update
apt-get upgrade

apt-get install python3-pip
pip3 install --upgrade setuptools

pip3 install RPI.GPIO

pip3 install adafruit-blinka

sudo pip3 install adafruit-circuitpython-pca9685
sudo pip3 install adafruit-circuitpython-servokit
sudo apt-get install libjpeg8-dev

sudo apt-get install cmake libjpeg8-dev -y
cd ~/
mkdir bin
cd bin
git clone https://github.com/jacksonliam/mjpg-streamer.git
cd mjpg-streamer/mjpg-streamer-experimental
make
sudo make install