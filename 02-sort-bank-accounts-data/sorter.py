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
            'timezone': 'UTC'
        }
    }
    }
]


def normalize_data(data):
    normalized_data = []
    for i in data:
        for (k, v) in i.items():
            account_dict = v['account']
            new_dict = {
                'name': k,
                'balance': account_dict['balance'],
                'timezone': account_dict['timezone'],
                'last_transaction': account_dict['last_transaction']
            }
            normalized_data.append(new_dict)

    return normalized_data


def denormalize_data(data):
    denormalized_data = [
        {x['name']: {
            'account': {
                'balance': x['balance'],
                'timezone': x['timezone'],
                'last_transaction': x['last_transaction']
            }
        }
        } for x in data
    ]

    return (denormalized_data)


def convert_to_datetime(value):
    local = pytz.timezone(value['timezone'])
    naive = datetime.strptime(value['last_transaction'], "%Y-%m-%d %H:%M:%S")
    local_dt = local.localize(naive)
    value['datetime'] = local_dt

    return value


def get_sorted_data(data):
    try:
        data = normalize_data(data)
        result = [convert_to_datetime(data_entry) for data_entry in data]
        sorted_result = sorted(result, key=lambda i: (
            i['balance'], i['datetime']), reverse=True)
        denormalized_result = denormalize_data(sorted_result)
        print(denormalized_result)
    except:
        print("Invalid data")


get_sorted_data(bank_data)
