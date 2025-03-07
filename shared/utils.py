import uuid
from datetime import datetime
from copy import deepcopy
from jsonschema import validate, ValidationError

def deep_merge(dict1, dict2):
    result = deepcopy(dict1)
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            dict1[key] = deepcopy(dict2[key])
    return dict1

def format_datetime(dt, format_str='%Y-%m-%d %H:%M:%S'):
    return dt.strftime(format_str)

def validate_schema(data, schema):
    try:
        validate(instance=data, schema=schema)
        return True, None
    except ValidationError as e:
        return False, str(e)

def generate_unique_id(prefix='id'):
    return f"{prefix}_{uuid.uuid4().hex}"
