# Documentation

This folder contains detailed documentation for the `moodle-convert` project.

## Contents

- **Overview**: General information about the project.
- **Installation**: Steps to set up the project.
- **Usage**: How to use the CLI tool.
- **Development**: Guidelines for contributing to the project.
- **Testing**: Information on running tests.

## Overview

`moodle-convert` is a tool designed to convert Moodle quiz formats, primarily from YAML to XML. It supports various quiz types and provides a simple CLI interface.

## Installation

Refer to the main [README.md](../README.md) for installation instructions.

## Usage

Run the following command to convert a YAML file to XML:

```bash
poetry run moodle-convert <INPUT.yaml> --output-format xml
```

## Development

### Folder Structure

- `src/`: Contains the main source code.
  - `parsers/`: Includes parsers for different formats.
  - `quiz_types/`: Contains implementations for specific quiz types.
  - `templates/`: Stores template files for output formats.
- `tests/`: Contains test cases and sample input/output files.

### Running Tests

Use the following command to run tests:

```bash
poetry run pytest tests/
```