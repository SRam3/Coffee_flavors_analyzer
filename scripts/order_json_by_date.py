import json
from datetime import datetime

with open('./data/processed_data/data_cleaned.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def date_key(entry):
    return datetime.strptime(entry['Fecha'], "%d/%m/%Y")

sorted_data = sorted(data, key=date_key)


with open('./data/processed_data/data_sorted.json', 'w', encoding='utf-8') as f:
    json.dump(sorted_data, f, ensure_ascii=False, indent=4)

