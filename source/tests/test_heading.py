import source.tests.template as template

data = [
    {
        "name": "level_1",
        "source": "! A heading of level 1",
        "tokens": [
            ["BANG"],
            ["TEXT", "A heading of level 1"]
        ]
    },
    {
        "name": "level_2",
        "source": "!! A heading of level 2",
        "tokens": [
            ["BANG"],
            ["BANG"],
            ["TEXT", "A heading of level 2"]
        ]
    },
    {
        "name": "level_3",
        "source": "!!! A heading of level 3",
        "tokens": [
            ["BANG"],
            ["BANG"],
            ["BANG"],
            ["TEXT", "A heading of level 3"]
        ]
    },
    {
        "name": "line_break",
        "source": "! A heading that has a \nline break",
        "tokens": [
            ["BANG"],
            ["TEXT", "A heading that has a "],
            ["NEWLINE"],
            ["TEXT", "line break"]
        ]
    },
    {
        "name": "double",
        "source": "! A heading\n\n! An another heading",
        "tokens": [
            ["BANG"],
            ["TEXT", "A heading"],
            ["MULTI_NEWLINE"],
            ["BANG"],
            ["TEXT", "An another heading"]
        ]
    },
    {
        "name": "bang",
        "source": "! A heading that has a ! (bang)",
        "tokens": [
            ["BANG"],
            ["TEXT", "A heading that has a ! (bang)"]
        ]
    },
    {
        "name": "inline_formattings",
        "source": "! A heading that has inline formattings: *bold*, /italicized/, _underlined_",
        "tokens": [
            ["BANG"],
            ["TEXT", "A heading that has inline formattings: "],
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
        ]
    }
]

class TestHeading(template.TestLexer): pass
template.generate_tests(TestHeading, data)