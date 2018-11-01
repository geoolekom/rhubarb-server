import time
from rhubarb import task


@task(name='multiply', json_schema={'type': 'object',
'properties': {
   'operands': {'type': 'array',
                'minItems': 1,
                'items': {'type': 'number'}}
},
'required': ['operands']})
def multiply(operands):
    res = 1
    for op in operands:
        res *= op
    time.sleep(5)
    return res
