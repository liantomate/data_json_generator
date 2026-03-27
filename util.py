import os
import json

OUT_PATH: str = "./out/"

def get_content(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
    
def dict_to_json_string(d: dict) -> str:
    return json.dumps(d, ensure_ascii=False, indent=4)

def json_string_to_file(json_string: str, file_path: str):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(json_string)

def generate_folder():
    if not os.path.exists(OUT_PATH):
        os.makedirs(OUT_PATH)
    return OUT_PATH