import json

raw_data_path = ''

with open(raw_data_path, 'r') as file:
    raw_data = json.load(file)

event_type = list()
version = list()
event_body = list()
for key in raw_data:
    event_type.append(key['event_type'])
    version.append(key['version'])
    event_body.append(key['event_body'])

list_of_dicts = []
variables = list()
for item in event_body:
    json_dict = json.loads(item)
    list_of_dicts.append(json_dict)
csv_data = ''

for my_dict in list_of_dicts:
    variables.append(my_dict.keys())
check = list(variables)
values_list = [list(keys) for keys in list_of_dicts]
csv_path = 'name_of_csv_file'
values = ''
for i in range(0,20):
    if i == 19:
        values += f'Value {i} \n'
    else:
        values += f'Value {i},'
csv_data=f'event_type,version,{values}'
for i in range(0, len(version)):
    csv_data += str(event_type[i]) + ',' + str(version[i]) + ',' + str(','.join(values_list[i])) + '\n'

with open(csv_path, 'w', newline='\n') as csv_file:
    csv_file.write(csv_data)

