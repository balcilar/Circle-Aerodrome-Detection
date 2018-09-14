import numpy as np
import cv2

from skimage.measure import CircleModel, ransac
from skimage import feature




class ObjectFinder:
    
     def __init__(self):
         self.x=-1
         self.y=-1
         self.r=-1
         self.cnt=0        
            


     def estimateLocation(self,cimg):
         kernel = np.ones((25,25),np.float32)/(25*25)
         dst = cv2.filter2D(cimg,-1,kernel)
         a=dst.argmax()
         nrow=int(a/cimg.shape[1])
         ncol=a-cimg.shape[1]*(nrow)
         return nrow,ncol


     def process(self,img):

         border=int(self.r)+10

         
                   
         if self.x< 0 or self.y <0:
            frame = cv2.medianBlur(img,7) 
            b=np.array(frame[:,:,0],dtype=np.float)
            g=np.array(frame[:,:,1],dtype=np.float)
            r=np.array(frame[:,:,2],dtype=np.float)
            r=2*r-g-b
            cimg=r/r.max()
            yy,xx=self.estimateLocation(cimg[50:-50,50:-50])
            self.y=yy+50
            self.x=xx+50
            border=50

                    

         tmp = img[int(self.y)-border:int(self.y)+border,int(self.x)-border:int(self.x)+border,2]
         #tmp= cv2.resize(tmp,None,None,0.25,0.25)
         edges = feature.canny(tmp, sigma=3) 
         points = np.array(np.nonzero(edges)).T
         if points.shape[0]==0:
             self.y=-1
             self.x=-1
             return False

         model_robust, inliers = ransac(points, CircleModel, min_samples=3,residual_threshold=2, max_trials=10)
                 

         self.r=model_robust.params[2] 
         self.x+=model_robust.params[1]-border
         self.y+=model_robust.params[0]-border

         if self.x-self.r<10 or self.x+self.r>img.shape[1]-10 or self.y-self.r<10 or self.y+self.r>img.shape[0]-10 or self.r<10 or self.r>150 or np.isnan(self.x) or np.isnan(self.y) or np.isnan(self.r):
             self.y=-1
             self.x=-1
             return False

         return True