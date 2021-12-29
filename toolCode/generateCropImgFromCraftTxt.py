import numpy
import os
import cv2 

# 將圖片中的指定區塊存成圖片(正方形未處理背景)
def saveCropImage(pointList, image, outputImageName):
    pointArray = numpy.array(pointList)
    minX = min(pointArray[:,0])
    maxX = max(pointArray[:,0])
    minY = min(pointArray[:,1])
    maxY = max(pointArray[:,1])
    cropImage = image[minY:maxY, minX:maxX]
    cv2.imencode('.jpg', cropImage)[1].tofile('./positionCrop/' + outputImageName)

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
    cv2.imencode('.jpg', cropImage)[1].tofile('./positionCrop/' + outputImageName)

# 文字定位模型所輸出的座標點文字檔位置
CraftTxtPath = './CraftOutput.txt'
CraftTxtFile = open(CraftTxtPath, 'r', encoding = 'utf8')
CraftString = CraftTxtFile.read()
CraftList = CraftString.split('\n')

for boxInfo in CraftList:
    if boxInfo == '':
        continue
    boxList = boxInfo.split(',')
    image = cv2.imread('./demoImage/' + boxList[0] + '.jpg') # 處理的影像儲存位置
    height, width = image.shape[:2]

    # 將超過圖片範圍的座標修正至圖片範圍內
    for i in range(1, len(boxList)):
        if int(boxList[i]) < 0: # 座標為負值時，將值更改成0
            boxList[i] = '0'
        if i % 2 == 0 and int(boxList[i]) > height: # Y座標超過圖片高度時，將值更改成圖片高度
            boxList[i] = str(height)
        elif i % 2 == 1 and int(boxList[i]) > width: # X座標超過圖片寬度時，將值更改成圖片寬度
            boxList[i] = str(width)

    outputImageName = boxList[0] + '_' + boxList[1] + '_' + boxList[2] + '_' + boxList[3] + '_' + boxList[4] + '_' + boxList[5] + '_' + boxList[6] + '_' + boxList[7] + '_' + boxList[8] + '.jpg'
    pointList = [[int(boxList[1]), int(boxList[2])], [int(boxList[3]), int(boxList[4])], [int(boxList[5]), int(boxList[6])], [int(boxList[7]), int(boxList[8])]]

    # saveCropImage(pointList, image, outputImageName)
    saveCropImageWithBlackBackground(pointList, image, outputImageName)

CraftTxtFile.close()