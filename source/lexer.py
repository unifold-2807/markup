import re
from token import Token
from lexicon_definitions import LEXICON_DEFINITIONS

# The lexer takes in the source text and produces a list of tokens
class Lexer:
    def __init__(self):
        self.cursor = 0

    def lex(self, source):
        # Move the cursor through the source string
        # Match tokens along the way
        tokens = []
        while self.cursor < len(source):
            is_matched = False
            for kind, pattern in LEXICON_DEFINITIONS.items():
                source_left = source[self.cursor:]
                pattern_match = re.match(pattern, source_left)
                if pattern_match is None:
                    continue
                
                if kind == "TEXT":
                    step = self.lex_text(source_left)
                    content = source_left[:step]
                else:
                    step = pattern_match.span()[1]
                    content = None
                token = Token(kind, content)

                is_matched = True
                tokens.append(token)
                self.cursor += step
                break
            if not is_matched:
                raise ValueError(f"Couldnt Identify the token at {self.cursor}")
        return tokens
    
    # Lexing text is a special case
    # Returns the step that the lexer should take
    def lex_text(self, source):
        # Find the first token in the source
        # Text will span from the beginning to that token
        first_token_index = len(source)
        for kind, pattern in LEXICON_DEFINITIONS.items():
            if kind == "TEXT":
                continue
            
            pattern_match = re.search(pattern, source)
            if pattern_match is None:
                continue
            
            token_index = pattern_match.span()[0]
            if first_token_index > token_index:
                first_token_index = token_index
        return first_token_index