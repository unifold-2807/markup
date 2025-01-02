# Token kinds and their patterns that the lexer can use
LEXICON_DEFINITIONS = {
    "DOUBLE_NEWLINE": r"\n\n",
    "BANG": r"! ?",
    "NEWLINE": r"\n",
    "ASTERISK": r"\*",
    "SLASH": r"/",
    "UNDERSCORE": r"_",
    
    # Text is handled separately by the lexer
    "TEXT": r"([\s\S]+)"
}