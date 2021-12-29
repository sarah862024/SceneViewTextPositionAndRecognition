import numpy
import os

ChineseCharList_1Path = './ChineseCharList_1.txt'
ChineseCharList_2Path = './ChineseCharList_2.txt'

#結合兩個字元列表的文字檔位置
outputTxtPath = './ChineseCharList.txt'

ChineseCharList_1File = open(ChineseCharList_1Path, 'r', encoding = 'utf8')
ChineseCharList_2File = open(ChineseCharList_2Path, 'r', encoding = 'utf8')
outputTxtFile = open(outputTxtPath, 'w', encoding = 'utf8')

ChineseCharList_1String = ChineseCharList_1File.read()
ChineseCharList_2String = ChineseCharList_2File.read()
ChineseCharList_1List = ChineseCharList_1String.split('\n')
ChineseCharList_2List = ChineseCharList_2String.split('\n')

combineCharList = ChineseCharList_1List + ChineseCharList_2List
combineCharList = numpy.unique(combineCharList).tolist()

outputCharList = []
for char in combineCharList:
    if char == '':
        continue
    outputCharList.append(char + '\n')


outputTxtFile.writelines(outputCharList)

ChineseCharList_1File.close()
ChineseCharList_2File.close()
outputTxtFile.close()
