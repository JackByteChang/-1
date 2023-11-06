import cv2
import numpy as np
from google.colab.patches import cv2_imshow
# 讀取圖片
image = cv2.imread('Jackson.png')

# 應用高斯模糊
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# 調整亮度和對比度
alpha = 1.5  # 控制對比度（大於1增加對比度，小於1降低對比度）
beta = 50    # 控制亮度（正數增加亮度，負數降低亮度）

brightened_image = cv2.convertScaleAbs(blurred_image, alpha=alpha, beta=beta)

# 儲存美化後的圖片
cv2.imwrite('beautified_image.png', brightened_image)

# 顯示原始圖片和美化後的圖片
cv2_imshow(image)
cv2_imshow(brightened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
