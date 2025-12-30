# Pencil Sketch with Python 🎨✏️
Convert any image into a realistic pencil sketch using Python and OpenCV in less than 20 lines of code. This project reads an image, converts it to grayscale, inverts, blurs, and blends it to generate a pencil sketch effect. Simple, fast, beginner-friendly and completely reusable.

This project demonstrates how to convert any image into a beautiful pencil sketch using Python and OpenCV in less than 20 lines of code. Python is a powerful language and with OpenCV, image processing becomes extremely easy and efficient.

## 🧠 Concept Behind the Project
To convert an image into a pencil sketch, we follow these steps:

1️⃣ Select an input image  
2️⃣ Read it in RGB format  
3️⃣ Convert it to grayscale  
4️⃣ Invert the grayscale image (negative image)  
5️⃣ Apply Gaussian blur to smooth details  
6️⃣ Invert the blurred image  
7️⃣ Divide grayscale image by inverted blurred image to generate the sketch  

Since images are arrays, OpenCV makes these operations simple and powerful.

## 🚀 Features
- Simple and beginner friendly
- Uses only one library
- Converts image to sketch instantly
- Completely reusable
- Less than 20 lines of code

## 🛠️ Requirements
Install OpenCV using:
pip install opencv-python

## ▶️ How to Run
1️⃣ Install Python  
2️⃣ Install required library  
3️⃣ Place your image in the same folder and rename it to `input.jpg`  
4️⃣ Run the script: python main.py

## 🖼️ Application Screenshot
![App Screenshot](screenshot.png)

## 🤝 Contribution
Feel free to fork, enhance and reuse this project!
