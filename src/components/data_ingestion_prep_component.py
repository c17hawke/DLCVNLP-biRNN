import tensorflow_datasets as tfds
from src.constants import *
import tensorflow as tf
from src import logging

class DataIngestionPreperation:
    def __init__(self,):
        self.dataset_name = "imdb_reviews"

    def load_data(self):
        dataset, info = tfds.load(
                                    name=self.dataset_name, 
                                    with_info=True, 
                                    as_supervised=True)
        self.train_ds, self.test_ds = dataset["train"], dataset["test"]                            
        logging.info(f"{self.dataset_name} dataset dowloaded with info:\n{info}")
        
    def shuffle_and_batch(self):
        pass

    def encode_on_traing_data(self):
        pass

    def save_encoder(self):
        pass

    def save_train_test_ds(self):
        pass