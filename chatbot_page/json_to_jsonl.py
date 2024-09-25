import os
import json

# 'out_json' 폴더 경로와 'out_jsonl' 폴더 경로 설정
input_folder = os.path.join(os.path.dirname(__file__), 'out_json')
output_folder = os.path.join(os.path.dirname(__file__), 'out_jsonl')

# 'out_jsonl' 폴더 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# out_json 폴더 내 모든 .json 파일 변환
for filename in os.listdir(input_folder):
    if filename.endswith('.json'):
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, filename.replace('.json', '.jsonl'))

        # JSON 파일을 JSONL로 변환
        with open(input_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        
            with open(output_file_path, 'w', encoding='utf-8') as jsonl_file:
                if isinstance(data, list):
                    for item in data:
                        jsonl_file.write(json.dumps(item) + '\n')
                else:
                    jsonl_file.write(json.dumps(data) + '\n')
