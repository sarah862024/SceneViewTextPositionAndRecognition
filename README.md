# Scene View Text Position And Recognition
Taiwan Scene View Text Position and Recognition

* 目錄
  * 訓練資料前處理
    * 取得中文字元文字檔(ChineseCharList.txt)
    * 擷取出資料集所有影像中的文字區塊
  *  擴增資料處理
    * 
  * 訓練文字辨識模型
  * 執行文字定位及辨識
  * 辨識結果篩選
  * 參考來源

## 訓練資料前處理
### 取得中文字元文字檔(ChineseCharList.txt)  
根據全部json檔案中的Label值取得不重複的所有中文字元  
```python
python ./toolCode/getLabelCharFromJson.py
```
如果有兩個中文字元文字檔可使用`combine2CharTxt.py`將它們合併
```python
python ./toolCode/combine2CharTxt.py
```
### 擷取出資料集所有影像中的文字區塊
根據全部json檔案中的資訊，將全部影像中的文字區塊擷取另存成jpg檔(`Line46,47,76,78`取消註解可以同時輸出GT.txt)
```python
python ./toolCode/convertJsonToTxtAndGetCropImage.py
```
## 擴增資料處理


## 訓練文字辨識模型


## 執行文字定位及辨識


## 辨識結果篩選


## 參考來源
