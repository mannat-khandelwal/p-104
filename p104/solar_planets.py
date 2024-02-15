import cv2

img=cv2.imread("solar-system.jpg")
cv2.putText(img,"Sun",(100,100),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,0,255))
cv2.putText(img,"Mercury",(115,185),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Venus",(180,260),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Earth",(280,260),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Mars",(380,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Jupiter",(570,370),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Saturn",(710,280),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Uranus",(970,290),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Neptune",(1110,285),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.imwrite("solar-system.jpg",img)
cv2.imshow('output',img)
cv2.waitKey(0)


