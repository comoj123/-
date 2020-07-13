import cv2
import numpy as np
from matplotlib import pyplot as plt

class compareImg:
    def __init__(self):
        pass

    def readImg(self, filepath):
        img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
        # cv2.namedWindow("root", cv2.WINDOW_NORMAL)# window 생성
        # cv2.imshow("root", img)# window에 이미지 띄우기
        # cv2.waitKey(5000)  #5초 기다림. 아무키나 입력되면 대기 종료
        # cv2.destroyAllWindows()  # window 제거
        return img


    def diffImg(self, img1, img2):
        # 지속 SIFT 검출
        orb = cv2.ORB_create()

        # SIFT로 핵심 포인트 및 설명자 찾기
        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)

        #BFMatcher 객체 생성
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        #
        matches = bf.match(des1, des2)

        #
        matches = sorted(matches, key=lambda x: x.distance)

        #
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1, des2, k=2)

        #
        good = []
        for m, n in matches:
            if m.distance < 0.1 * n.distance:
                good.append([m])

        #
        knn_image = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
        plt.imshow(knn_image)
        plt.show()

    def run(self):
        # 이미지 파일 경로 설정
        filepath1 = r"C:\Users\co_mo\PycharmProjects\dicturepen\opencvtest\test1.png"
        filepath2 = r"C:\Users\co_mo\PycharmProjects\dicturepen\opencvtest\test2.png"

        #
        img1 = self.readImg(filepath1)
        img2 = self.readImg(filepath2)

        #
        self.diffImg(img1, img2)


if __name__ == '__main__':
    cImg = compareImg()
    cImg.run()
