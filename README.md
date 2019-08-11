# CNN-on-MNIST-dataset
Here we try to use Convolutional Neural networks to make accurate predictions for hand written dataset

## Dependencies
1. Numpy
2. Pandas
3. Tensorflow (keras is included in Tensorflow)
4. Matplotlib

## How to use:

Download Hand]written digit's dataset from https://www.kaggle.com/c/3004/download-all
Change the address to train and test data in line 7,8 in **final-code.py**.
Run the file using **python 3**(this code won't run in Python 2)

## Score on Kaggle

0.82328

you can check the score here also: https://www.kaggle.com/c/digit-recognizer/submissions

## Conclusion

We didn't achive highest score, but that is obvious because We didn't fine-tune our model enough.
Also It is to kept in mind the there'll always be trade-off between computing cost and performance.
If you intend to use this code to achieve higher accuracy you can use Grid Search or Randomized Search as mentioned in jupyter-notebook.
