from datetime import datetime
import pytz

bank_data = [
    {'Kevin': {
        'account': {
            'balance': 10000,
            'last_transaction': '2020-12-13 12:00:00',
            'timezone': 'Europe/Vienna'
        }
    }
    },
    {'Peter': {
        'account': {
            'balance': 10400,
            'last_transaction': '2020-12-15 14:30:00',
            'timezone': 'Asia/Singapore'
        }
    }
    },
    {'Dohn': {
        'account': {
            'balance': 1300,
            'last_transaction': '2020-12-12 12:00:00',
            'timezone': 'UTC'
        }
        }
    },
    {'Dave': {
        'account': {
            'balance': 1300,
            'last_transaction': '2020-12-12 12:00:05',
            'timezone': 'UTC',
        }
    }
    }
]

class BancAccountDataSorter:
    def __init__(self, bank_data):
        self.__bank_data = bank_data
    
    def get_bank_data(self):
        return self.__bank_data
    
    def set_bank_data(self, data):
        self.__bank_data = data
        
    def __convert_to_datetime(self, value):
        local = pytz.timezone(value['timezone'])
        naive = datetime.strptime(value['last_transaction'], "%Y-%m-%d %H:%M:%S")
        local_dt = local.localize(naive)

        return local_dt

    def __get_sorting_criteria(self, data):
        data = [[v['account']['balance'], self.__convert_to_datetime(v['account'])] for v in data.values()]
        return data

    def get_sorted_data(self):
        bank_data = self.get_bank_data()
        try:
            sorted_result = sorted(bank_data, key=lambda i: self.__get_sorting_criteria(i), reverse=True)
            self.set_bank_data(sorted_result)
        
        except Exception:
            raise Exception("Invalid data") 

bank_account_sorter = BancAccountDataSorter(bank_data)
bank_account_sorter.get_sorted_data()
sorted_data = bank_account_sorter.get_bank_data()
print(sorted_data)
