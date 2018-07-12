# -*- coding: utf-8 -*-
from .exceptions import QACliException
from .messages import MSG_FIELD_DOES_NOT_EXIST as MSG_ERROR_VALIDATE_FIELD
from .config import get_config
from .log import logger

CONFIG =  get_config()

def validate_code_response_200(code):
    if code != 200: 
        raise QACliException("Error: el codigo de respuesta debe ser 200")

def validate_if_have_field(field, schema):
    if not field in schema:
       raise QACliException(MSG_ERROR_VALIDATE_FIELD.format(field))

def validate_fields_in_schema(fields, schema):
    for field in fields:
        validate_if_have_field(field, schema)