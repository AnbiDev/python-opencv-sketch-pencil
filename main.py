import cv2

# Nama gambarnya kalian sesuaikan dengan yang ingin kalian konversi
# Kalau mau lebih mudah, jadiin satu folder aja
img = cv2.imread('mikasa.jpg', 1)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("hasil_gray.png", img_gray)

img_invert = cv2.bitwise_not(img_gray)
cv2.imwrite("hasil_invert.png", img_invert)

img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
cv2.imwrite("hasil_pra.png", img_smoothing)

final_img = cv2.divide(img_gray, 255 - img_smoothing, scale=256)
cv2.imwrite("hasil.png", final_img)




