# ChatGPT:透過opencv將圖片美化
# 只能在colab上執行

import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# 讀取圖片
image = cv2.imread('me.png')

# 模糊效果（使用均值模糊）
blurred = cv2.GaussianBlur(image, (15, 15), 0)

# 銳化效果（使用卷積核）
kernel = np.array([[-1, -1, -1],
                   [-1, 9, -1],
                   [-1, -1, -1]])
sharpened = cv2.filter2D(blurred, -1, kernel)

# 調整亮度和對比度
alpha = 1.5  # 控制對比度（大於1增加對比度，小於1降低對比度）
beta = 30    # 控制亮度（正值增加亮度，負值降低亮度）
adjusted = cv2.convertScaleAbs(sharpened, alpha=alpha, beta=beta)

# 保存處理後的圖片
cv2.imwrite('output.jpg', adjusted)

# 顯示原始圖片和處理後的圖片（需要在窗口中顯示圖片時使用）
cv2_imshow(image)
cv2_imshow(adjusted)
