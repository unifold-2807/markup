import source.tests.template as template

data = [
    {
        "name": "paragraph",
        "source": "| A paragraph inside a blockquote.",
        "tokens": [
            ["BAR"],
            ["TEXT", "A paragraph inside a blockquote."]
        ]
    },
    {
        "name": "heading",
        "source": "| ! A heading inside a blockquote",
        "tokens": [
            ["BAR"],
            ["BANG"],
            ["TEXT", "A heading inside a blockquote"]
        ]
    },
    {
        "name": "nested",
        "source": "| | A nested blockquote",
        "tokens": [
            ["BAR"],
            ["BAR"],
            ["TEXT", "A nested blockquote"]
        ]
    },
    {
        "name": "line break",
        "source": "| A paragraph that has a \n| line break.",
        "tokens": [
            ["BAR"],
            ["TEXT", "A paragraph that has a "],
            ["NEWLINE"],
            ["BAR"],
            ["TEXT", "line break."]
        ]
    },
    {
        "name": "inline_formattings",
        "source": "| A paragraph that has inline formattings: *bold*, /italicized/, _underlined_, ~struck through~, `inline code`.",
        "tokens": [
            ["BAR"],
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
            ["TEXT", ", "],
            ["TILDE"],
            ["TEXT", "struck through"],
            ["TILDE"],
            ["TEXT", ", "],
            ["BACKTICK"],
            ["TEXT", "inline code"],
            ["BACKTICK"],
            ["TEXT", "."]
        ]
    },
    {
        "name": "double_paragraph",
        "source": "| A paragraph.\n| \n| An another paragraph.",
        "tokens": [
            ["BAR"],
            ["TEXT", "A paragraph."],
            ["NEWLINE"],
            ["BAR"],
            ["NEWLINE"],
            ["BAR"],
            ["TEXT", "An another paragraph."]
        ]
    },
    {
        "name": "heading_paragraph",
        "source": "| ! A heading\n| \n| A paragraph.",
        "tokens": [
            ["BAR"],
            ["BANG"],
            ["TEXT", "A heading"],
            ["NEWLINE"],
            ["BAR"],
            ["NEWLINE"],
            ["BAR"],
            ["TEXT", "A paragraph."]
        ]
    },
    {
        "name": "double",
        "source": "| A blockquote.\n\n| An another blockquote.",
        "tokens": [
            ["BAR"],
            ["TEXT", "A blockquote."],
            ["MULTI_NEWLINE"],
            ["BAR"],
            ["TEXT", "An another blockquote."]
        ]
    }
]

class TestBlockquote(template.TestLexer): pass
template.generate_tests(TestBlockquote, data)

"""
| A paragraph.
| 
| An another paragraph
"""