# ai-ml-algorithms
Algorithms for some ai and ml problems

## Contents

- [UCS](#ucs-algorithm)

- [Backtracking Search](#backtracking-search)

- [Perceptron](#perceptron) (*Multiclass classification with single perceptron)

- [MLP](#mlp)

- [Perceptron2](#perceptron2) (*Modified version 'Perceptron' for mnist dataset)

- [Image_Classification](#image_classification) (*CIFAR10 dataset)

- [GAN](#gan) (*CycleGAN)

- [LSTM](#lstm) 

## UCS-Algorithm
 
Uniform Cost Search (UCS) Algorithm that determines the shortest path between two cities. Dataset added to [/UCS-Algorithm/data](https://github.com/HakkiAkut/ai-ml-algorithms/tree/master/UCS-Algorithm/data) directory.

![cities](https://github.com/HakkiAkut/ai-ml-algorithms/blob/master/UCS-Algorithm/cities.png)

Output

![output-cities](https://user-images.githubusercontent.com/32385870/152206068-1851ff0d-c254-44ef-a1d4-904bf0829988.png)


## Backtracking-Search

Backtracking Search algorithm that colors the map of the South America continent with using plotly package.
![countries](https://github.com/HakkiAkut/ai-ml-algorithms/blob/master/Backtracking-Search/countries.png)

Output

![output](https://user-images.githubusercontent.com/32385870/152212715-726d38a8-e8ff-4d6c-be8f-227dc0e6f32f.png)


## Perceptron

implementing a multiclass classification perceptron and test it on the given "iris.csv" (part 1) and "irismodified.csv" (part 2). Datasets added to [/Perceptron/data](https://github.com/HakkiAkut/ai-ml-algorithms/tree/master/Perceptron/data) directory.

iris.csv dataset has 3 classes, irismodified.csv has 2 classes.


## MLP

implementing a multilayer perceptron which predict car prices with using carprices.csv dataset. Datasets added to [/MLP/data](https://github.com/HakkiAkut/ai-ml-algorithms/tree/master/MLP/data) directory.


## Perceptron2

Implementing single layer perceptron for classifying mnist digit classification dataset. The dataset contains 7000 samples with dimensions of 28x28. [dataset](https://keras.io/api/datasets/mnist/)


## Image_Classification

CIFAR10 dataset image classification with keras sequential. This dataset has 50000 train, 10000 test image. [dataset](https://keras.io/api/datasets/cifar10/)


## GAN

Using Generative Adversarial Network for converting dog images into cat images. CycleGAN is used for this model. The dataset is dog vs cat dataset from kaggle. [dataset](https://www.kaggle.com/c/dogs-vs-cats/rules)


## LSTM

Text recogniton with LSTM models. The dataset is [Spam Text Message Classification](https://www.kaggle.com/team-ai/spam-text-message-classification). Model recognizes that is message spam or ham.
