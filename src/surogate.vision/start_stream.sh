mkdir ~/video
mkdir ~/video/streams

cd ~/bin/cd mjpg-streamer/mjpg-streamer-experimental
raspistill -w 640 -h 480 -q 5 -o ~/video/streams/pic.jpg -tl 100 -t 9999999 -th 0:0:0 &