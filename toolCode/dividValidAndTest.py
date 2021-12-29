import random
import shutil
import os

#所有用於訓練的影像先存放於training資料夾內
folderPath = './trainingDataset/training/' # training資料夾位置

def moveFile2valid(imageName):
    oldPath = folderPath + imageName
    newPath = './trainingDataset/validation/' + imageName # validation資料夾位置
    shutil.move(oldPath, newPath)

def moveFile2test(imageName):
    oldPath = folderPath + imageName
    newPath = './trainingDataset/test/' + imageName # test資料夾位置
    shutil.move(oldPath, newPath)

imageIdStart = 0              # 影像起始編號
imageIdEnd = 321598           # 影像結束編號
generateRandomNumCnt = 64318  # valid+test的數量

randomNumList = random.sample(range(imageIdStart, imageIdEnd), generateRandomNumCnt)

validNumList = randomNumList[0:len(randomNumList)//2]
testNumList = randomNumList[len(randomNumList)//2:]

allFileList = os.listdir(folderPath)
for fileName in allFileList:
    nameAfterbaseline = fileName.split('_')[1]
    imageId = nameAfterbaseline.split('.')[0]

    if int(imageId) in validNumList:
        moveFile2valid(fileName)
    elif int(imageId) in testNumList:
        moveFile2test(fileName)