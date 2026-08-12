"""Track planned improvements to generated-template test coverage."""

TODO = {
    "expand_generated_template_testing": {
        "estimate": "2-4 engineering days",
        "target": "10-15 representative generation scenarios, retaining the five branch smoke tests",
        "tasks": [
            "Parameterize generation data and fixtures.",
            "Cover default, demo, examples, demo-plus-examples, and custom name/module/Python-range scenarios.",
            "Run generated `make qa/full`, including Ruff, Ty, and Typos.",
            "Build documentation and package artifacts.",
            "Validate generated imports, workflows, Dockerfiles, and other key artifacts.",
            "Test Copier validators and safe local tasks such as Git initialization.",
            "Tune CI runtime across all five framework branches.",
        ],
        "out_of_scope": [
            "Do not execute external GitHub, push, deployment, or PyPI operations in tests.",
            "Avoid exhaustive testing of every option combination.",
        ],
    },
}
