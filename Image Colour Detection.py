import cv2 as cv
import numpy as np
import pandas as pd
import matplotlib as mat
import PIL as pil
from PIL import Image
img_path = r"C:\Users\melro\PycharmProjects\HopeThisWorks\venv\Scripts\SPOTIFY-Image.jpg"
img = cv.imread(img_path)                       # loads image
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)        # converts into HSV colour space (easier to work with hues)

hsv_array = np.asarray(hsv)                     # loads HSV values into an array
pixelsWidth = len(hsv_array[1])
pixelsHeight = len(hsv_array)
HSV_arranged = np.reshape(hsv_array, ((pixelsHeight*pixelsWidth),3))    # reshapes array into single row array
HSVValues = pd.DataFrame(HSV_arranged, columns = ["H", "S", "V"])       # loads array into dataframe with H,S,V columns
HSVValuesMode = pd.DataFrame.mode(HSVValues, axis = 0)                  # finds mode value for hue (most dominant colour)
mode1RGBarr = np.array([HSVValuesMode["H"][0]/179, HSVValuesMode["S"][0]/255, HSVValuesMode["V"][0]/255])   # changes range for all to be 0-1
RGBMode = mat.colors.hsv_to_rgb(mode1RGBarr)*255                        # convert back to RGB colour space (mulitply 255 for RGB range)
RGB_colourR = RGBMode[0].astype(str)
RGB_colourG = RGBMode[1].astype(str)
RGB_colourB = RGBMode[2].astype(str)
print("RGB values = "+RGB_colourR+", "+RGB_colourG+", "+RGB_colourB)    # RGB values (can be used to set RGB LEDs to this colour)
img2 = np.ones((300,300,3),np.uint8)                                    # creates an array of ones for new image (300x300)
img2[:] = np.flip(RGBMode)                                              # loads BGR values into array (OpenCV works with BGR)
cv.imshow("Colour",img2)                                                # displays image
cv.waitKey(0)                                                           # necessary to display window infinitely until keypress
cv.destroyAllWindows()                                                  # close window
data = np.asarray(np.flip(img2)).astype(np.uint8)                       # saves img2 to new array
im = Image.fromarray(data, mode="RGB")                                  # create image from array
im.save("D:\Files\Wallpapers\Desktop Wallpapers\Palette.jpg")          # saves image