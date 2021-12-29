from os import listdir
from os.path import isfile
import os

folderPath = "./augment"
files = listdir(folderPath)

imageCnt = 0 # 影像開始序號

outputTxtList = []
for f in files:
    if isfile:
        inputImgName = f
        f = f.replace(" ","")
        f = f.split("_")[0]
        outputImgName = f + "_" + str(imageCnt) + ".jpg"
        imageCnt += 1
        print(outputImgName)
        os.rename(folderPath + '\\' + inputImgName, folderPath + '\\' + outputImgName)
        outputTxtList.append(outputImgName + '\t' + f + '\n')
