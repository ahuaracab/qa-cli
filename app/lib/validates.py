# -*- coding: utf-8 -*-
from .exceptions import QACliException
from .messages import MSG_FIELD_DOES_NOT_EXIST as MSG_ERROR_VALIDATE_FIELD

def validate_if_have_field(field, schema):
    if not field in schema:
       raise QACliException(MSG_ERROR_VALIDATE_FIELD.format(field))

def validate_fields_in_schema(fields, schema):
    for field in fields:
        validate_if_have_field(field, schema)