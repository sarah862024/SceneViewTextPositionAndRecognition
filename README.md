# Scene View Text Position And Recognition
Taiwan Scene View Text Position and Recognition

* 目錄
  * [訓練資料前處理](https://github.com/sarah862024/SceneViewTextPositionAndRecognition#%E8%A8%93%E7%B7%B4%E8%B3%87%E6%96%99%E5%89%8D%E8%99%95%E7%90%86 "link")
    * [取得中文字元文字檔(ChineseCharList.txt)](https://github.com/sarah862024/SceneViewTextPositionAndRecognition#%E5%8F%96%E5%BE%97%E4%B8%AD%E6%96%87%E5%AD%97%E5%85%83%E6%96%87%E5%AD%97%E6%AA%94chinesecharlisttxt "link")
    * [擷取出資料集所有影像中的文字區塊](https://github.com/sarah862024/SceneViewTextPositionAndRecognition#%E6%93%B7%E5%8F%96%E5%87%BA%E8%B3%87%E6%96%99%E9%9B%86%E6%89%80%E6%9C%89%E5%BD%B1%E5%83%8F%E4%B8%AD%E7%9A%84%E6%96%87%E5%AD%97%E5%8D%80%E5%A1%8A "link")
    * [分割訓練集、驗證集、測試集](https://github.com/sarah862024/SceneViewTextPositionAndRecognition#%E5%88%86%E5%89%B2%E8%A8%93%E7%B7%B4%E9%9B%86%E9%A9%97%E8%AD%89%E9%9B%86%E6%B8%AC%E8%A9%A6%E9%9B%86 "link")
    * [生成Ground Truth](https://github.com/sarah862024/SceneViewTextPositionAndRecognition#%E7%94%9F%E6%88%90ground-truth "link")
  * [擴增資料處理](https://github.com/sarah862024/SceneViewTextPositionAndRecognition#%E6%93%B4%E5%A2%9E%E8%B3%87%E6%96%99%E8%99%95%E7%90%86 "link")
    * 
  * [訓練文字辨識模型](https://github.com/sarah862024/SceneViewTextPositionAndRecognition#%E8%A8%93%E7%B7%B4%E6%96%87%E5%AD%97%E8%BE%A8%E8%AD%98%E6%A8%A1%E5%9E%8B "link")
    * [建立lmdb資料集](https://github.com/sarah862024/SceneViewTextPositionAndRecognition#%E5%BB%BA%E7%AB%8Blmdb%E8%B3%87%E6%96%99%E9%9B%86 "link")
    * [訓練模型](https://github.com/sarah862024/SceneViewTextPositionAndRecognition#%E8%A8%93%E7%B7%B4%E6%A8%A1%E5%9E%8B "link")
  * [執行文字定位及辨識](https://github.com/sarah862024/SceneViewTextPositionAndRecognition#%E5%9F%B7%E8%A1%8C%E6%96%87%E5%AD%97%E5%AE%9A%E4%BD%8D%E5%8F%8A%E8%BE%A8%E8%AD%98 "link")
    * [執行文字定位模型](https://github.com/sarah862024/SceneViewTextPositionAndRecognition#%E5%9F%B7%E8%A1%8C%E6%96%87%E5%AD%97%E5%AE%9A%E4%BD%8D%E6%A8%A1%E5%9E%8B "link")
    * [擷取出影像中的文字區塊儲存成影像](https://github.com/sarah862024/SceneViewTextPositionAndRecognition#%E6%93%B7%E5%8F%96%E5%87%BA%E5%BD%B1%E5%83%8F%E4%B8%AD%E7%9A%84%E6%96%87%E5%AD%97%E5%8D%80%E5%A1%8A%E5%84%B2%E5%AD%98%E6%88%90%E5%BD%B1%E5%83%8F "link")
    * [執行文字辨識模型](https://github.com/sarah862024/SceneViewTextPositionAndRecognition#%E5%9F%B7%E8%A1%8C%E6%96%87%E5%AD%97%E8%BE%A8%E8%AD%98%E6%A8%A1%E5%9E%8B "link")
  * [辨識結果篩選](https://github.com/sarah862024/SceneViewTextPositionAndRecognition#%E8%BE%A8%E8%AD%98%E7%B5%90%E6%9E%9C%E7%AF%A9%E9%81%B8 "link")
    * [如果將文字定位結果分為Word、Char兩部分個別進行文字辨識(如沒有則略過此部分)](https://github.com/sarah862024/SceneViewTextPositionAndRecognition#%E5%A6%82%E6%9E%9C%E5%B0%87%E6%96%87%E5%AD%97%E5%AE%9A%E4%BD%8D%E7%B5%90%E6%9E%9C%E5%88%86%E7%82%BAwordchar%E5%85%A9%E9%83%A8%E5%88%86%E5%80%8B%E5%88%A5%E9%80%B2%E8%A1%8C%E6%96%87%E5%AD%97%E8%BE%A8%E8%AD%98%E5%A6%82%E6%B2%92%E6%9C%89%E5%89%87%E7%95%A5%E9%81%8E%E6%AD%A4%E9%83%A8%E5%88%86 "link")
    * [基本篩選](https://github.com/sarah862024/SceneViewTextPositionAndRecognition#%E5%9F%BA%E6%9C%AC%E7%AF%A9%E9%81%B8 "link")
    * [基本篩選+字串文字重組](https://github.com/sarah862024/SceneViewTextPositionAndRecognition#%E5%9F%BA%E6%9C%AC%E7%AF%A9%E9%81%B8%E5%AD%97%E4%B8%B2%E6%96%87%E5%AD%97%E9%87%8D%E7%B5%84 "link")
  * [參考來源](https://github.com/sarah862024/SceneViewTextPositionAndRecognition#%E5%8F%83%E8%80%83%E4%BE%86%E6%BA%90 "link")

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
### 如果將文字定位結果分為Word、Char兩部分個別進行文字辨識(如沒有則略過此部分)
如果將文字定位結果分為Word、Char兩部分個別進行文字辨識，辨識結果的兩個文字檔分別為`demoResult_Char.txt`以及`demoResult_Word.txt`
先針對`demoResult_Word.txt`的結果過濾純中文且只有一個字的項目，輸出`demoResult_Word_filter.txt`的結果
```python
python ./toolCode/demoResult_Word.py
```
再針對`demoResult_Char.txt`的結果過濾英文及數字的項目，輸出`demoResult_Char_filter.txt`的結果
```python
python ./toolCode/demoResult_Char.py
```
然後手動將`demoResult_Word_filter.txt`以及`demoResult_Char_filter.txt`合併成同一個文字檔`demoResult_WordChar_filter.txt`
再執行`sortDemoWordChar.py`來對資料進行排序，得到排序後的輸出結果`demoResult_WordChar_filter_sorted.txt`
```python
python ./toolCode/sortDemoWordChar.py
```
接著下面篩選的部分就使用此文字檔`demoResult_WordChar_filter_sorted.txt`去篩選  
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
## 參考來源
文字定位模型:
https://github.com/clovaai/CRAFT-pytorch  
擴增資料方法:  

文字辨識模型:
https://github.com/clovaai/deep-text-recognition-benchmark
