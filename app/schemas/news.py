post_article = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "author": {"type": "string"},
        "organization": {"type": "string"},
        "body": {"type": "string"},
        "turn": {"type": "number"},
        "game": {"type": "number"},
        "user": {"type": "number"}
    },
    "required": ["title", "author", "organization", "body", "turn", "game", "user"]
}

get_articles= {
    "type": "object",
    "properties": {
        "game": {"turn": "game"},
        "turn": {"turn": "number"}
    },
    "required": ["turn"]
}
