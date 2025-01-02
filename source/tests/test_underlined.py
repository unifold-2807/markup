import source.tests.template as template

data = [
    {
        "name": "default",
        "source": "_some underlined text_",
        "tokens": [
            ["UNDERSCORE"],
            ["TEXT", "some underlined text"],
            ["UNDERSCORE"]
        ]
    },
    {
        "name": "double",
        "source": "some text that has _underlined_ formatting _twice_",
        "tokens": [
            ["TEXT", "some text that has "],
            ["UNDERSCORE"],
            ["TEXT", "underlined"],
            ["UNDERSCORE"],
            ["TEXT", " formatting "],
            ["UNDERSCORE"],
            ["TEXT", "twice"],
            ["UNDERSCORE"],
        ]
    },
    {
        "name": "line_break",
        "source": "some text that has _underlined \nformatting_ over a line break",
        "tokens": [
            ["TEXT", "some text that has "],
            ["UNDERSCORE"],
            ["TEXT", "underlined "],
            ["NEWLINE"],
            ["TEXT", "formatting"],
            ["UNDERSCORE"],
            ["TEXT", " over a line break"]
        ]
    }
]

class TestUnderlined(template.TestLexer): pass
template.generate_tests(TestUnderlined, data)