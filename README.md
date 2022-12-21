# MFCC-emo

The purpose of this project was to compare performance of different models in task of speech emotion recognition based on the acoustic characteristics of an audio recording.


## Installation

To install required packages, run the following line in terminal:

```shell
pip install -r requirements.txt
```


## Dataset

The audio recordings were self-produced and involved eight speakers. Each of them was asked to read the same text in five different ways - expressing five different emotions (neutral state, joy, sadness, anger, and fear). Whole process was based on the Stanislavski method.

The recordings were then processed and Mel-Frequency Cepstral Coefficients (MFCCs) were extracted. The parameters were chosen to reflect the natural response of the human auditory system to stimulation by speech.

In the end, 1985 samples were obtained, from which $80%$ were put into the training set and the remaining $20%$ into the test set.

| id | Emotion | Training | Test | Sum |
| -- | ------- | -------- | ---- | --- |
| 0  | anger   | 326      | 62   | 388 |
| 1  | fear    | 388      | 97   | 485 |
| 2  | joy     | 260      | 90   | 350 |
| 3  | neutral | 294      | 71   | 365 |
| 4  | sadness | 320      | 77   | 391 |


## Solutions

### Naive Bayes Classifier
Naive Bayes Classifier is a probabilistic classifier indicating the class with the highest probability.

### Decision Tree
Decision Tree is a representation in which the nodes are attributes and the leaves are the class of observations. For the model, the `log_loss` criterion and the maximum number of features equal to $\log_2(n)$, where $n$ is the number of all features.

### $k$ Nearest Neighbours
kNN is a classifier that determines a given number of neighbors to which a given observation has the shortest distance. In this case, $k=5$.

### Random Forest
Random Forest is a classifier built from multiple decision trees based on randomly selected learning data sets. As with the decision tree, a `log_loss` criterion and a maximum number of features equal to $\log_2(n)$ were assumed, where $n$ is the number of all features.

### Gradient Boosting
Gradient Boosting is a model built in a stepwise manner, also based on decision trees. Again, the `log_loss` criterion is applied.

### Multi-Layer Perceptron
Multilayer perceptron is an artificial neural network consisting of an input layer, an output layer and hidden layers. In this case, it was decided to use ReLU activation function, ADAM optimizer and L2 regularization with $\alpha=0.1$.


## Evaluation

The accuracy, precision, recall and F1-score metrics were used for evaluation. The results are presented in the table below.

| Classifier             | Accuracy | Precision | Recall | F1 score |
| ---------------------- | -------- | --------- | ------ | -------- |
| Naive Bayes            | $47.36\%$ | $47.3\%$ | $48.4\%$ | $47.28\%$ |
| Decision Tree          | $44.33\%$ | $44.53\%$ | $44.88\%$ | $44.5\%$ |
| $k$ Nearest Neighbours | $60.2\%$ | $61.43\%$ | $60.83\%$ | $60.8\%$ |
| Random Forest          | $\mathbf{65.99\%}$ | $66.91\%$ | $\mathbf{66.66\%}$ | $\mathbf{66.5\%}$ |
| Gradient Boosting      | $60.96\%$ | $61.41\%$ | $61.68\%$ | $61.29\%$ |
| Multi-Layer Perceptron | $57.68\%$ | $\mathbf{69.07\%}$ | $57.94\%$ | $54.09\%$ |