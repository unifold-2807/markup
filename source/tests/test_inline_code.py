import source.tests.template as template

data = [
    {
        "name": "default",
        "source": "`some inline code text`",
        "tokens": [
            ["BACKTICK"],
            ["TEXT", "some inline code text"],
            ["BACKTICK"]
        ]
    },
    {
        "name": "double",
        "source": "some text that has `inline code` formatting `twice`",
        "tokens": [
            ["TEXT", "some text that has "],
            ["BACKTICK"],
            ["TEXT", "inline code"],
            ["BACKTICK"],
            ["TEXT", " formatting "],
            ["BACKTICK"],
            ["TEXT", "twice"],
            ["BACKTICK"],
        ]
    },
    {
        "name": "line_break",
        "source": "some text that has `inline code \nformatting` over a line break",
        "tokens": [
            ["TEXT", "some text that has "],
            ["BACKTICK"],
            ["TEXT", "inline code "],
            ["NEWLINE"],
            ["TEXT", "formatting"],
            ["BACKTICK"],
            ["TEXT", " over a line break"]
        ]
    },
    {
        "name": "bold",
        "source": "*`some inline code text that is also bold`*",
        "tokens": [
            ["ASTERISK"],
            ["BACKTICK"],
            ["TEXT", "some inline code text that is also bold"],
            ["BACKTICK"],
            ["ASTERISK"]
        ]
    },
    {
        "name": "marks",
        "source": "`some inline code text that has marks: #, *, /, _, ~`",
        "tokens": [
            ["BACKTICK"],
            ["TEXT", "some inline code text that has marks: #, *, /, _, ~"],
            ["BACKTICK"]
        ]
    },
]

class TestInlineCode(template.TestLexer): pass
template.generate_tests(TestInlineCode, data)