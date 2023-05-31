from datetime import datetime

data = {
    'date': '2022/10/18'

}

processors = {
    "date": lambda date_str: datetime.strptime(date_str, "%Y/%m/%d")
}

new_date = {}

for key, value in data.items():
    processor = processors.get(key, None)

    if processor is not None:
        new_value = processor(value)
        new_date[key] = new_value
print(new_date['date'])
