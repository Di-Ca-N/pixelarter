import cv2


def remove_alpha(image):
    trans_mask = image[:, :, 3] == 0
    image[trans_mask] = [255, 255, 255, 255]
    new_img = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
    return new_img


def pixelize(image, pixelart_size=(24, 24), output_size=(256, 256)):
    smoothed = cv2.bilateralFilter(image, 3, 70, 70)
    little = cv2.resize(smoothed, pixelart_size)
    display = cv2.resize(little, output_size, interpolation=cv2.INTER_NEAREST)
    display_8_bit = display.astype('uint8')
    return display_8_bit
