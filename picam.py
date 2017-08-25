import picamera,os,time
from time import sleep

var = 1
while var == 1 :
    camera = picamera.PiCamera()
    try:
        print()
        list = os.listdir("/home/pi/Desktop/Videos")
        list.sort()

        print(list)
        os.remove("/home/pi/Desktop/Videos/"+list[0])
        list1 = os.listdir("/home/pi/Desktop/Videos")
        print(list1)
        
        fileTime = str(time.time())
        fileName = "/home/pi/Desktop/Videos/"+fileTime+".h264"

        camera.resolution = (640, 480)
        camera.start_recording(fileName)
        camera.wait_recording(10)
        camera.stop_recording()
    finally:
        camera.close()
