# States that the lexer can be in
# Which states can it transition into
# Which token kinds need to be lexed in order to do so
STATE_DEFINITIONS = {
    "BLOCK": {
        "BLOCK": ["MULTI_NEWLINE", "BANG"],
        "INLINE": ["ASTERISK", "SLASH", "UNDERSCORE", "TILDE", "TEXT"]
    },
    "INLINE": {
        "BLOCK": ["MULTI_NEWLINE"],
        "INLINE": ["NEWLINE", "ASTERISK", "SLASH", "UNDERSCORE", "TILDE", "TEXT"]
    }
}

DEFAULT_STATE = "BLOCK"