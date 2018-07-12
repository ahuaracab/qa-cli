# -*- coding: utf-8 -*-

import os
import sys

from lib.log import logger
from lib.exceptions import QACliException
from lib.messages import MSG_STARTING, MSG_ENDING
from lib.messages import MSG_GET_PAYLOAD, MSG_VALIDATE_PAYLOAD
from lib.messages import MSG_GET_FIELDS_PAYLOAD
from lib.validates import validate_fields_in_schema
from lib.config import get_config

def get_fieds_payload():
    return ["code", "message"]

def get_payload():
    payload = {
        "code": 200,
        "message": "Busqueda satisfactoria"
    }
    return payload

def validate_payload(fields, payload):
    validate_fields_in_schema(fields, payload)

def main():

    logger.info(MSG_STARTING)
    try:
        config = get_config()
        
        logger.info(config['app']['name'])
        logger.info(MSG_GET_PAYLOAD)
        payload = get_payload()

        logger.info(MSG_GET_FIELDS_PAYLOAD)
        fields_payload = get_fieds_payload()

        logger.info(MSG_VALIDATE_PAYLOAD)
        validate_payload(fields_payload, payload)
        
    except QACliException as error:
        logger.error(str(error))
    
    logger.info(MSG_ENDING) 

if __name__ == "__main__":
    main()