import cv2
from pixelart import remove_alpha, pixelize

image = cv2.imread('examples/mario/input.png', cv2.IMREAD_8U)
cv2.imwrite('examples/mario/output.png', pixelize(image))
