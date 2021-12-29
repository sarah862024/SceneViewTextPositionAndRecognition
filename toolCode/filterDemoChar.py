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

charResultFile = open('./demoResult_Char.txt', 'r', encoding = 'utf8')
charResultString = charResultFile.read()
charResultList = charResultString.split('\n')

charFilterFile = open('./demoResult_Char_filter.txt', 'w', encoding = 'utf8')
charFilterList = []

for index in range(0, len(charResultList)):        
    if charResultList[index] == '': # 略過空字串
        continue

    chInfoList = charResultList[index].split(',')

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

    # 刪除符號部分
    NoSymbolLabel = chInfoList[1].replace('!','')
    NoSymbolLabel = NoSymbolLabel.replace('"','')
    NoSymbolLabel = NoSymbolLabel.replace('#','')
    NoSymbolLabel = NoSymbolLabel.replace('$','')
    NoSymbolLabel = NoSymbolLabel.replace('%','')
    NoSymbolLabel = NoSymbolLabel.replace('&','')
    NoSymbolLabel = NoSymbolLabel.replace('(','')
    NoSymbolLabel = NoSymbolLabel.replace(')','')
    NoSymbolLabel = NoSymbolLabel.replace('*','')
    NoSymbolLabel = NoSymbolLabel.replace('+','')
    NoSymbolLabel = NoSymbolLabel.replace(',','')
    NoSymbolLabel = NoSymbolLabel.replace('-','')
    NoSymbolLabel = NoSymbolLabel.replace('.','')
    NoSymbolLabel = NoSymbolLabel.replace('/','')
    NoSymbolLabel = NoSymbolLabel.replace(':','')
    NoSymbolLabel = NoSymbolLabel.replace(';','')
    NoSymbolLabel = NoSymbolLabel.replace('<','')
    NoSymbolLabel = NoSymbolLabel.replace('>','')
    NoSymbolLabel = NoSymbolLabel.replace('=','')
    NoSymbolLabel = NoSymbolLabel.replace('?','')
    NoSymbolLabel = NoSymbolLabel.replace('@','')
    NoSymbolLabel = NoSymbolLabel.replace('[','')
    NoSymbolLabel = NoSymbolLabel.replace(']','')
    NoSymbolLabel = NoSymbolLabel.replace('^','')
    NoSymbolLabel = NoSymbolLabel.replace('_','')
    NoSymbolLabel = NoSymbolLabel.replace('`','')
    NoSymbolLabel = NoSymbolLabel.replace('{','')
    NoSymbolLabel = NoSymbolLabel.replace('}','')
    NoSymbolLabel = NoSymbolLabel.replace('|','')
    NoSymbolLabel = NoSymbolLabel.replace('~','')

    if NoSymbolLabel.encode('utf-8').isalnum(): # 過濾英文及數字
        continue
    
    charFilterList.append(chInfoList[0] + ',' + chInfoList[1] + ',' + chInfoList[2] + '\n')

charFilterFile.writelines(charFilterList)
    
charResultFile.close()
charFilterFile.close()