from flask import Flask
import modin.pandas as pd
import ray
#from ray import logger
import logging

logger = logging.getLogger("ray")
ray_data_logger = logging.getLogger("ray.data")
ray_tune_logger = logging.getLogger("ray.tune")
ray_rllib_logger = logging.getLogger("ray.rllib")
ray_train_logger = logging.getLogger("ray.train")
ray_serve_logger = logging.getLogger("ray.serve")
logger.handlers.clear()
ray_data_logger.handlers.clear()
ray_tune_logger.handlers.clear()
ray_rllib_logger.handlers.clear()
ray_serve_logger.handlers.clear()
ray_train_logger.handlers.clear()
#logger.addHandler(logging.FileHandler('ray_logs.log',mode="w"))


app = Flask(__name__)


@app.route('/read_data', methods=['GET'])
def read_data():
    file_path = "titanic.csv"
    modin_df = pd.read_csv(file_path)
    print(modin_df)
    return "data reading was successful", 200


if __name__ == '__main__':
    ray.init(include_dashboard=False)
    print("ray instance started")
    app.run(port=5050)