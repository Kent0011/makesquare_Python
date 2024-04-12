import os
import cv2
import glob
import numpy as np

#========================================================================================
#
#
# 画像正方形化ツール
# 画像の上下または左右に余白を追加し正方形画像を生成します。
#
# 使用方法
# 1. このプログラムと同じディレクトリに'input'および'output'という名称のディレクトリを作成
# 2. 'input'に正方形化したい画像を入れる
# 3. 実行 : $ python makesquare.py      
# 4. 'output'ディレクトリに正方形化された画像ファイルが出力されます
#
#
#
#=========================================================================================



# inputディレクトリにある.jpegファイルをすべて読み込み
filenames = []
imglist = []

dir = os.path.dirname(__file__) #現在のパスを取得

files = glob.glob(dir + '/input/*.jpeg')    #対象画像のパスをリストで取得

for i in range(len(files)):     #画像を読み込み、imglistに格納
    
    img = cv2.imread(files[i])
    imglist.append(img)
    

for i in range(len(files)):             #ファイル名をfilenamesに格納
    filenames.append(files[i][len(dir) + 7:])
    

print('import succed:')
for i in range(len(filenames)):
    print(filenames[i])

    
# メイン処理部分
for i in range(len(imglist)):
    
    if imglist[i].shape[0] == imglist[i].shape[1]:  #正方形画像
        cv2.imwrite(dir + '/output/square_' + filenames[i], imglist[i])    # 元から正方形ならば、そのまま返す
        
    elif imglist[i].shape[0] < imglist[i].shape[1]: #横長画像
        diff = imglist[i].shape[1] - imglist[i].shape[0]
        margin = np.full((int(diff/2), imglist[i].shape[1],3), 255)
        
        img = np.concatenate([margin,imglist[i],margin],axis = 0)
        
        if img.shape[0] == img.shape[1]:
            cv2.imwrite(dir + '/output/square_' + filenames[i], img)
            print('succed!: ' + filenames[i])
        else:
            print('ellor: ' + filenames[i])
        
    elif imglist[i].shape[0] < imglist[i].shape[1]: #縦長画像
        diff = imglist[i].shape[0] - imglist[i].shape[1]
        margin = np.full((imglist[i].shape[0],int(diff/2),3), 255)
        
        img = np.concatenate([margin,imglist[i],margin],axis = 1)
        
        if img.shape[0] == img.shape[1]:
            cv2.imwrite(dir + '/output/square_' + filenames[i], img)
            print('succed!: ' + filenames[i])
        else:
            print('ellor: ' + filenames[i])