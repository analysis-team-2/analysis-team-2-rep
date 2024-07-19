import json
import sys
import pandas as pd
import io
from autogluon.tabular import TabularDataset, TabularPredictor

def main():
    # 표준 입력으로부터 JSON 데이터 읽기
    input_data = sys.stdin.read()

    try:
        data = json.loads(input_data)

        # JSON 데이터를 DataFrame으로 변환
        df_predict = pd.DataFrame(data)
        df_predict = TabularDataset(df_predict)
        # 운영점포평균영업기간의 값만 조회
        operating_avg_period = df_predict['store_avg_period'].values[0]
        predictor2 = TabularPredictor.load(r"ag-20240715_073451")
        y_pred = predictor2.predict(df_predict.drop(columns=['amt']))
        
        # 결과를 JSON 형태로 반환
        result = {
            "status": "success",
            "actual_value": 365433405,  # 실제값 (예시로 입력)
            "predicted_value": y_pred.iloc[0]  # numpy.int64 -> 기본 데이터 타입으로 변환
        }
    except Exception as e:
        result = {
            "status": "error",
            "message": str(e)
        }

    # 결과를 JSON 형태로 표준 출력
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False))

if __name__ == "__main__":
    main()



