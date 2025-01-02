import source.tests.template as template

data = [
    {
        "name": "default",
        "source": "*some bold text*",
        "tokens": [
            ["ASTERISK"],
            ["TEXT", "some bold text"],
            ["ASTERISK"]
        ]
    },
    {
        "name": "double",
        "source": "some text that has *bold* formatting *twice*",
        "tokens": [
            ["TEXT", "some text that has "],
            ["ASTERISK"],
            ["TEXT", "bold"],
            ["ASTERISK"],
            ["TEXT", " formatting "],
            ["ASTERISK"],
            ["TEXT", "twice"],
            ["ASTERISK"],
        ]
    },
    {
        "name": "line_break",
        "source": "some text that has *bold \nformatting* over a line break",
        "tokens": [
            ["TEXT", "some text that has "],
            ["ASTERISK"],
            ["TEXT", "bold "],
            ["NEWLINE"],
            ["TEXT", "formatting"],
            ["ASTERISK"],
            ["TEXT", " over a line break"]
        ]
    }
]

class TestBold(template.TestLexer): pass
template.generate_tests(TestBold, data)