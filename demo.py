import numpy as np
import cv2
import time
import sys
from ObjectFinder import ObjectFinder

       


if __name__ == '__main__':  
    
    o=ObjectFinder()
    
    videofile='Input/video1.mp4'

    if len(sys.argv)>1:
        videofile=str(sys.argv[1])   

    cap = cv2.VideoCapture(videofile)
    ploc=None
    ptime=time.time()
    fno=0
    while(cap.isOpened()):
        fno+=1
        ret, frame = cap.read()
        if not ret:
            break
        
        status=o.process(frame)
        ctime=time.time()

        if status:
            
            cv2.circle(frame,(int(o.x),int(o.y)),int(o.r),(0,0,255),2)
            cv2.circle(frame,(int(o.x),int(o.y)),int(1),(255,0,0),2)            
            msg="x:" + str(o.x) +"  y:" +str(o.y) +"   r:" + str(o.r)
            cv2.putText(frame,msg, (10,300),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
            ploc=[o.x, o.y]
        else:
            ploc=None
            cv2.putText(frame,"None", (10,300),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1) 
            

        fname=str(fno)+".jpg"
        #cv2.imwrite(fname,frame)
        cv2.imshow('detected circles',frame)
        
        cv2.waitKey(10)

    cap.release()
               