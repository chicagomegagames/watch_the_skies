game_create = {
    "type": "object",
    "properties": {
        "location": {"type": "string"},
        "date": {"type": "number", "optional": True},
        "turn": {"type": "number", "optional": True},
    },
    "required": ["location"]
}

game_id = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
    },
    "required": ["id"]
}
