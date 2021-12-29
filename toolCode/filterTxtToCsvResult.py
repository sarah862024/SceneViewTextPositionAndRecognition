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

# 將資料寫入csv檔
def writeDataToCsv(writer, imageName, answer):
    pointList = imageName[:-4].split('_')
    addList = [pointList[0] + '_' + pointList[1], pointList[2], pointList[3], pointList[4], pointList[5], pointList[6], pointList[7], pointList[8], pointList[9], answer]
    writer.writerow(addList)

chResultFile = open('./demoResult.txt', 'r', encoding = 'utf8')
chResultString = chResultFile.read()
chResultList = chResultString.split('\n')

with open('resultCSV.csv', 'w', newline='', encoding='utf8') as csvFile:
    for index in range(0, len(chResultList)):        
        if chResultList[index] == '': # 略過空字串
            continue

        chInfoList = chResultList[index].split(',')        
        writer = csv.writer(csvFile)
        Thresh = 0.6

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

        if float(chInfoList[2]) >= Thresh: # 過濾信心值太低的項目
            if not isOnlyChinese(chInfoList[1]) and len(chInfoList[1]) <= 1: # 過濾非純中文且只有一個字的項目
                continue
            writeDataToCsv(writer, chInfoList[0], chInfoList[1])
            
    chResultFile.close()
    csvFile.close()
