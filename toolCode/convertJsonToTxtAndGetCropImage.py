import json
import numpy
import os
import cv2 
import string

# 將字串中的符號刪除
def removeSymbolInString(inputString):
    symbolList = list(string.printable[62:-6])
    resultString = ''
    for char in inputString:
        if char not in symbolList:
           resultString  = resultString + char
    return resultString

# 將圖片中的指定區塊存成圖片(正方形未處理背景)
def saveCropImage(pointList, image, outputImageName):
    pointArray = numpy.array(pointList)
    minX = min(pointArray[:,0])
    maxX = max(pointArray[:,0])
    minY = min(pointArray[:,1])
    maxY = max(pointArray[:,1])
    cropImage = image[minY:maxY, minX:maxX]
    cv2.imencode('.jpg', cropImage)[1].tofile('./outputDataset/image/' + outputImageName)

# 將圖片中的指定區塊存成圖片(將背景區塊填黑)
def saveCropImageWithBlackBackground(pointList, image, outputImageName):
    pointArray = numpy.array(pointList)
    mask = numpy.ones(image.shape, dtype=numpy.uint8)
    mask.fill(0)
    roiCorners = numpy.array([[(pointArray[0][0], pointArray[0][1]), (pointArray[1][0], pointArray[1][1]), (pointArray[2][0], pointArray[2][1]), (pointArray[3][0], pointArray[3][1])]], dtype=numpy.int32)
    cv2.fillPoly(mask, roiCorners, (255, 255, 255))
    maskedImage = cv2.bitwise_and(image, mask)
    minX = min(pointArray[:,0])
    maxX = max(pointArray[:,0])
    minY = min(pointArray[:,1])
    maxY = max(pointArray[:,1])
    cropImage = maskedImage[minY:maxY, minX:maxX]
    cv2.imencode('.jpg', cropImage)[1].tofile('./outputDataset/image/' + outputImageName)

# Dataset中json跟img的上一層
folderPath = './train/train/'
imageCnt = 0

#ground truth文字檔的輸出位置
# outputTxtPath = './outputDataset/GT.txt'
# txtFile = open(outputTxtPath, 'w', encoding = 'utf8')

allFileList = os.listdir(folderPath + 'json/')
for file in allFileList:
    outputTxtList = []
    jsonFile = open(folderPath + 'json/' + file, encoding = 'utf8')
    data = json.load(jsonFile)

    for i in data['shapes']:
        jsonLabelStr = i.get('label')
        jsonPointsList = i.get('points')
        
        if jsonLabelStr.find('###') != -1 or jsonLabelStr == '':
            continue

        outputNameStr = removeSymbolInString(jsonLabelStr)

        if outputNameStr == '':
            continue

        outputImageName = outputNameStr + '_' + str(imageCnt) + '.jpg'
        outputTxtList.append(outputImageName + '\t' + jsonLabelStr + '\n')
        imageName = file[0:-5] + '.jpg'
        image = cv2.imread(folderPath + 'img/' + imageName)

        # saveCropImage(jsonPointsList, image, outputImageName)
        saveCropImageWithBlackBackground(jsonPointsList, image, outputImageName)
        imageCnt += 1
    jsonFile.close()
    # txtFile.writelines(outputTxtList)

# txtFile.close()





