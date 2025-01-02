import unittest
from source.markup.lexer import Lexer
from source.markup.token import Token

class TestLexer(unittest.TestCase):
    def setUp(self):
        self.lexer = Lexer()

# Generate tests dynamically
def generate_tests(case, data):
    for configuration in data:
        name, source, tokens = configuration.values()
        tokens = [Token(*token) for token in tokens]
        def test(self, source=source, tokens=tokens):
            lexed = self.lexer.lex(source)
            self.assertEqual(tokens, lexed)
        setattr(case, f"test_{name}", test)
        