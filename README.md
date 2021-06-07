# Python-PROJECT
Face Detection

Introduction

We’ll be using OpenCV, an open source library for computer vision, written in C/C++, that has interfaces in C++, Python and Java. It supports Windows, Linux, MacOS, iOS and Android. Some of our work will also require using Dlib, a modern C++ toolkit containing machine learning algorithms and tools for creating complex software.

Requirements

The first step is to install OpenCV. Run the following command line in your terminal :

pip install opencv-python
Depending on your version, the file will be installed here :

/usr/local/lib/python3.7/site-packages/cv2

Cascade classifier

or namely cascade of boosted classifiers working with haar-like features, is a special case of ensemble learning, called boosting. It typically relies on Adaboost classifiers (and other models such as Real Adaboost, Gentle Adaboost or Logitboost).

Cascade classifiers are trained on a few hundred sample images of image that contain the object we want to detect, and other images that do not contain those images.

How can we detect if a face is there or not ? There is an algorithm, called Viola–Jones object detection framework, that includes all the steps required for live face detection :

Haar Feature Selection, features derived from Haar wavelets
Create integral image
Adaboost Training
Cascading Classifiers
The original paper was published in 2001.

a. Haar Feature Selection
There are some common features that we find on most common human faces :

a dark eye region compared to upper-cheeks
a bright nose bridge region compared to the eyes
some specific location of eyes, mouth, nose…

In this example, the first feature measures the difference in intensity between the region of the eyes and a region across the upper cheeks. The feature value is simply computed by summing the pixels in the black area and subtracting the pixels in the white area.

Then, we apply this rectangle as a convolutional kernel, over our whole image. In order to be exhaustive, we should apply all possible dimensions and positions of each kernel. A simple 24*24 images would typically result in over 160’000 features, each made of a sum/subtraction of pixels values. It would computationally be impossible for live face detection. So, how do we speed up this process ?

once the good region has been identified by a rectangle, it is useless to run the window over a completely different region of the image. This can be achieved by Adaboost.
compute the rectangle features using the integral image principle, which is way faster. We’ll cover this in the next section.

The classifiers are trained using Adaboost and adjusting the threshold to minimize the false rate. When training such model, the variables are the following :

the number of classifier stages
the number of features in each stage
the threshold of each stage
Luckily in OpenCV, this whole model is already pre-trained for face detection.
