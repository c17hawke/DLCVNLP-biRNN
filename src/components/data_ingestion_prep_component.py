import tensorflow_datasets as tfds
from src.constants import *
import tensorflow as tf
from src import logging
from src.utils import save_bin

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
        self.train_ds = self.train_ds.shuffle(TRAINING_BUFFER_SIZE).batch(TRAINING_BATCH_SIZE).prefetch(tf.data.AUTOTUNE)
        self.test_ds = self.test_ds.batch(TRAINING_BATCH_SIZE).prefetch(tf.data.AUTOTUNE)
        logging.info(f"datasets are now shufled and batched!")

    def encode_on_training_data(self):
        self.encoder = tf.keras.layers.TextVectorization(max_tokens=TRAINING_VOCAB_SIZE)
        self.encoder.adapt(self.train_ds.map(lambda text, label: text))
        logging.info(f"encoding on traing ds is done!")

    def save_artifacts(self):
        # self._save_encoder()
        # self._save_train_test_ds()
        logging.info(f"artifacts saved successfully!")


    def _save_encoder(self):
        save_bin(data=self.encoder, path="artifacts/encoder.bin")

    def _save_train_test_ds(self):
        save_bin(data=self.train_ds, path="artifacts/train_ds.bin")
        save_bin(data=self.test_ds, path="artifacts/test_ds.bin")