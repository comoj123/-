import cv2
import time
import os

cap = cv2.VideoCapture(1)
time.sleep(3)
if not cap.isOpened():
  exit()

##########모델 예측

name = 'apple'
count = 1
while True:
    ret, image = cap.read()
    #print(type(image)) #<class 'numpy.ndarray'>
    #print(image.shape) #(720, 1280, 3)

    if not ret:
        break

    if not os.path.isdir('fruit/{}'.format(name)):
        os.makedirs('fruit/{}'.format(name))

    cv2.imwrite('fruit/{}/{}.png'.format(name, count), image)
    count += 1
    time.sleep(1)

    if count == 100:
        break

    x1, y1 = 30, 30
    text = 'fruit/{}/{}.png'.format(name, count)
    cv2.putText(image, text=text, org=(x1, y1), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 255, 255), thickness=2)

    cv2.imshow('image', image)

    if cv2.waitKey(1) == ord('q'): #key 입력이 있을때까지 1밀리 세컨드 만큼 대기
        break

cap.release()
cv2.destroyAllWindows()