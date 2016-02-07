user_create = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "email": {"type": "string"},
        "position": {"type": "string"},
        "game": {"type": "number"}
    },
    "required": ["name", "email", "position", "game"]
}

user_id = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
    },
    "required": ["id"]
}
