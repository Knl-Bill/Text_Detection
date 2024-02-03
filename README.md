# Text Detection using OpenCV and Tesseract

## Contents

1. [Overview](#overview)
2. [Description](#description)
3. [Installation](#installation)
4. [Usage](#usage)

## Overview

This project demonstrates text detection in images using OpenCV and Tesseract. It provides a graphical user interface (GUI) built with Tkinter for easy interaction.

## Description

The application uses OpenCV to preprocess the image by converting it to grayscale, applying morphological transformations, and performing adaptive thresholding. The preprocessed image is then passed to Tesseract OCR for text extraction.

The Tkinter-based GUI provides a user-friendly interface for selecting images and initiating text detection.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/Text-Detection.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Text-Detection
    ```

3. Install the required dependencies:

    ```bash
    pip install opencv-python numpy Pillow pytesseract
    ```

    Ensure that Tesseract OCR is installed on your system. You can download it from [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract).

4. Run the application:

    ```bash
    python Text_Detection.py
    ```

## Usage

1. Launch the application.

2. Select an image file (supported formats: jpg, jpeg, png, bmp) for text detection using the file dialog.

3. The GUI displays the image and provides a button to perform text detection.

4. Click the "Detect Text" button.

5. The detected text will be printed to the console, and a label with the detected text will be displayed on the GUI.
