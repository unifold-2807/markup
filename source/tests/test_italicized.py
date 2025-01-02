import source.tests.template as template

data = [
    {
        "name": "default",
        "source": "/some italicized text/",
        "tokens": [
            ["SLASH"],
            ["TEXT", "some italicized text"],
            ["SLASH"]
        ]
    },
    {
        "name": "double",
        "source": "some text that has /italicized/ formatting /twice/",
        "tokens": [
            ["TEXT", "some text that has "],
            ["SLASH"],
            ["TEXT", "italicized"],
            ["SLASH"],
            ["TEXT", " formatting "],
            ["SLASH"],
            ["TEXT", "twice"],
            ["SLASH"],
        ]
    },
    {
        "name": "line_break",
        "source": "some text that has /italicized \nformatting/ over a line break",
        "tokens": [
            ["TEXT", "some text that has "],
            ["SLASH"],
            ["TEXT", "italicized "],
            ["NEWLINE"],
            ["TEXT", "formatting"],
            ["SLASH"],
            ["TEXT", " over a line break"]
        ]
    }
]

class TestItalicized(template.TestLexer): pass
template.generate_tests(TestItalicized, data)