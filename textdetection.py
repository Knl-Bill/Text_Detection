import pytesseract
from PIL import Image

# Load the captcha image
captcha = Image.open("captchatext.png")

# Convert the image to grayscale
captcha = captcha.convert('L')

# Use pytesseract to read the text from the image
text = pytesseract.image_to_string(captcha)

# Print the captcha text
print(text)
