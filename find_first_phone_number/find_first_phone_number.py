import re

phonebook_data = [
    {'name': 'John Doe', 'phones': '0888463789 / /032/ 26 74 27'}, 
    {'name': 'Corey Lee', 'phones': '052 62-47-72 | 003590988371591'}, 
    {'name': 'Reece Russell', 'phones': 'every working day +359 32 267453; supervisor +359889-463789'}, 
    {'name': 'James Thomas', 'phones': ' (032) 21 18 28'}, 
    {'name': 'Zac Lawrence', 'phones': '---'}
   ]

pattern = r'[\+\(]?\d{3}[\)]?[\d\s\-]+\b'


def get_phone_number_matches(input_data):
    matches = re.search(pattern, input_data)
    if(matches):
        return matches.group()


matches = [get_phone_number_matches(x['phones']) for x in phonebook_data if get_phone_number_matches(x['phones'])]


def get_phonebook_value(key, value ):
    return phonebook_data[matches.index(value)][key]


def print_result():
    l = [print(f'{get_phonebook_value("name", x)} - {x}') for x in matches if x in get_phonebook_value('phones', x)]


print_result()
