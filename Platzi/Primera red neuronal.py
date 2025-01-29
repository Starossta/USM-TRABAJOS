import numpy as np
from keras import layers, models
from tensorflow.keras.utils import to_categorical
from keras.datasets import mnist
import matplotlib.pyplot as plt

(train_data, train_data) , (test_data, test_lables)= mnist.load_data()