from src.utils import save_bin
import time
from src import logging
from src.constants import *
from src.components import DataIngestionPreperation


STAGE = "Data ingestion and preparation" ## <<< change stage name 

def main():
    data_ing_prep_obj = DataIngestionPreperation()
    data_ing_prep_obj.load_data()
    data_ing_prep_obj.shuffle_and_batch()
    data_ing_prep_obj.encode_on_training_data()
    # data_ing_prep_obj.save_artifacts()
    save_bin(data_ing_prep_obj, "artifacts/data_ing_prep.bin")

if __name__ == '__main__':
    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main()
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e