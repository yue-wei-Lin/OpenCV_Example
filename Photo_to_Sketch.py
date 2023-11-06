# ChatGPT:透過opencv將圖片做成素描圖
# 只能在colab上執行

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# 讀取照片
image = cv2.imread('me.png')

# 將照片轉換為灰階圖像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 反轉灰階圖像（將白色背景轉為黑色）
inverted_gray_image = cv2.bitwise_not(gray_image)

# 使用高斯模糊平滑圖像
blurred_image = cv2.GaussianBlur(inverted_gray_image, (111,111),0)

# 反轉模糊後的圖像（獲得素描風格）
inverted_blurred_image = cv2.bitwise_not(blurred_image)

# 將原始彩色圖像和素描風格圖像進行混合
sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

# 保存素描風格圖像
cv2.imwrite('sketch.jpg', sketch)

# 顯示原始照片和素描風格圖像（需要在窗口中顯示照片時使用）
cv2_imshow(image)
cv2_imshow(sketch)
