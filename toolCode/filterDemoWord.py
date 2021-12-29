import numpy
import csv

# 如果字串中有非中文或字串為空字串則回傳False
def isOnlyChinese(check_str):
    for ch in check_str:
        if ch < '\u4e00' or ch > '\u9fff':
            return False
    if check_str == '':
        return False
    return True

wordResultFile = open('./demoResult_Word.txt', 'r', encoding = 'utf8')
wordResultString = wordResultFile.read()
wordResultList = wordResultString.split('\n')

wordFilterFile = open('./demoResult_Word_filter.txt', 'w', encoding = 'utf8')
wordFilterList = []

for index in range(0, len(wordResultList)):        
    if wordResultList[index] == '': # 略過空字串
        continue

    chInfoList = wordResultList[index].split(',')

    # 將label中有','的項目重新組合成正確的List
    if len(chInfoList) > 3:
        tmpName = chInfoList[0]
        tmpScore = chInfoList[-1]
        tmpLabel = ''
        for tmpIndex in range(1, len(chInfoList)-1):
            tmpLabel += chInfoList[tmpIndex]
            tmpLabel += ','
        chInfoList = []
        chInfoList.append(tmpName)
        chInfoList.append(tmpLabel[0:-1])
        chInfoList.append(tmpScore)

    if isOnlyChinese(chInfoList[1]) and len(chInfoList[1]) <= 1: # 過濾純中文且只有一個字的項目
        continue
    
    wordFilterList.append(chInfoList[0] + ',' + chInfoList[1] + ',' + chInfoList[2] + '\n')

wordFilterFile.writelines(wordFilterList)
    
wordResultFile.close()
wordFilterFile.close()