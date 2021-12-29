import json
import numpy
import os

def isOnlyChinese(checkStr):
    for ch in checkStr:
        if ch < '\u4e00' or ch > '\u9fff':
            return False
    return True

folderPath = '存放所有json檔案的資料夾路徑，例如:./train/train/json/'
wordList = []

allFileList = os.listdir(folderPath)
for file in allFileList:
    print(file)
    jsonFile = open(folderPath + '/' + file, encoding = 'utf8')
    data = json.load(jsonFile)

    for i in data['shapes']:
        tmpStr = i.get('label')
        tmpList = list(tmpStr)
        for word in tmpList:
            if not isOnlyChinese(word):
                continue
            wordList.append(word + "\n")

    wordList = numpy.unique(wordList).tolist()
    jsonFile.close()
    wordList = numpy.unique(wordList).tolist()

outputTxtPath = 'ChineseCharList.txt'
txtFile = open(outputTxtPath, 'w', encoding = 'utf8')
txtFile.writelines(wordList)
txtFile.close()
