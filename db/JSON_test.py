import datetime
import json

data = {
    'string': 'hello world',
    'integer': 5,
    'lst': ['thinkpad', 'apple'],
    'birthday': datetime.datetime.now(),
    'date': datetime.date(1988, 1, 15)
}


# with open('data/data_json.json', 'w') as file:
#     json.dump(data, file, indent=4)
#
#
# with open('data/data_json.json', 'r') as f:
#     content = json.load(f)
#     print(content)

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return {
                "value": obj.strftime('%d/%m/%y %H:%M:%S'),
                "__datetime__": True
            }
        if isinstance(obj, datetime.date):
            return {
                "value": obj.strftime('%d/%m/%y'),
                "__date__": True
            }
        return super().default(obj)


with open('data/datetime.json', 'w') as file:
    json.dump(data, file, cls=DateEncoder, indent=4)


def as_datetime(dct):
    if '__datetime__' in dct:
        return datetime.datetime.strptime(dct['value'], '%d/%m/%y %H:%M:%S')
    if '__date__' in dct:
        return datetime.datetime.strptime(dct["value"], '%d/%m/%y').date()
    return dct


with open('data/datetime.json') as f:
    cont = json.load(f, object_hook=as_datetime)
    print(cont)
