# Scene View Text Position And Recognition
Taiwan Scene View Text Position and Recognition

* 目錄
  * 訓練資料前處理
    * 取得中文字元文字檔(ChineseCharList.txt)
    * 擷取出資料集所有影像中的文字區塊
    * 分割訓練集、驗證集、測試集
    * 生成Ground Truth
  * 擴增資料處理
    * 
  * 訓練文字辨識模型
    * 建立lmdb資料集
    * 訓練模型
  * 執行文字定位及辨識
    * 執行文字定位模型
    * 擷取出影像中的文字區塊儲存成影像
    * 執行文字辨識模型
  * 辨識結果篩選
    * 基本篩選
    * 基本篩選+字串文字重組
    * 
  * 參考來源

## 訓練資料前處理
### 取得中文字元文字檔`ChineseCharList.txt`  
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
### 分割訓練集、驗證集、測試集
先將所有用於訓練的影像存放於`trainingDataset/training`資料夾內，再依照分割比例分別將影像移至`trainingDataset/test`資料夾以及`trainingDataset/validation`資料夾內
```python
python ./toolCode/dividValidAndTest.py
```
### 生成Ground Truth
分別生成訓練集、驗證集、測試集的Ground Truth檔案，  
將`generateGT.py`中的變數`typeString`分別更改成`training`, `test`, `validation`共執行三次程式，  
總共會得到`training_GT.txt`, `test_GT.txt`, `validation_GT.txt`三個Ground Truth檔案
```python
python ./toolCode/generateGT.py
```
## 擴增資料處理


## 訓練文字辨識模型
### 建立lmdb資料集
分別建立訓練集、驗證集、測試集的lmdb資料集，  
建立訓練集的lmdb，並存放於`./data_lmdb_release/training/data/data_train/`
```python
python create_lmdb_dataset.py --inputPath ./trainingDataset/ --gtFile ./trainingDataset/training_GT.txt --outputPath ./data_lmdb_release/training/data/data_train/
```
建立驗證集的lmdb，並存放於`./data_lmdb_release/training/data/data_valid/`
```python
python create_lmdb_dataset.py --inputPath ./trainingDataset/ --gtFile ./trainingDataset/validation_GT.txt --outputPath ./data_lmdb_release/training/data/data_valid/
```
建立測試集的lmdb，並存放於`./data_lmdb_release/training/data/data_test/`
```python
python create_lmdb_dataset.py --inputPath ./trainingDataset/ --gtFile ./trainingDataset/test_GT.txt --outputPath ./data_lmdb_release/training/data/data_test/
```
### 訓練模型
準備好中文字元文字檔`ChineseCharList.txt`以及訓練集、驗證集、測試集的三組mdb檔案後，即可開始訓練
```python
python train.py --train_data data_lmdb_release/training/data/data_train --valid_data data_lmdb_release/training/data/data_valid --Transformation TPS --FeatureExtraction ResNet --SequenceModeling BiLSTM --Prediction Attn --data_filtering_off
```
## 執行文字定位及辨識
### 執行文字定位模型

### 擷取出影像中的文字區塊儲存成影像
根據文字定位模型所輸出的座標點文字檔`CraftOutput.txt`影像中的文字區塊擷取出來儲存成影像，且影像名稱命名為`原檔名_x1_y1_x2_y2_x3_y3_x4_y4.jpg`儲存至`positionCrop`資料夾內
```python
python ./toolCode/generateCropImgFromCraftTxt.py
```
### 執行文字辨識模型
依照`positionCrop`資料夾中的影像進行文字辨識，輸出結果文字檔`demoResult.txt`
```python
python demo.py --Transformation TPS --FeatureExtraction ResNet --SequenceModeling BiLSTM --Prediction Attn --image_folder ./positionCrop --saved_model ./saved_models/TPS-ResNet-BiLSTM-Attn-Seed1111/best_accuracy.pth
```
## 辨識結果篩選
篩選方式有兩種，選擇其中一種執行即可
### 基本篩選
僅過濾信心值<0.6以及非純中文且只有一個字的資料，輸出`resultCSV.csv`即為最終結果
```python
python ./toolCode/filterTxtToCsvResult.py
```
### 基本篩選+字串文字重組
除了過濾信心值<0.6以及非純中文且只有一個字的資料以外，針對信心值低於0.6的中文字串做重新組合的演算法，輸出`resultCSV.csv`即為最終結果
```python
python ./toolCode/filterTxtToCsvResultAdvance.py
```
### 

## 參考來源
