import numpy
import csv
import shapely 
from shapely.errors import TopologicalError 
from shapely.geometry import Polygon,MultiPoint 

# 轉換資料型態至多邊形
def toPolygon(quadrilateral): 
    quadrilateral_array = numpy.array(quadrilateral).reshape(4, 2)  
    quadrilateral_polygon = Polygon(quadrilateral_array).convex_hull 
    return quadrilateral_array, quadrilateral_polygon 

# 計算IOU
def calculateIOU(actual_quadrilateral, predict_quadrilateral): 
    actual_quadrilateral_array, actual_quadrilateral_polygon = toPolygon(actual_quadrilateral) 
    predict_quadrilateral_array, predict_quadrilateral_polygon = toPolygon(predict_quadrilateral) 
    union_poly = numpy.concatenate((actual_quadrilateral_array, predict_quadrilateral_array)) 
    inter_status = actual_quadrilateral_polygon.intersects(predict_quadrilateral_polygon) 
    if inter_status: 
        try:  
            inter_area = actual_quadrilateral_polygon.intersection(predict_quadrilateral_polygon).area 
            union_area = MultiPoint(union_poly).convex_hull.area 
            if union_area == 0: 
                iou = 0 
            else: 
                iou = float(inter_area) / actual_quadrilateral_polygon.area 
        except shapely.errors.TopologicalError : 
            print('shapely.errors.TopologicalError occured, iou set to 0') 
            iou = 0 
    else: 
        iou = 0 
    return iou 

# 全中文或中文加數字才回傳True (不包含純數字)
def isOnlyChineseAndNumber(check_str):
    for ch in check_str:
        if ch < '\u4e00' or ch > '\u9fff':
            if not ch.isdigit():
                return False
    if check_str == '': # 過濾空字串
        return False
    if check_str.isdigit(): # 過濾純數字
        return False
    return True

# 寫入資料至CSV
def writeDataToCsv(writer, imageName, answer):
    pointList = imageName[:-4].split('_')
    addList = [pointList[0] + '_' + pointList[1], pointList[2], pointList[3], pointList[4], pointList[5], pointList[6], pointList[7], pointList[8], pointList[9], answer]
    writer.writerow(addList)

# 根據符合物件重新組合字串內容
def regroupString(recheckPointList, matchList):
    avgWidth = int(((recheckPointList[2] - recheckPointList[0]) + (recheckPointList[4] - recheckPointList[6]))/2)
    avgHeight = int(((recheckPointList[5] - recheckPointList[3]) + (recheckPointList[7] - recheckPointList[1]))/2)
    if avgHeight > avgWidth: # 縱向
        matchList.sort(key = lambda s:s[1])
    else:                    # 橫向
        matchList.sort(key = lambda s:s[0])
    resultLabel = ''
    for matchItem in matchList:
        if float(matchItem[9]) >= 0.6:
            resultLabel += matchItem[8]
    return resultLabel

# 針對信心值低的中文數字字串進行重新確認
def recheckChineseString(currentImageIdList, recheckStringList, writer):
    for recheckItem in recheckStringList:
        matchList = []
        recheckPointList = recheckItem[0][:-4].split('_') # 保留四個座標點位置資訊
        recheckPointList = list(map(int ,recheckPointList[2:])) # 將list中string轉換成int
        for currentItem in currentImageIdList:
            currentPointList = currentItem[0][:-4].split('_') # 保留四個座標點位置資訊
            currentPointList = list(map(int ,currentPointList[2:])) # 將list中string轉換成int            
            matchIOU = calculateIOU(currentPointList, recheckPointList)
            if matchIOU >= 0.9 and recheckItem[0] != currentItem[0]: # IOU達90%且非自身物件就判斷為符合物件
                matchList.append(currentPointList + currentItem[1:])
        newLabel = regroupString(recheckPointList, matchList)
        if len(newLabel) > 1:
            writeDataToCsv(writer, recheckItem[0], newLabel)

if __name__ == '__main__': 
    chResultFile = open('./demoResult.txt', 'r', encoding = 'utf8')
    chResultString = chResultFile.read()
    chResultList = chResultString.split('\n')

    currentImageIdList = []
    currentImageId = ''
    recheckStringList = []
    with open('resultCSV.csv', 'w', newline='', encoding='utf8') as csvFile:
        for index in range(0, len(chResultList)):
            if chResultList[index] == '': # 略過空字串
                continue

            chInfoList = chResultList[index].split(',')        
            writer = csv.writer(csvFile)

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

            # 將當前圖片的所有辨識結果存在List，並在切換下張圖片的時候進行字串的重新確認
            if chInfoList[0].split('_')[1] == currentImageId:
                currentImageIdList.append(chInfoList)
            else:
                recheckChineseString(currentImageIdList, recheckStringList, writer)
                currentImageId = chInfoList[0].split('_')[1]
                currentImageIdList = []
                currentImageIdList.append(chInfoList)
                recheckStringList = []

            Thresh = 0.6
            if float(chInfoList[2]) >= Thresh: # 過濾信心值太低的項目
                if not isOnlyChineseAndNumber(chInfoList[1]) and len(chInfoList[1]) <= 1: # 過濾非純中文且只有一個字的項目
                    continue
                writeDataToCsv(writer, chInfoList[0], chInfoList[1])
            else: # 對於信心值低的中文數字字串做重新確認
                if isOnlyChineseAndNumber(chInfoList[1]) and len(chInfoList[1]) >= 3:
                    recheckStringList.append(chInfoList)

        recheckChineseString(currentImageIdList, recheckStringList, writer)   # 最後一張圖片也要做確認   
        chResultFile.close()
        csvFile.close()