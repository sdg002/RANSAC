# Introduction

The RANSAC (Random sample and consensus) algorithm is the "gold standard" in eliminating noise. A while ago, I wrote an [article](https://medium.com/@saurabh.dasgupta1/outlier-detection-using-the-ransac-algorithm-de52670adb4a)  on how the RANSAC algorithm is implemented for finding the model of a straight line in a noisy field of points. 

The RANSAC algorithm in its original form was developed around finding straight line models when presented with noisy visual data. In this article, I will explore how to implement the RANSAC algorithm a circle model in a noisy set of points. I hope that by the end of this article you will appreciate how beautiful RANSAC is. Sometimes, I get carried away and visualize that human brain is perhaps doing some sort of RANSAC deep inside. Enough!


![Human mind](images/Intro_HumanMind_SeesStraightLine.PNG)

<<Overlay a good line and a bad line, Tag them as expected and actual>>


# Problem definition

Consider the points shown below. It is not difficult to spot there is a nice circle that can be traced out of the points only if we exclude the 2 noisy points on the far right of the visual.

## Fitting a noisy circle - before
<img src="circle-images/Simple.png" />

## Fitting a circle - using Gradient descent algorithm
The output after finding the best fitting circle is presented below.
<img src="circle-images/Simple_After_GradientDescent.png" />

## Fitting a circle -  using RANSAC
The output after using RANSAC to take into account the outliers. Notice that the algorithm has nicely detected the noisy points on the far right
<img src="circle-images/Simple_After_Ransac.png" />


# Understanding the RANSAC algorithm for fitting a circle

<<you will need some diagrams to explain how the algo works, show 3 points, fit a circle, how many outliers>>
<< do it via Power point>>
# Formal definition of the RANSAC algorithm
<<write the algo in a formal language, wee Wikipedia >>

# Overview of the source code



# Reference
- Youtube lecture (https://www.youtube.com/watch?v=BpOKB3OzQBQ)
- Wikipedia article on RANSAC (https://en.wikipedia.org/wiki/Random_sample_consensus)
- Finding the maxima and minima (http://clas.sa.ucsb.edu/staff/lee/Max%20and%20Min's.htm)
- My original article on RANSAC for straight lines (https://medium.com/@saurabh.dasgupta1/outlier-detection-using-the-ransac-algorithm-de52670adb4a)




