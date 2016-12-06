from time import sleep
import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from alertnoise import sendAlert
from cameraCode import initRecvideo, stopVideo, recVideo
import os

#initRecvideo()

# initialize sesnor and leds
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN )
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
sleep(1)
isTrig = False

def trig():
    print "LED on"
    GPIO.output(18,GPIO.HIGH)
    time.sleep(1)
    print "LED off"
    GPIO.output(18,GPIO.LOW)
    time.sleep(1)

print("Telematics~ running ...");
while True:
        GPIO.output(18,GPIO.HIGH)

        if isTrig == True:
            trig();
            #stopVideo()
            
        result = GPIO.input(5)
        if result == 1:
            print("Vibrated\n********************************\nRecording Video")
            isTrig =True
            vidName = time.strftime("%d%m%Y")+time.strftime("%I%M%S")
            recVideo(vidName)
 	    sleep(1)
 	    hname = vidName+"video.h264"
 	    mname = vidName+"video.mp4"
 	    print("Converting video file h264 to MP4");
 	    commands = "sudo MP4Box -add" + " "+hname + " " +mname
 	    os.system(commands)
            print("Sending video file to email");
 	    sendAlert(vidName)
 	    print("File sent");

