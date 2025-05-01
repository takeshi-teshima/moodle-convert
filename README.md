# moodle-convert
A pandoc-wannabe converter for various moodle quiz formats

## Description
This tool is designed to convert Moodle quiz formats from YAML to XML. It provides a simple command-line interface for converting quizzes, making it easy to import them into Moodle.
[Moodle XML](https://docs.moodle.org/500/en/Moodle_XML_format)

## Quiz Type Support

| Quiz Type     | Supported | Planned | Currently Not Planned |
|---------------|-----------|---------|-----------------------|
| multichoice   | ✓         |         |                       |
| truefalse     | ✓         |         |                       |
| shortanswer   |           |         | ✓                     |
| matching      |           | ✓       |                       |
| cloze         |           |         | ✓                     |
| essay         |           |         | ✓                     |
| numerical     |           | ✓       |                       |
| description   |           |         | ✓                     |

## Installation

```bash
pip install git+https://github.com/takeshi-teshima/moodle-convert.git
```

If you also want to use the validation tool, install it with:

```bash
brew install cue
```

## Usage

### Convert YAML to XML
```
moodle-convert <INPUT.yaml> [OPTIONS]
```

OPTIONS include:
- `--output-format`: Output format. Default is `xml`.
- `--output`: Output filename. Default is the input filename with the extension of the output format appended.

### Check YAML Format Validity
```
$ moodle-convert-validate <INPUT.yaml>
```

### Output template YAML
```
$ moodle-convert-scaffold >> <OUTPUT.yaml>
```

## Features

- Convert Moodle quiz formats from YAML to XML.
- Supports multiple quiz types such as multichoice and yes/no.
- Easy-to-use CLI interface.

## Supported Input Formats

| Format      | Description                | multichoice | truefalse |
|-------------|----------------------------|-------------|-------|
| YAML        | Human-readable format for defining quizzes. | ✓           | ✓     |

This tool currently supports YAML as the input format for Moodle quizzes.

## Supported Output Formats

| Format      | Description                | multichoice | truefalse |
|-------------|----------------------------|-------------|-------|
| XML         | Moodle-compatible XML format for quizzes. | ✓           | ✓     |

The output format is XML, which is compatible with Moodle's quiz import functionality.

## Example YAML

Here is an example of a YAML file that can be converted using this tool:

- [./examples/example.yaml](./examples/example.yaml)

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to your branch.
4. Submit a pull request.

## License

See the LICENSE file for details.

