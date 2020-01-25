# Introduction
In this article we will explore the **Random Sample Consensus** algorithm - more popularly known by the acronym RANSAC. This is an iterative and a non-deterministic algorithm that helps in eliminating outliers. This algorithm is commonly used  to solve computer vision challenges. In this article I have presented the motivation for the RANSAC algorithm and the source code for a simplistic implementation using **Python**.

# Problem definition
Consider the distribution of points in the following diagram. 

<img src="images/Intro_HumanMind_SeesStraightLine.png"/>

The human mind can immediately spot that all the points in this distribution but for one is aligned in a straight line and the mind has no difficulty in distinguising the inliers from the outliers. How can me make the computer emulate this aspect of the human behavior? The RANSAC algorithm attempts to address this challenge.

# Traditional approach - Fitting a straight line using the least squares regression method
<img src="images/SimpleLinearRegression.png"/>

Consider the points above. How do we find a line which fits this distribution? One of the popular approaches is the least square distance method. In this approach we 

- Create a cost function which sum up the distance of all points from the line
- Interatively tinker with the equation of the line and evaluate the cost function
- Select the line line which yields the lowest cost function

## How do we build a cost function?

<img src="images/y_mx_plus_c.png"/>


- Consider any point P<sub>i</sub> with coordinates (X<sub>i</sub>, Y<sub>i</sub>)
- Consider a straight line with the equation y=mx+c where  **m** is the slope and the Y intercept is **c** 

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

<img src="images/Linear_Regression_Perfect.png"/>

But real data is seldom so clean. Let us add one outlier to this distribution  (10,15) and find the best fitting line using least squares regression

<img src="images/Linear_Regression_Noise.png"/>

We can see that the single outlier has brought about a considerable change. The out of box least squares method is very sensitive to outliers. Algorithms like weighted least squares use the distance of a point from the straight line as a weight to minimize the impact of far flung points. In this article we will restrict ourselves to RANSAC.


# Understanding RANSAC - Overview
Before getting into the full details, I have presented a distilled version of RANSAC in this section
- Randomly select a smaller set of points (**n**) from the entire distribution (**N**)
- Use least squares regression to determine the linear equation which fits the **n** points
- Determine the average of the distance of every point **N** from this line. This score can be treated as a score which measure the goodness of the line. 
- Keep track of the **score**. If this score is lesser than the last known score then discard the older linear equation and select the current linear equation.
- Go back the first step and continue iterating till you have completed a predetermined number of iterations
- The linear equation available at the end of the iterations is possibly the best candidate line

We can see that the algorithm is not deterministic and hence the name *Random* in the acronym RANSAC. It is possible that you may not get the best model.


# Understanding RANSAC - Detailed (TODO)
This is the body ddkkd

# Results (TODO)
This is the body ddkkd

# Overview of the code (TODO)
This is the body ddkkd

# References and further reading
- Youtube lecture (https://www.youtube.com/watch?v=BpOKB3OzQBQ)
- Wikipedia article on RANSAC (https://en.wikipedia.org/wiki/Random_sample_consensus)
- Deriving the least squares regression (https://online.stat.psu.edu/stat414/node/278/)
- Weighted least squares (https://towardsdatascience.com/when-and-how-to-use-weighted-least-squares-wls-models-a68808b1a89d)
- Hough transform (https://en.wikipedia.org/wiki/Hough_transform)
