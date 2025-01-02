import source.tests.template as template

data = [
    {
        "name": "default",
        "source": "```# A code block```",
        "tokens": [
            ["TRIPLE_BACKTICK"],
            ["CODE", "# A code block"],
            ["TRIPPLE_BACKTICK"]
        ]
    },
    {
        "name": "newline",
        "source": "```# A code block that has a \nnewline character```",
        "tokens": [
            ["TRIPLE_BACKTICK"],
            ["CODE", "# A code block that has a \nnewline character"],
            ["TRIPLE_BACKTICK"]
        ]
    },
    {
        "name": "double_newline",
        "source": "```# A code block that has \n\ntwo newline characters```",
        "tokens": [
            ["TRIPLE_BACKTICK"],
            ["CODE", "# A code block that has \n\ntwo newline characters"],
            ["TRIPLE_BACKTICK"]
        ]
    },
    {
        "name": "marks",
        "source": "```# A code block with marks: #, |, *, /, _, `, ~```",
        "tokens": [
            ["TRIPLE_BACKTICK"],
            ["CODE", "# A code block with marks: #, |, *, /, _, `, ~"],
            ["TRIPLE_BACKTICK"]
        ]
    }
]

class TestCodeBlock(template.TestLexer): pass
template.generate_tests(TestCodeBlock, data)