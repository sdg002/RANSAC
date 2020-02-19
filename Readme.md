# Implementation of RANSAC algorithm  (Article on Medium)
This is the source code of my article on Medium
https://medium.com/@saurabh.dasgupta1/outlier-detection-using-the-ransac-algorithm-de52670adb4a


# About the source code
I have used the following tools to author the Python scripts that accompany this article.
1. Visual Studio 2019
1. with Python project templates
1. Python 3.7 engine



# Quick start
## Generating an image of a noisy line
- Run the script **GenerateNoisyLine.py** to generate a rectangular image with 1 line in a random orientation and salt-pepper noise
- The resulting image will be generated in the subfolder **.\out**

<img src="RANSAC/article/images/Sample_Output_GenerateNoisyImage.66.png" width="100%" height="100%" />

## Perform RANSAC on a noisy image
- Run the script **RANSAC.py** to find the best fitting line in a noisy image
- The input file is controlled by a variable inside RANSAC.py and the this file should be placed in the subdirectory **.\input**
- The output is generated in the form of a new image which has the RANSAC line superimposed over the original line

<img src="RANSAC/article/images/Sample_Output_After_RANSAC_GenerateNoisyImage.66.png"  width="100%" height="100%" />

# Examples of noisy image 

## Random line with all points on the line and a background of salt-pepper noise
<img src="RANSAC/article/images/Sample_Output_GenerateNoisyImage.66.png" width="100%" height="100%" />

## Random line with points generated using Gaussian distribution and a background of salt-pepper noise
<img src="RANSAC/article/images/NoisyLine-Gaussian-sp-0.80.1.png" width="100%" height="100%" />

# List of Python files and folders

The folder hierarchy is as follows:
## **Common** - Python module files
- **LineModel.py** - Implements a class that represents the equation of a straight line
- **Point.py** - Implements a class which represents a 2d point
- **RansacHelper.py** - Implements the core RANSAC algorithm
- **Util.py** - Utility functions
- **test_??.py** - These are unit test classes

## **RANSAC** - Runnable python files which reference the module files in *Common*
- **RANSAC.py** - Outermost Python script which can be executed from the command line
- **GenerateNoisyLine.py** - Outermost Python script which will generate a random straight line with salt-pepper noise
- **GenerateNoisyLineGaussian.py** - Outermost Python script which will generate a random line with Gaussian noise around the line on a background with salt-pepper noise
- .\input\ - The folder containing input files
- .\output\ - The folder where the resulting images are published

## Configuring the Python environment
If you are using Visual Studio 2019 as your Python IDE then you can configure the project properties of *RANSAC* and specify the *Search path* property
For other environments, the PYTHONPATH environment variable should be set to the physical location of *Common* folder

# References and further reading
- Wikipedia article on RANSAC (https://en.wikipedia.org/wiki/Random_sample_consensus)
- Youtube lecture (https://www.youtube.com/watch?v=BpOKB3OzQBQ)
- Deriving the least squares regression (https://online.stat.psu.edu/stat414/node/278/)
- Weighted least squares (https://towardsdatascience.com/when-and-how-to-use-weighted-least-squares-wls-models-a68808b1a89d)
- Hough transform (https://en.wikipedia.org/wiki/Hough_transform)
- Finding the maxima and minima (http://clas.sa.ucsb.edu/staff/lee/Max%20and%20Min's.htm)
