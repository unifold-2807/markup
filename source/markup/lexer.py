import re
from source.markup.token import Token
from source.markup.lexicon_definitions import LEXICON_DEFINITIONS
from source.markup.state_definitions import STATE_DEFINITIONS, DEFAULT_STATE

# The lexer takes in the source text and produces a list of tokens
class Lexer:
    def __init__(self):
        self.cursor = 0
        self.state = DEFAULT_STATE

    def lex(self, source):
        # Move the cursor through the source string
        # Match tokens along the way
        tokens = []
        while self.cursor < len(source):
            source_left = source[self.cursor:]
            
            state, step, token = self.advance(source_left).values()
            self.state = state
            self.cursor += step
            tokens.append(token)
        return tokens
    
    # Indentify the next token and state
    def advance(self, source):
        transitions = STATE_DEFINITIONS[self.state]
        for state, lexicon in transitions.items():
            identified = self.identify_token(lexicon, source)
            if identified is None:
                continue
            
            return {"state": state, "step": identified["step"], "token": identified["token"]}

        # If no match was found
        raise ValueError(f"Couldnt identify the token at index {self.cursor}")
      
    # Identify the next token using a given lexicon
    def identify_token(self, lexicon, source):
        # Iterate through token kinds to see which matches
        for kind in lexicon:
            pattern = LEXICON_DEFINITIONS[kind]
            pattern_match = re.match(pattern, source)
            if pattern_match is None:
                continue
            
            if kind == "TEXT":
                text_source = pattern_match.group(1)
                step = self.indentify_text(lexicon, text_source)
                content = source[:step]
            else:
                step = pattern_match.span()[1]
                content = None
            token = Token(kind, content)

            return {"step": step, "token": token}
        
        # If no token was found
        return None
    
    # Identifying text is a special case
    # Returns the step that the cursor should take
    def indentify_text(self, lexicon, source):
        # Find the first token in the source
        # Text will span from the beginning to that token
        first_token_index = len(source)
        for kind in lexicon:
            if kind == "TEXT":
                continue
            
            pattern = LEXICON_DEFINITIONS[kind]
            pattern_match = re.search(pattern, source)
            if pattern_match is None:
                continue
            
            token_index = pattern_match.span()[0]
            if first_token_index > token_index:
                first_token_index = token_index
        return first_token_index