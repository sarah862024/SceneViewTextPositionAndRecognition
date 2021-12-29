import numpy
import os

# typeString分別更改成training, test, validation執行三次程式得到各自的GT
typeString = 'training'

folderPath = './trainingDataset/' + typeString + '/'

# ground truth文字檔輸出位置
outputTxtPath = './trainingDataset/' + typeString + '_GT.txt'
txtFile = open(outputTxtPath, 'w', encoding = 'utf8')

outputTxtList = []
allFileList = os.listdir(folderPath)
for imageName in allFileList:
    imageGt = imageName.split('_')[0]
    outputTxtList.append(typeString + '/' + imageName + '\t' + imageGt + '\n')

txtFile.writelines(outputTxtList)
txtFile.close()