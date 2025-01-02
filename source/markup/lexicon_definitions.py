# Token kinds and their patterns that the lexer can use
LEXICON_DEFINITIONS = {
    "MULTI_NEWLINE": r"\n{2,}",
    "BANG": r"! ?",
    "BAR": r"\| ?",
    "TRIPLE_BACKTICK": r"```",
    "HYPHEN": r"- ?",
    "PLUS": r"\+ ?",
    "NEWLINE": r"\n",
    "ASTERISK": r"\*",
    "SLASH": r"/",
    "UNDERSCORE": r"_",
    "TILDE": r"~",
    "BACKTICK": r"`",
    
    # Text is handled separately by the lexer
    "TEXT": r"([\s\S]+)"
}