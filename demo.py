#import cv2
#import numpy as np
#image=cv2.imread('blue.jpg',1)
#cv2.imshow('original',image)
#cap=cv2.VideoCapture(0)
#while(1):
   # _,frame=cap.read()
   # new_image=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #cv2.imshow('image',new_image)
    #lower_bound=np.array([110,50,50])
    #upper_bound=np.array([130,252,252])
    #mask=cv2.inRange(new_image,lower_bound,upper_bound)
    #cv2.imshow('mask',mask)
    #blue=np.uint8([[[255,0,0]]])
    #rest=cv2.bitwise_and(frame,frame,mask,mask)
    #cv2.imshow('rest',rest)
    #hsv_blue=cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
    #print(hsv_blue)
    #k=cv2.waitKey(5)&0xFF
    #if k==27:
       # break
        #def draw_circle(event,x,y,flag,param):
  #  if event==cv2.EVENT_LBUTTONDBLCLK:
       # cv2.circle(image, (x, y), 100, (255, 0, 0), -1)
#image=cv2.imread('god.jpg',1)
#cv2.namedWindow("image")
#cv2.setMouseCallback('image',draw_circle)
#while(1):
    #cv2.imshow('image',image)
    #if cv2.waitKey(10000)&0xFF==27:
     # break
#image=cv2.imread('god.jpg',1)
#cv2.line(image,(0,0),(400,400),(255,0,0),5)
#cv2.rectangle(image,(0,0),(400,400),(0,255,0),3)
#cv2.circle(image,(200,200),100,(0,0,255),-1)
#font=cv2.FONT_HERSHEY_COMPLEX
#cv2.putText(image,"hello",(100,100),font,4,(255,255,255),cv2.LINE_AA)
#cv2.imshow('shapes',image)
#cv2.waitKey(10000)
#cv2.imwrite('god.png',image)
import cv2
import numpy as np
image=cv2.imread("train.jpeg",1)
#matrix=np.ones((5,5),np.float32)/25
blur=cv2.blur(image,(5,5))
gaussian_blur=cv2.GaussianBlur(image,(5,5),0)
cv2.imshow('gaussian',gaussian_blur)
#new_image=cv2.filter2D(image,-1,matrix)
cv2.imshow("image",image)
#cv2.imshow("newimage",new_image)
cv2.imshow("blur",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
