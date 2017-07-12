# Food Image Classification Using Deep Convolutional Neural Networks
In this project we address the problem of automatic identification
of a food type from its image. We fine-tune a pretrained
Caffenet model to classify a data-set of 101 food
categories. The dataset contains 101,000 images. Our system
achieves a top-1 accuracy of 54.92% and a top-5 accuracy
of 77.2%. Our system surpasses the baseline accuracy
50.76% obtained by using hand-crafted features [3]. We
find that our method of adding the HOG and HSV features
to the trained model yields no improvement in accuracy for
the given dataset. Deeper analysis of the layers and the
learned weights show that color and shape specificity are
the major factors for the classification of images in given
dataset. We find that our model learns to capture these color
specific and shape specific features.
