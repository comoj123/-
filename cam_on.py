import cv2
import os
import configparser

###설정값 관리
#img_path = 실행디렉토리/resource/image
img_path = os.path.dirname(os.path.realpath(__file__))+os.sep+'resource'+os.sep +'image'  #이미지 저장 경로
config = configparser.ConfigParser() #Config Parser 초기화
config.read(os.path.dirname(os.path.realpath(__file__))+os.sep + 'envs' + os.sep + 'property.ini') #Config File

def CAM_ON() :
    cam = cv2.VideoCapture(1)  # 카메라 연결
    cv2.namedWindow("Dicture pen")
    while (True):
        ret, frame = cam.read()
        cv2.imshow('Dicture pen', frame)
        if not ret:
            break
        k = cv2.waitKey(1)
        if k % 256 == 27:
            print("카메라를 끕니다")
            break
        if k % 256 == 32:
            cv2.imwrite(os.path.join(img_path, 'image.jpg'),frame)

            img_file = img_path + os.sep + 'image.jpg'
            src = cv2.imread(img_file, cv2.IMREAD_COLOR)  # 이미지 소스
            gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  # 그레이스케일

            # cv2.adaptiveThreshold(img, value, adaptivemethod, thresholdType, blocksize, C)
            threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

            cv2.imwrite(os.path.join(img_path, 'image.jpg'), threshold)  # 덮어쓰기
            print("캡쳐")
