from flask import Flask
import modin.pandas as pd
import ray




app = Flask(__name__)


@app.route('/', methods=['GET'])
def read_data():
    file_path = "titanic.csv"
    modin_df = pd.read_csv(file_path)
    print(modin_df)
    return "data reading was successful", 200


if __name__ == '__main__':
    ray.init(include_dashboard=False)
    print("ray instance started")
    app.run(port=5050)