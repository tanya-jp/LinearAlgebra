# LinearAlgebra
This repository contains four mini-projects covering the important topics in Linear Algebra.

## Coordinate System
In this mini-project, the aim is to solve a `coordinate system` using `augmented matrix`. The steps of solving the given system are listed in the following:
  1. Creating augmented matrix 
  2. Finding pivot columns
  3. Choosing a non-zero pivot column and put that in pivot position by interchanging
  4. Using row replacement to change each entry under the pivot position to zero
  5. Making echelon form of the matrix
  6. Finding free variables
  7. Printing results
 - Input Coordinate System
 ```
   1(x3)-2(x4)=-3
   1(x1)-7(x2)+6(x4)=5
   -1(x1)+7(x2)-4(x3)+2(x4)=7
 ```
  Input values for each row should be splitted by space. For instance, entering first row of above example is:
 ```
 0 0 1 -2
 ```
 The rule of entering constant values is the same as entering coefficients. 
  
  - Output
  ```
  Given Matrix:
  [[ 0.  0.  1. -2. -3.]
   [ 1. -7.  0.  6.  5.]
   [-1.  7. -4.  2.  7.]]
  x1 is (5.0+-7.0+6.0)
  x2 is free
  x3 is (-3.0+-2.0)
  x4 is free
  ```
  
  ## Shadow
  In this mini-project, the attempt is to create a shadow for an object in a picture, using `shear transformation`. Here are the steps of shadow creation:
  1. Making a matrix of input image by saving its pixels values
  2. Changing the color of objects of input image to gray and saving the results as a new matrix
  3. Using shear transformation on the matrix of gray picture to make shadow and saving the results in a new matrix
  4. Making final image by mixing the results of step 1 and step 3
  
 - Final Result of [This Image](https://github.com/tanya-jp/LinearAlgebra/blob/main/Shadow%20Test.JPG)
<p align="left">
    <img src="https://user-images.githubusercontent.com/72709191/195399219-8f655b3f-49e8-490c-83f5-d4ef391f70ff.png" width=55% height=55% />
</p>

## Regression
This mini-project aims to forecast the open values of the last 10 rows of [GOOGL.csv](https://github.com/tanya-jp/LinearAlgebra/blob/main/GOOGL.csv), using `linear regression` and `polynomial regression`. After the prediction the error is calculated and the figure of actual values and forecasted ones is shown.
- Output Figure
<p align="left">
   <img src="https://user-images.githubusercontent.com/72709191/195385249-15a0d8b4-58e9-4ce9-aa1e-c02071424a9d.png" width=60% height=60% />
</p>

## Noise Reduction
This mini-project is based on the fact that `SVD` reduces the noises of received signals and images. The `SVD` process should be applied on each R, G, and B matrix of the input image to reduce the noises of [the Noisy Image](https://github.com/tanya-jp/LinearAlgebra/blob/main/noisy.jpg). `Numpy` is used to find the values of S, V and D of each matrix:
```
np.linalg.svd(matrix)
```
It is notable that for having the most possible accurate output, S values need a threshold which in this project is set 1750. After finding new S values, new image which has less noise will be created.
- The Cleaned Image of [the Noisy Image](https://github.com/tanya-jp/LinearAlgebra/blob/main/noisy.jpg)
<p align="left">
   <img src="https://user-images.githubusercontent.com/72709191/195393268-3d9931fd-cea8-4f3b-ad90-d3837ed75dd9.jpeg" width=15% height=15% />
</p>
