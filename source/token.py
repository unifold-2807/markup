from lexicon_definitions import LEXICON_DEFINITIONS

# Tokens are produced by the lexer
class Token:
    def __init__(self, kind, content=None):
        if kind not in LEXICON_DEFINITIONS:
            raise ValueError(f"Token kind '{kind}' is not in the lexicon definitions")
        self.kind = kind
        
        if content is None:
            self.content = content
        else:
            self.content = str(content)
    
    def __repr__(self):
        if self.content is None:
            representation = f"{self.kind}"
        else:
            representation = f"{self.kind} '{self.content}'"
        return representation