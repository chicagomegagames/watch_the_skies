game = {
    "type": "object",
    "properties": {
        "location": {"type": "string"},
        "date": {"type": "number", "optional": True},
        "turn": {"type": "number", "optional": True},
    },
    "required": ["location"]
}
