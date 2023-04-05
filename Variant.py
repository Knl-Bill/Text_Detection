import cv2
import numpy as np
from PIL import Image, ImageTk
from tkinter import Tk,Frame,Label,Button,PhotoImage,font,filedialog
from pytesseract import image_to_string
def get_string(img_path,this_frame):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    img_path = img_path + "removed_noise.png"
    cv2.imwrite(img_path, img)
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    cv2.imwrite(img_path + "thres.png", img)
    result = image_to_string(Image.open(img_path + "thres.png"))
    if(result != ''):
        print(result)
        this_label = Label(this_frame,text=result)
        this_label.pack()
    else:
        print("Operation Failed!")
class Text_Detect:
    def __init__(self) -> None:
        root = Tk()
        root.title('Text Detection')
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry("%dx%d"%(screen_width,screen_height))
        center_frame = Frame(root)
        center_frame.pack(expand=True)
        src_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
        my_font = font.Font(size=13)
        my_font1 = font.Font(size=40)
        heading = Label(center_frame,text='Captcha Text Detection',font=my_font1,pady=15)
        heading.pack()
        fin = open('Description.txt','r')
        data = fin.readlines()
        desc = []
        for line in data:
              desc.append(line)
        data = ''
        for i in desc:
              data += i
        content = Label(center_frame,text=data,font=my_font,bg='maroon1')
        content.pack()
        br = Label(center_frame,text='\n')
        br.pack()
        image = Image.open(src_path)
        photo = ImageTk.PhotoImage(image)
        stick = Label(center_frame, image=photo,padx=10,pady=10)
        stick.pack()
        this_frame = Frame(center_frame)
        this_frame.pack()
        br = Label(this_frame,text='\n')
        br.pack()
        this_button = Button(this_frame,text="Detect Text",command=lambda:get_string(src_path,this_frame),padx=10,pady=10)
        this_button.pack()
        root.mainloop()
        
obj = Text_Detect()