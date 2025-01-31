# LUCI

### LUCI : Land use change analysis of the Indian subcontinent using machine learning 

### About
Analyzing the land use / land cover in the Indian subcontinent using Indian Remote Sensing (IRS) data while applying machine learning techniques

### Objectives
* Development of a thematic map indicating land cover in the Indian subcontinent.
* Comparison of various machine learning algorithms to achieve high accuracy in segmentation and classification.
* Analyze change in land cover patterns over the study period.
* Investigate the relationship between change in land cover and the climate in the region.


### Dataset
This implementation uses the orthorectified multi-spectral Resourcesat- 1, Advanced Wide Field Sensor (AWiFS) unlabeled data, which  operates in three spectral bands in VNIR and one band in SWIR with 56 metre spatial resolution and a combined swath of 730 km achieved through two AWiFS cameras. The dataset can be obtained at Bhuvan- ISRO's geoportal and the gateway to Indian earth observation.

### Tools and Technologies used
Python and its various toolkits have been used in this implementation.
* TensorFlow - a computational framework for building machine learning models.
* Keras - a high-level neural networks API, capable of running on top of TensorFlow.
* Numpy - a fundamental package for scientific computing with Python.
* Scikit-learn - a machine learning library for Python.
* OpenCV - an open source computer vision library.
* ImageMagick - An open source software used to work with images.
* GIMP -  An open source image editor.

### Implementation
The following are the steps followed in the implementation of this project.
1. The obtained images are 4 single band images. They are normalized using image-magick. Some structure can be seen after normalization ( norm.sh ).
2. For better visual perception, false color is added ( addfalse.py ).
3. K-means is applied to segment the coloured images. Labeling is done manually by refering to the ground truth images (kmeans.py). 
4. To obtain better accuracy, pixelwise labeling is done by considering the region of interest (ROI) and obtaining the range of intensity values for each terrain across the 4 bands (roi.py).
5. Each image is read and pixel-wise labeling is done manually (rdpix.py).
6. The data is passed through classifier and the model is stored (classifier.py).
7. The saved model is loaded and image is predicted for the testing dataset (test.py).
8. Create an image from the predicted labels and stitch multiple images together to obtain a terrain map (addcolor.py).
