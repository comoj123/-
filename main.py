import os
import configparser
from cam_on import CAM_ON

from ocr import ocrToStr

img_path = os.path.dirname(os.path.realpath(__file__))+os.sep+'resource'+os.sep +'image'  #이미지 저장 경로
config = configparser.ConfigParser() #Config Parser 초기화
config.read(os.path.dirname(os.path.realpath(__file__))+os.sep + 'envs' + os.sep + 'property.ini') #Config File 읽기 (Tesseract 실행시 참고하는

if __name__ == "__main__":
    outTxtPath = os.path.dirname(os.path.realpath(__file__)) + config['Path']['OcrTxtPath']
    #CAM_ON()

    #OCR
    for root, dirs, files in os.walk(os.path.dirname(os.path.realpath(__file__)) + config['Path']['OriImgPath']):
        for fname in files:
            fullName = os.path.join(root, fname)
            ocrToStr(fullName, fname,'eng')
