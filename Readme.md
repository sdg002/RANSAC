# Implementation of RANSAC algorithm 

This is an implementation of the RANSAC algorithm using Python


## List of Python files and folders
- **RANSAC.py** - Outermost Python script which can be executed from the command line
- **GenerateNoisyLine.py** - Outermost Python script which will generate a random straight line with salt-pepper noise
- **LineModel.py** - Implements a class that represents the equation of a straight line
- **Point.py** - Implements a class which represents a 2d point
- **RansacHelper.py** - Implements the core RANSAC algorithm
- **Util.py** - Utility functions
- **test_??.py** - These are unit test classes


## Quick start - Generating an image of a noisy line
- Run the script **GenerateNoisyLine.py** to generate a rectangular image with 1 line in a random orientation and salt-pepper noise
- The resulting image will be generated in the subfolder **.\out**

<img src="RANSAC/article/images/Sample_Output_GenerateNoisyImage.66.png" width="100%" height="100%" />

## Quick start - Perform RANSAC on a noisy image
- Run the script **RANSAC.py** to find the best fitting line in a noisy image
- The input file is controlled by a variable inside RANSAC.py and the this file should be placed in the subdirectory **.\input**
- The output is generated in the form of a new image which has the RANSAC line superimposed over the original line

<img src="RANSAC/article/images/Sample_Output_After_RANSAC_GenerateNoisyImage.66.png"  width="100%" height="100%" />


# References and further reading
- Youtube lecture (https://www.youtube.com/watch?v=BpOKB3OzQBQ)
- Wikipedia article on RANSAC (https://en.wikipedia.org/wiki/Random_sample_consensus)
- Deriving the least squares regression (https://online.stat.psu.edu/stat414/node/278/)
- Weighted least squares (https://towardsdatascience.com/when-and-how-to-use-weighted-least-squares-wls-models-a68808b1a89d)
- Hough transform (https://en.wikipedia.org/wiki/Hough_transform)
- Finding the maxima and minima (http://clas.sa.ucsb.edu/staff/lee/Max%20and%20Min's.htm)
