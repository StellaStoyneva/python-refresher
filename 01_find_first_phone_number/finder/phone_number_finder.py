from process_regex_mixin import ProcessRegexMixIn
from data import phonebook_data, pattern

'''
matches = ['0888463789', '052 62-47-72', '+359 32 267453', '(032) 21 18 28']
get_phonebook_value({'name': 'John Doe', 'phones': '0888463789 / /032/ 26 74 27'})=> 'John Doe'
print_result(John Doe - 0888463789)
'''

class PhoneNumberFinder(ProcessRegexMixIn):
    def __init__(self, phonebook_data):
        self.__phonebook_data = phonebook_data
        self.__matches = []
    
    def get_phonebook_data(self):
        return self.__phonebook_data
    
    def set_phonebook_data(self, data):
        if(not data['name'] or not data['phones'] or len(data.keys())!=2):
            print('Invalid data format')
            exit()
        self.__phonebook_data = data

    def get_matches(self):
        return self.matches
    
    def set_matches(self, pattern):
        matches = [ProcessRegexMixIn.find_first_match(x['phones'], pattern) for x in self.__phonebook_data if ProcessRegexMixIn.find_first_match(x['phones'], pattern)]
        self.__matches = matches
        

    def __get_phonebook_value(self, key, value ):
        return self.__phonebook_data[self.__matches.index(value)][key]

    def get_result(self, pattern):
        try:
            self.set_matches(pattern)
            result = [f'{self.__get_phonebook_value("name", x)} - {x}' for x in self.__matches if x in self.__get_phonebook_value('phones', x)]
            return result
        except:
            raise Exception("Invalid data format")

phones = PhoneNumberFinder(phonebook_data)

result = phones.get_result(pattern)

[print(x) for x in result] if isinstance(result, list)  else print(result)