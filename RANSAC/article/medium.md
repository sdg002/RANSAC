# Introduction
In this article we will explore the Random Sample Consensus algorithm - more popularly known by the acronym RANSAC. This is an iterative and a non-deterministic algorithm that helps in eliminating outliers. This algorithm is commonly used  to solve computer vision challenges. I have written a sample implementation using Python

# Problem definition
Consider the following diagram. The human mind can immediately spot that there is one straight line and the mind has no difficulty in distinguising the inliers from the outliers. How can me make the computer emulate this aspect of the human behavior? The RANSAC algorithm attempts to address this challenge.

<<Show a picture of points along a straight line, with some noisy points - The human mind is able to identify the outliers - how do we make the computer achieve this>>

# Traditional approach - Fitting a straight line using the least squares regression method
<<Show a picture, points and a line passing - no noise>>
Consider the points above. How do we find a line which fits this distribution? One of the popular approaches is the least square distance method. In this approach we 

- Create a cost function which sum up the distance of all points from the line
- Interatively tinker with the equation of the line and evaluate the cost function
- Select the line line which yields the lowest cost function

<Show a line, show some points, indicate the vertical distance of every point from the line, we want to make the reader derive the least squares cost function> 

- Consider any point P<sub>i</sub> with coordinates (X<sub>i</sub>, Y<sub>i</sub>)
- Consider a straight line with the equation y=mx+c where  **m** is the slope and the Y intercept is **c** 
<<Show a simple picture of a straight line, show slope, show Y intercept>>
- The vertical distance of point P from this line is given by  d<sub>i</sub>=(mx<sub>i</sub>+c) - y<sub>i</sub>
- We do want to be worried about negative values. Therfore let us square the above distance
- The summation of the square of the vertical distance of all **N** points is given by Sum =&Sigma;(mx<sub>i</sub>+c) - y<sub>i</sub>)<sup>2</sup>
- We can express the summationi as a function which is dependent on two variables - The slope **m** and the Y intercept **c**
- Therefore the cost function f(m,c) = &Sigma;(mx<sub>i</sub>+c) - y<sub>i</sub>)<sup>2</sup>
- Since we have 2 variables (m and C) we need 2 equations
- We will use partial differentiation to find the values of m and c which yield the lowest value
- The partial derivatives of f(m,c) with respect to the variables m and c would have to be zero to give us the lowest cost value
- <sup>df</sup>&frasl;<sub>dm</sub> = 2&Sigma;(mx<sub>i</sub>+c) - y<sub>i</sub>)*x<sub>i</sub>
- <sup>df</sup>&frasl;<sub>dc</sub> = 2&Sigma;(mx<sub>i</sub>+c) - y<sub>i</sub>)
- In the interest of time, I will skip the derivation of the least squares distance formula and straight away present the solution
- m=(N&Sigma;(xy) -&Sigma;x&Sigma;y)/(N&Sigma;(x<sup>2</sup>) + (&Sigma;x)<sup>2</sup>)
- c= (&Sigma;y - m&Sigma;x)/N

# Challenges with least squares regression 
Consider the data points shown below. The data appears to follow a straight line and indeed least squares regression gives us a nice line that models the data.
<<Show a pic with some points and a nicely fit line>>
But real data is seldom so clean. Let us add one outlier to this distribution and find the best fitting line using least squares regression
<<Show a picture , same as immediately above, but with 1 outlier point, show the line>>
We can see that the single outlier has brought about a considerable change. The out of box least squares method is very sensitive to outliers. Algorithms like weighted least squares use the distance of a point from the straight line as a weight to minimize the impact of far flung points. In this article we will restrict ourselves to RANSAC.

**you were here**


# Understanding RANSAC
This is the body ddkkd

# The algorithm
This is the body ddkkd

# Results
This is the body ddkkd

# Overview of the code
This is the body ddkkd

# References
- Weighted least squares 
- Youtube video
- Wikipedia article
 
ssd
sdsds


sfdsfsdfsdf
sdfsdfsdf msf,sd,,,,,,,,,,