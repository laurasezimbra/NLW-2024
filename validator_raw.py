from cerberus import Validator

body = {
    "data": {
        "elemento1": 123.45,
        "elemento2": "plau",
        "elemento3": 1
    }
}

body_validator = Validator({
    "data": {
        "type": "dict",
        "schema": {
            "elemento1": { "type": "float", "required": True, "empty": False },
            "elemento2": { "type": "string", "required": True, "empty": True },
            "elemento3": { "type": "string", "required": False, "empty": False }
        }
    }
})

response = body_validator.validate(body)

if response is False:
    print(body_validator.errors)
else:
    print("Body OK")

print(response)
print(body_validator.errors)
