
# Wally Detection Project  

This repository contains a Python project for detecting the character **Wally** (from the "Where's Wally?" series) in an image. The project uses a custom-trained Haar Cascade classifier and OpenCV for image processing and object detection.  

## Features  
- Detects multiple instances of Wally in a single image.  
- Highlights detected regions with bounding rectangles.  
- Utilizes a pre-trained XML classifier built from positive and negative samples.  

## Requirements  
To run this project, ensure you have the following installed:  

- Python 3.x  
- OpenCV (`cv2`)  
- NumPy (`numpy`)  

Install dependencies using:  
```bash
pip install opencv-python numpy
```  

## Project Structure  
- **`cascade_fin.xml`**: The trained Haar Cascade classifier file.  
- **`n8.jpg`**: Example input image containing Wally.  
- **`wally_detection.py`**: The main Python script for detection.  

## How It Works  

1. **Loading the Classifier**  
   The script loads the Haar Cascade classifier (`cascade_fin.xml`) trained using positive and negative samples of Wally.  
   ```python
   wally = cv.CascadeClassifier("cascade_fin.xml")
   if wally.empty():
       print("Error: no se pudo cargar el clasificador.")
   else:
       print("Clasificador cargado correctamente.")
   ```

2. **Reading the Image**  
   The input image (`n8.jpg`) is loaded using OpenCV.  
   ```python
   frame = cv.imread("n8.jpg")
   if frame is None:
       print("Error: no se pudo cargar la imagen.")
   else:
       print("Imagen cargada correctamente.")
   ```

3. **Converting to Grayscale**  
   The image is converted to grayscale for preprocessing.  
   ```python
   gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
   ```

4. **Detecting Wally**  
   The classifier scans the image for matches and returns bounding box coordinates for each detection.  
   ```python
   wallys = wally.detectMultiScale(gray, 1.5, 5)
   ```

5. **Drawing Rectangles**  
   Detected regions are marked with green rectangles.  
   ```python
   for (x, y, w, h) in wallys:
       frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
   ```

6. **Displaying Results**  
   The output image with rectangles is displayed in a window.  
   ```python
   cv.imshow('wally', frame)
   cv.waitKey(0)
   cv.destroyAllWindows()
   ```  

## Training the Classifier  
The `cascade_fin.xml` file was trained using the OpenCV Haar Cascade training process. This involved:  
1. Collecting **positive samples** (images containing Wally).  
2. Collecting **negative samples** (images without Wally).  
3. Using OpenCV tools to train the classifier with these samples.  

## Usage  
1. Clone the repository:  
   ```bash
   git clone https://github.com/Fergetse/AI_ElementDetection
   cd wally-detection
   ```  

2. Place your input image in the project folder.  

3. Run the detection script:  
   ```bash
   python wally_detection.py
   ```  

4. View the result in the OpenCV display window.  

## Example Output  
Input image:  

![Input Image](path/to/your/image.jpg)  

Output image with Wally detected:  

![Output Image](path/to/your/output_image.jpg)  

## Future Improvements  
- Enhance classifier accuracy with more training samples.  
- Add support for real-time detection using a webcam.  
- Integrate deep learning models for improved detection.  

## Contributions  
Contributions are welcome! Feel free to open issues or submit pull requests.  

## License  
This project is licensed under the MIT License.  
