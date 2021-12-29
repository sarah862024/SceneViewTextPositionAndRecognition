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

##### 重新排序資料，編號從低到高 #####
wordCharResultFile = open('./demoResult_WordChar_filter.txt', 'r', encoding = 'utf8')
wordCharResultString = wordCharResultFile.read()
wordCharResultList = wordCharResultString.split('\n')

sortFilterFile = open('./demoResult_WordChar_filter_sorted.txt', 'w', encoding = 'utf8')
sortFilterList = []

for index in range(0, len(wordCharResultList)):        
    if wordCharResultList[index] == '': # 略過空字串
        continue

    chInfoList = wordCharResultList[index].split(',')

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

    chInfoList.append(chInfoList[0].split('_')[1])
    sortFilterList.append(chInfoList)

sortFilterList.sort(key = lambda s:s[3])

outputStringList = []
for item in sortFilterList:
    outputStringList.append(item[0] + ',' + item[1] + ',' + item[2] + '\n')

sortFilterFile.writelines(outputStringList)

wordCharResultFile.close()
sortFilterFile.close()