import source.tests.template as template

data = [
    {
        "name": "default",
        "source": "A paragraph.",
        "tokens": [
            ["TEXT", "A paragraph."]
        ]
    },
    {
        "name": "line_break",
        "source": "A paragraph with a \nline break.",
        "tokens": [
            ["TEXT", "A paragraph with a "],
            ["NEWLINE"],
            ["TEXT", "line break."]
        ]
    },
    {
        "name": "double_line_break",
        "source": "A paragraph with \ntwo whole \nline breaks.",
        "tokens": [
            ["TEXT", "A paragraph with "],
            ["NEWLINE"],
            ["TEXT", "two whole "],
            ["NEWLINE"],
            ["TEXT", "line breaks."]
        ]
    },
    {
        "name": "double",
        "source": "A paragraph.\n\nAn another paragraph.",
        "tokens": [
            ["TEXT", "A paragraph."],
            ["MULTI_NEWLINE"],
            ["TEXT", "An another paragraph."]
        ]
    },
    {
        "name": "inline_formattings",
        "source": "A paragraph that has inline formattings: *bold*, /italicized/, _underlined_.",
        "tokens": [
            ["TEXT", "A paragraph that has inline formattings: "],
            ["ASTERISK"],
            ["TEXT", "bold"],
            ["ASTERISK"],
            ["TEXT", ", "],
            ["SLASH"],
            ["TEXT", "italicized"],
            ["SLASH"],
            ["TEXT", ", "],
            ["UNDERSCORE"],
            ["TEXT", "underlined"],
            ["UNDERSCORE"],
            ["TEXT", "."]
        ]
    }
]

class TestParagraph(template.TestLexer): pass
template.generate_tests(TestParagraph, data)