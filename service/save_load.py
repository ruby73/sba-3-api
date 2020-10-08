import model
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
import numpy as np
import tensorflow as tf 
import util.version_checker

class SaveLoad():

    train_images : object = None
    train_label : object = None 
    test_images : object = None
    test_label : object = None

    def __init__(self):
        util.version_checker.env_info()

    def hook(self):
        self.get_data()
        self.create_model()
        self.train_model()
        self.eval_model()

    def get_data(self):
        pass

    def create_model(self):
        self.model = tf.keras.models.Sequential()
        self.model.compile()

    def train_model(self):
        self.model.fit()
    
    def save_model(self):
        pass
    def load_model(self):
        pass

    def debug_model(self):
        print(f'모델 정보: {self.model.summary()}')