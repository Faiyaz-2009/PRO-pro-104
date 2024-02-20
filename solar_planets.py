import cv2
img = cv2.imread("solar-system.jpg")


text = "SUN"
cv2.putText(img, text, (120,  122), cv2.FONT_HERSHEY_COMPLEX,  1.4, (0,  0,  255),  1)

text2 = "Neptune"
cv2.putText(img, text2, (1070,  127), cv2.FONT_HERSHEY_COMPLEX,  0.5, (255,  255,  255),  1)


text3 = "Uranus"
cv2.putText(img, text3, (920,  127), cv2.FONT_HERSHEY_COMPLEX,  0.5, (255,  255,  255),  1)



text4 = "Saturn"
cv2.putText(img, text4, (770,  127), cv2.FONT_HERSHEY_COMPLEX,  0.5, (255,  255,  255),  1)


text5 = "Jupiter"
cv2.putText(img, text5, (550,  70), cv2.FONT_HERSHEY_COMPLEX,  0.8, (255,  255,  255),  1)



text6 = "Mars"
cv2.putText(img, text6, (377,  257), cv2.FONT_HERSHEY_COMPLEX,  0.5, (255,  255,  255),  1)

text7 = "Earth"
cv2.putText(img, text7, (277,  257), cv2.FONT_HERSHEY_COMPLEX,  0.5, (255,  255,  255),  1)

text8 = "Venus"
cv2.putText(img, text8, (190,  257), cv2.FONT_HERSHEY_COMPLEX,  0.5, (255,  255,  255),  1)


text9 = "Mercury"
cv2.putText(img, text9, (107,  257), cv2.FONT_HERSHEY_COMPLEX,  0.5, (255,  255,  255),  1)




cv2.imshow("Output", img)
cv2.waitKey(0)
