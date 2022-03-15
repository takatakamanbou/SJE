import cv2
import facedetect

# 画像を読み込む
image = cv2.imread( ここに画像ファイル名を指定 )
if image is None:
    exit('ファイルが見つかりません')
print(f'画像サイズ: {image.shape[1]} x {image.shape[0]}')

# 顔検出を実行
posizeList = facedetect.facedetect(image)

# 顔の位置と大きさを表示
for i, posize in enumerate(posizeList):
    print(f'{i+1}人目: (左上のx座標) = {posize[0]}, (y座標) = {posize[1]}, (幅) = {posize[2]}, (高さ) = {posize[3]}')

# 画像を書き出す
cv2.imwrite('hoge.png', image)

