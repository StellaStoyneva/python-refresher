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

def convert_to_datetime(value):
    local = pytz.timezone(value['timezone'])
    naive = datetime.strptime(value['last_transaction'], "%Y-%m-%d %H:%M:%S")
    local_dt = local.localize(naive)

    return local_dt

def get_sorting_criteria(data):
    data = [[v['account']['balance'], convert_to_datetime(v['account'])] for v in data.values()]
    return data

def get_sorted_data(data):
    try:
        sorted_result = sorted(bank_data, key=lambda i: get_sorting_criteria(i), reverse=True)
        print(sorted_result)
    except:
        print("Invalid data")


get_sorted_data(bank_data)
