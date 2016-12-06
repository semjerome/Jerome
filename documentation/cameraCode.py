from picamera import PiCamera

from time import sleep

camera = PiCamera()

def initRecvideo():
        # initialize camera
        camera = PiCamera()
        camera.start_preview()

def stopVideo():
        camera.stop_preview()

def recVideo( sNum ):
	dest = '/home/pi/Desktop/Final Presentation/'+str(sNum)+'video.h264'
	camera.start_preview()
	camera.start_recording(dest)
	sleep(20)
	camera.stop_recording()
	camera.stop_preview()
	return;

