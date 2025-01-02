import source.tests.template as template

data = [
    {
        "name": "single_item",
        "source": "+ An ordered list item",
        "tokens": [
            ["PLUS"],
            ["TEXT", "An ordered list item"],
        ]
    },
    {
        "name": "multiple_items",
        "source": "+ An ordered list item 1\n+ An ordered list item 2\n+ An ordered list item 3",
        "tokens": [
            ["PLUS"],
            ["TEXT", "An ordered list item 1"],
            ["NEWLINE"],
            ["PLUS"],
            ["TEXT", "An ordered list item 2"],
            ["NEWLINE"],
            ["PLUS"],
            ["TEXT", "An ordered list item 3"],
        ]
    },
    {
        "name": "inline_formattings",
        "source": "+ An ordered list item with inline formattings: *bold*, /italicized/, _underlined_, ~struck through~, `inline code`",
        "tokens": [
            ["PLUS"],
            ["TEXT", "An ordered list item with inline formattings: "],
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
            ["BACKTICK"]
        ]
    },
    {
        "name": "marks",
        "source": "+ An ordered list item with marks: #, |, -, +",
        "tokens": [
            ["PLUS"],
            ["TEXT", "An ordered list item with marks: #, |, -, +"]
        ]
    }
]

class TestOrderedList(template.TestLexer): pass
template.generate_tests(TestOrderedList, data)