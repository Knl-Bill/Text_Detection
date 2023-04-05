# Text_Detection
The objective of this project is to develop a Python program that can detect captcha texts from an image using OpenCV and Pytesseract with Tesseract OCR. Captchas can sometimes be a hindrance for users who struggle to read distorted text. The project aims to create a solution to this problem by developing a program that can detect captcha texts from an image and display it in a clear and readable format. The program will use OpenCV to pre-process the image and extract the captcha text. Pytesseract with Tesseract OCR will then be used to recognize the extracted text.

The Program will consist of the following steps:  

1.	Implement a user interface feature to select an image file
2.	Load the captcha image into the program using OpenCV
3.	Pre-process the image using OpenCV and PIL techniques such as thresholding, erosion, and dilation to remove noise and enhance the captcha text
4.	Use Pytesseract with Tesseract OCR to recognize the captcha text from the pre-processed image
5.	Display the recognized captcha text in a clear and readable format 

There are several limitations to this program :

1. Image quality: The program heavily relies on the quality of the input image. If the image is blurry or has low contrast, the program may not be able to detect the text accurately
2. Text orientation: The program assumes that the text in the image is oriented horizontally. If the text is vertical or at an angle, the program may not be able to detect it accurately
3. Language: The program uses the default language model for text recognition, which may not work well for languages other than English.
4. Performance: The program may be slow when processing large or complex images, which may affect its usability for real-time or time-critical applications.

