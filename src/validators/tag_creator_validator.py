from cerberus import Validator
from src.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntityerror

def tag_creator_validator(request: any) -> None:
    body_validator = Validator({
        "product_code": { "type": "string", "required": True, "empty": False }
    })

    response = body_validator.validate(request.json)
    if response is False:
        raise HttpUnprocessableEntityerror(body_validator.errors)
