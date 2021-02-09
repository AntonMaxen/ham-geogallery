from pathlib import Path
import decimal
import datetime


def get_project_root():
    return Path(__file__).parent.parent.parent


def print_dict(my_dict):
    for key, value in my_dict.items():
        print(f'{key}: {value}')


def print_dicts(my_dicts, sep='-', amount=20):
    for my_dict in my_dicts:
        print_dict(my_dict)
        print(sep * amount)


def make_list_of_dicts_jsonable(list_of_dicts):
    return [make_dict_jsonable(my_dict) for my_dict in list_of_dicts]


def make_dict_jsonable(my_dict):
    new_dict = {}
    for k, v in my_dict.items():
        if isinstance(v, decimal.Decimal):
            insert_value = float(str(v))
        elif isinstance(v, datetime.date):
            insert_value = str(v)
        else:
            insert_value = v

        new_dict[k] = insert_value

    return new_dict
