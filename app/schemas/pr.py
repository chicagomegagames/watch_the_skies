pr = {
    "type": "object",
    "properties": {
        "delta": {"type": "number"},
        "reason": {"type": "string"},
        "user": {"type": "number"},
        "country": {"type": "number"}
    },
    "required": ["delta", "reason", "user", "country"]
}

pr_request = {
    "type": "object",
    "properties": {
        "country": {"type": "number"}
    },
    "required": ["country"]
}
