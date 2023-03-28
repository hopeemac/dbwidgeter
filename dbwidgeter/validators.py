from pydantic import validator


def parse_string_to_list(str_list):
    if str_list in ['', None]:
        return None
    elif type(str_list) == list:
        return str_list
    else:
        str_list = str_list.strip()
        return [x.strip() for x in str_list.split(',')]


def validate_parse_string_to_list(field_name: str):
    return validator(field_name, allow_reuse=True, pre=True)(lambda v: parse_string_to_list(v))


def confirm_in_list(value, allowed_set):
    if value not in allowed_set:
        raise ValueError(f"Field value must be in {allowed_set}, value was {value}")
    return value


# https://github.com/pydantic/pydantic/discussions/2938
def validate_confirm_in_list(field_name: str, allowed_set: list):
    return validator(field_name, allow_reuse=True)(lambda v: confirm_in_list(v, allowed_set))


def convert_empty_string_to_none(value):
    if value == '':
        return None
    else:
        return value


def convert_all_empty_strings_to_none():
    return validator('*', allow_reuse=True, pre=True)(convert_empty_string_to_none)