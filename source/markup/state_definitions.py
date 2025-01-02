# States that the lexer can be in
# Which states can it transition into
# Which token kinds need to be lexed in order to do so
STATE_DEFINITIONS = {
    "BLOCK": {
        "BLOCK": ["MULTI_NEWLINE", "BANG", "BAR", "NEWLINE"],
        "CODE_BLOCK": ["TRIPLE_BACKTICK"],
        "INLINE_CODE": ["BACKTICK"],
        "INLINE": ["ASTERISK", "SLASH", "UNDERSCORE", "TILDE", "TEXT", "BACKTICK", "NEWLINE", "MULTI_NEWLINE"]
    },
    "CODE_BLOCK": {
        "BLOCK": ["TRIPLE_BACKTICK"],
        "CODE_BLOCK": ["TEXT", "TRIPLE_BACKTICK"]
    },
    "INLINE": {
        "BLOCK": ["MULTI_NEWLINE"],
        "INLINE_CODE": ["BACKTICK"],
        "LINE_BREAK": ["NEWLINE"],
        "INLINE": ["ASTERISK", "SLASH", "UNDERSCORE", "TILDE", "TEXT", "BACKTICK", "NEWLINE", "MULTI_NEWLINE"]
    },
    "INLINE_CODE": {
        "INLINE": ["BACKTICK"],
        "INLINE_CODE": ["NEWLINE", "TEXT", "BACKTICK"]
    },
    "LINE_BREAK": {
        "BLOCK": ["BAR"],
        "INLINE": ["ASTERISK", "SLASH", "UNDERSCORE", "TILDE", "TEXT", "BACKTICK", "NEWLINE", "MULTI_NEWLINE"]
    }
}

DEFAULT_STATE = "BLOCK"