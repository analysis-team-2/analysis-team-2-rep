import pandas as pd
from autogluon.timeseries import TimeSeriesPredictor, TimeSeriesDataFrame
import argparse
import warnings
import logging

warnings.filterwarnings("ignore")
warnings.filterwarnings("ignore", category=UserWarning, module='statsforecast.arima')

logging.getLogger("autogluon").setLevel(logging.CRITICAL)
logging.getLogger("autogluon.core").setLevel(logging.CRITICAL)
logging.getLogger("autogluon.timeseries").setLevel(logging.CRITICAL)
logging.getLogger("statsforecast").setLevel(logging.CRITICAL)

def load_and_predict(model_name, item_id):
    # 모델 경로 설정
    model_paths = {
        '광명시': 'models/merged_data_gm',
        '시흥시': 'models/merged_data_sh',
        '수원시': 'models/merged_data_sw',
        '안양시': 'models/merged_data_yy',
        '화성시': 'models/merged_data_hs'
    }
    
    if model_name not in model_paths:
        raise ValueError("Invalid model name provided.")
    
    model_path = model_paths[model_name]
    print(model_path)
    # 모델 로드
    predictor = TimeSeriesPredictor.load(model_path)
    
    # 데이터 로드 및 변환
    file_path = "./train_data_time.csv"
    df = pd.read_csv(file_path)
    df = TimeSeriesDataFrame.from_data_frame(
        df,
        id_column="item_id",
        timestamp_column="timestamp"
    )
    
    # 예측 수행
    predictions = predictor.predict(df)
    
    # 2024-07-01부터 끝까지의 결과 필터링
    predictions = predictions.loc[item_id, ['mean']].reset_index()
    predictions = predictions[predictions['timestamp'] >= '2024-07-01']
    
    return predictions

def main():
    parser = argparse.ArgumentParser(description="Time series prediction script.")
    parser.add_argument("model_name", type=str, help="The name of the model to use.")
    parser.add_argument("item_id", type=str, help="The item ID to predict.")
    
    args = parser.parse_args()
    
    # 예측 수행
    predictions = load_and_predict(args.model_name, args.item_id)
    
    # 예측 결과를 JSON 형식으로 변환 및 출력
    predictions_json = predictions.to_json(orient='records', date_format='iso')
    print(predictions_json)

if __name__ == "__main__":
    main()
