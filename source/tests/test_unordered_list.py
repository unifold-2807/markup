import source.tests.template as template

data = [
    {
        "name": "single_item",
        "source": "- An unordered list item",
        "tokens": [
            ["HYPHEN"],
            ["TEXT", "An unordered list item"],
        ]
    },
    {
        "name": "multiple_items",
        "source": "- An unordered list item 1\n- An unordered list item 2\n- An unordered list item 3",
        "tokens": [
            ["HYPHEN"],
            ["TEXT", "An unordered list item 1"],
            ["NEWLINE"],
            ["HYPHEN"],
            ["TEXT", "An unordered list item 2"],
            ["NEWLINE"],
            ["HYPHEN"],
            ["TEXT", "An unordered list item 3"],
        ]
    },
    {
        "name": "inline_formattings",
        "source": "- An unordered list item with inline formattings: *bold*, /italicized/, _underlined_, ~struck through~, `inline code`",
        "tokens": [
            ["HYPHEN"],
            ["TEXT", "An unordered list item with inline formattings: "],
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
        "source": "- An unordered list item with marks: #, |, -, +",
        "tokens": [
            ["HYPHEN"],
            ["TEXT", "An unordered list item with marks: #, |, -, +"]
        ]
    }
]

class TestUnorderedList(template.TestLexer): pass
template.generate_tests(TestUnorderedList, data)