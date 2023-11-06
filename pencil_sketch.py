#鉛筆素描

import cv2
import numpy as np

img = cv2.imread( "me.png", -1 )
img1, img2 = cv2.pencilSketch( img )
cv2_imshow( img )
cv2_imshow( img1 )
cv2_imshow( img2 )
