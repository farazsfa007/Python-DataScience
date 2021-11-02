import cv2

img=cv2.imread('../coin.jpg')

# print(img)
# print(img.ndim)
# print(img.shape)

# cv2.imshow('using opencv',img)
# cv2.waitKey(10000)

cap = cv2.VideoCapture(0)

while True:

    ret,frame=cap.read()
    cv2.imshow('using webcam',frame)

    if cv2.waitKey(10) & 0xFF == ord ('q'):
        break

cv2.destroyAllWindows()
cap.releace()