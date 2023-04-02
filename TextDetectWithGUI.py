import cv2
import numpy as np
from PIL import Image, ImageTk
from pytesseract import image_to_string
from tkinter import Tk, Frame, Label, Button, PhotoImage,font
root = Tk()
root.title('Text Detection')
root.configure(background='maroon1')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("%dx%d"%(screen_width,screen_height))
center_frame = Frame(root)
center_frame.pack(expand=True)
src_path = r'D:\python\test2.png'
my_font = font.Font(size=12)
content = Label(center_frame,text='This Python program uses the OpenCV library and pytesseract OCR engine to detect text from an image. The program reads an image file from a specified path and converts it into a grayscale image.\n It then applies dilation and erosion filters to the image to remove any unwanted noise.\n The filtered image is then thresholded using an adaptive Gaussian filter to convert it into a binary image.\n The program then passes the binary image to pytesseract OCR engine to extract the text from the image.\n If text is detected, it is displayed in a label. The program also includes a button that triggers the text detection process\n\n There are several limitations to this program : \n\n1. Image quality: The program heavily relies on the quality of the input image. If the image is blurry or has low contrast, the program may not be able to detect the text accurately\n2. Text orientation: The program assumes that the text in the image is oriented horizontally. If the text is vertical or at an angle, the program may not be able to detect it accurately\n3. Language: The program uses the default language model for text recognition, which may not work well for languages other than English.\n 4. Performance: The program may be slow when processing large or complex images, which may affect its usability for real-time or time-critical applications.',font=my_font,bg='maroon1')
content.pack()
image = Image.open(src_path)
photo = ImageTk.PhotoImage(image)
stick = Label(center_frame, image=photo,padx=10,pady=10)
stick.pack()
this_frame = Frame(center_frame)
this_frame.pack()
def get_string(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    cv2.imwrite(src_path + "removed_noise.png", img)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    cv2.imwrite(src_path + "thres.png", img)
    result = image_to_string(Image.open(src_path + "thres.png"))
    if(result != ''):
        print(result)
        this_label = Label(this_frame,text=result)
        this_label.pack()
    else:
        print("Operation Failed!")
this_button = Button(this_frame,text="Detect Text",command=lambda:get_string(src_path),padx=10,pady=10)
this_button.pack()
root.mainloop()
