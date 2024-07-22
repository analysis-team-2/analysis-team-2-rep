import sys
import json
import pandas as pd
from autogluon.tabular import TabularPredictor

def load_model():
    predictor = TabularPredictor.load(r"AutogluonModels\ag-20240713_155155")
    return predictor

def predict(predictor, data):
    df = pd.DataFrame(data)
    predictions = predictor.predict(df)
    return predictions.to_list()

def main():
    input_data = json.load(sys.stdin)
    predictor = load_model()
    result = predict(predictor, input_data)
    json.dump(result, sys.stdout)

if __name__ == '__main__':
    main()

