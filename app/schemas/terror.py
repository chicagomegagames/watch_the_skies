terror = {
    "type": "object",
    "properties": {
        "delta": {"type": "number"},
        "reason": {"type": "string"},
        "user": {"type": "number"},
        "game": {"type": "number"}
    },
    "required": ["delta", "reason", "user", "game"]
}

terror_request = {
    "type": "object",
    "properties": {
        "game": {"type": "number"}
    },
    "required": ["game"]
}
