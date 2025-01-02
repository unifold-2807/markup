import source.tests.template as template

data = [
    {
        "name": "default",
        "source": "~some struck through text~",
        "tokens": [
            ["TILDE"],
            ["TEXT", "some struck through text"],
            ["TILDE"]
        ]
    },
    {
        "name": "double",
        "source": "some text that has ~struck through~ formatting ~twice~",
        "tokens": [
            ["TEXT", "some text that has "],
            ["TILDE"],
            ["TEXT", "struck through"],
            ["TILDE"],
            ["TEXT", " formatting "],
            ["TILDE"],
            ["TEXT", "twice"],
            ["TILDE"],
        ]
    },
    {
        "name": "line_break",
        "source": "some text that has ~struck through \nformatting~ over a line break",
        "tokens": [
            ["TEXT", "some text that has "],
            ["TILDE"],
            ["TEXT", "struck through "],
            ["NEWLINE"],
            ["TEXT", "formatting"],
            ["TILDE"],
            ["TEXT", " over a line break"]
        ]
    }
]

class TestStruckThrough(template.TestLexer): pass
template.generate_tests(TestStruckThrough, data)