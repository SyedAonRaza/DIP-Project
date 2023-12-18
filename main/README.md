# Dog-Breeds-Image-Classifier
### Use a Pre-trained Image Classifier to Identify Dog Breeds

## Overview
- Using an image classification application using a deep learning model called a convolutional neural network (often abbreviated as CNN). <br>
- Using a CNN that has already learned the features from a giant dataset of 1.2 million images called <b> <a href="https://image-net.org/">ImageNet</a></b>.<br>

- Exploring the three different architectures (AlexNet, VGG, and ResNet) and determining which are best for the application.<br><br>

## Problem
Your city is hosting a citywide dog show and you have volunteered to help the organizing committee with contestant registration. Every participant that registers must submit an image of their dog along with biographical information about their dog. The registration system tags the images based upon the biographical information. Some people are planning on registering pets that aren’t actual dogs. Develop Python classifier to make sure the participants are dogs.<br><br>

## Principal Objectives
1. Correctly identify which pet images are of dogs (even if the breed is misclassified) and which pet images aren't of dogs.<br>

2. Correctly classify the breed of dog, for the images that are of dogs.<br>

3. Determine which CNN model architecture (ResNet, AlexNet, or VGG), "best" achieve objectives 1 and 2.<br><br>

## Directories and files
### Directories
<b>A. pet_images</b>(given), <b>uploaded_images</b>:- Testing data (Images to be classified)

### Files
<b>A. resnet_pet-images.txt(given), resnet_uploaded-images.txt</b> - that contains the results using CNN model architecture ResNet (after classification)<br>
<b>B. alexnet_pet-images.txt(given), alexnet_uploaded-images.txt</b> - that contains the results using CNN model architecture AlexNet (after classification)<br>
<b>C. vgg_pet-images.txt(given), vgg_uploaded-images.txt</b> - that contains the results using CNN model architecture VGG (after classification)<br>
<b>D. run_models_batch, run_models_batch_uploaded</b> - bash program(executes shell commands- Batch Processing)<br><br>

## Execution
To run file run_models_batch.sh in the workspace, open a <i><strong>terminal window (in Unix/Linux/OSX/Lab Workspace)</strong></i> and type the following:
```
sh run_models_batch.sh
```
<strong>Note: </strong>(run_models_batch.bat <b>on Windows</b>)<br><br>

## Observation
Notice that both VGG and AlexNet correctly identify images of "dogs" and "not-a-dog" 100% of the time.
VGG provides the best solution because it classifies the correct breed of dog over 90% of the time.
<img src="https://github.com/Rakshit-26/Dog-Breeds-Image-Classifier-CNN/tree/main/Screenshots/1.png"><br><br>

## Result
Given our results, the "best" model architecture is VGG. It outperformed both of the other architectures when considering both objectives 1 and 2. You will notice that ResNet did classify dog breeds better than AlexNet, but only VGG and AlexNet were able to classify "dogs" and "not-a-dog" at 100% accuracy. The model VGG was the one that was able to classify "dogs" and "not-a-dog" with 100% accuracy and had the best performance regarding breed classification with 93.3% accuracy.<br>