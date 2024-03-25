import pint 
from django.core.exceptions import ValidationError
from pint.errors import UndefinedUnitError

def validators_for_unit(value):
    unit_db=pint.UnitRegistry()
    try:
        unit_db[value]
    except UndefinedUnitError as e:
        raise ValidationError(f'{value} is not a valid unit of measurement.')

    except:
        raise ValidationError(f'{value} is invalid.')