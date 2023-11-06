# ChatGPT:透過opencv將圖片做成卡通圖

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# 讀取圖片
image = cv2.imread('me.png')

# 灰度轉換
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 邊緣檢測
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# 色彩量化
color = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)

# 合併邊緣和彩色圖像
cartoon = cv2.bitwise_and(color, color, mask=edges)

# 保存處理後的圖片
cv2.imwrite('cartoon.jpg', cartoon)

# 顯示原始圖片和處理後的圖片（需要在窗口中顯示圖片時使用）
cv2_imshow(image)
cv2_imshow(cartoon)
