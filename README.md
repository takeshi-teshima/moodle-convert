# moodle-convert
A pandoc-wannabe converter for various moodle quiz formats

## Installation

```bash
$ <git clone this repo>
$ poetry install
$ poetry run moodle-convert --help
```

## Usage

```
moodle-convert <INPUT.yaml> [OPTIONS]
```

OPTIONS include:
- `--output-format`: Output format. Default is `xml`.
- `--output`: Output filename. Default is the input filename with the extension of the output format appended.

## Features

- Convert Moodle quiz formats from YAML to XML.
- Supports multiple quiz types such as multichoice and yes/no.
- Easy-to-use CLI interface.

## Supported Input Formats

| Format      | Description                | multichoice | yesno |
|-------------|----------------------------|-------------|-------|
| YAML        | Human-readable format for defining quizzes. | ✓           | ✓     |

This tool currently supports YAML as the input format for Moodle quizzes.

## Supported Output Formats

| Format      | Description                | multichoice | yesno |
|-------------|----------------------------|-------------|-------|
| XML         | Moodle-compatible XML format for quizzes. | ✓           | ✓     |

The output format is XML, which is compatible with Moodle's quiz import functionality.

## Example YAML

Here is an example of a YAML file that can be converted using this tool:

```yaml
- type: multichoice
  question: |
    What is the capital of France?
  choices:
    A: "Paris"
    B: "London"
    C: "Berlin"
  answer: A
  feedback:
    A: "Correct! Paris is the capital of France."
    B: "Incorrect. London is not the capital of France."
    C: "Incorrect. Berlin is not the capital of France."
- type: yesno
  question: "The Earth is flat."
  answer: false
  feedback:
    true: "Incorrect. The Earth is not flat."
    false: "Correct! The Earth is not flat."
```

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to your branch.
4. Submit a pull request.

## License

See the LICENSE file for details.

