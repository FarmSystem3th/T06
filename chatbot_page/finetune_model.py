from openai import OpenAI
import os

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY1")
client = OpenAI(api_key='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', timeout=60)

# 'out_jsonl' 폴더 경로 설정
folder_path = os.path.join(os.path.dirname(__file__), 'out_jsonl')

# 업로드할 파일 목록 가져오기
jsonl_files = [f for f in os.listdir(folder_path) if f.endswith('.jsonl')]

# 파일 업로드 및 업로드된 파일 ID 저장
uploaded_file_ids = []

for jsonl_file in jsonl_files:
    file_path = os.path.join(folder_path, jsonl_file)
    
    try:
        # 파일을 이진 모드로 열기
        with open(file_path, 'rb') as file_data:
            # 파일을 OpenAI API로 업로드
            file_response = client.files.create(file=file_data, purpose='fine-tune')
            # FileObject의 속성으로 접근
            uploaded_file_ids.append(file_response.id)  # 파일 ID 저장
            print(f"파일 업로드 성공: {jsonl_file}, 파일 ID: {file_response.id}")
    except Exception as e:
        print(f"파일 업로드 실패: {jsonl_file}, 오류: {str(e)}")

# 업로드된 파일로 파인튜닝 작업 시작
if uploaded_file_ids:
    for file_id in uploaded_file_ids:
        try:
            fine_tune_response = client.fine_tuning.jobs.create(
                training_file=file_id,  # 업로드된 학습 파일 ID 사용
                model="gpt-4o-2024-08-06"  # 파인튜닝할 모델 지정
            )
            print(f"파인튜닝 작업 시작: {fine_tune_response}")
        except Exception as e:
            print(f"파인튜닝 작업 생성 실패: {str(e)}")
else:
    print("업로드된 파일이 없습니다.")
    
