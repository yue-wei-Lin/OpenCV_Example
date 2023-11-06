#風格化

import cv2
import numpy as np

img1 = cv2.imread( "me.png", -1 )
img2 = cv2.stylization( img1 )
cv2_imshow( img1 )
cv2_imshow( img2 )
