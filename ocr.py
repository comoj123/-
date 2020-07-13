from pytesseract import *
import os
import configparser
from PIL import Image
from crawling import get_dic_search


img_path = os.path.dirname(os.path.realpath(__file__)) + os.sep + 'resource' + os.sep + 'image'
config = configparser.ConfigParser()  # Config Parser 초기화
config.read(os.path.dirname(os.path.realpath(__file__)) + os.sep + 'envs' + os.sep + 'property.ini')

def ocrToStr(fullPath, fileName, lang='eng'):
    img = Image.open(fullPath)
    outText = image_to_string(img, lang=lang, config='--psm 1 -c preserve_interword_spaces=1')

    print('+++++++ OCR 결과 +++++++')
    print('추출한 파일 : ', fileName, '> : <<<-')
    print("단어 : " + outText)

    get_dic_search(outText)



