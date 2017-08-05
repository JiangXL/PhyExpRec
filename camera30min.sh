
videoname=`date '+%s%F'`
echo ">-----------------------------------"


ffmpeg -t 1800 -f v4l2 -framerate 25 -i /dev/video0 /home/pi/Desktop/Video/$videoname.avi
