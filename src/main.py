# -*- coding: utf-8 -*-
from pathlib import Path
import click
from jinja2 import Environment, FileSystemLoader
from src.parsers.yaml_parser import parse_yaml_file


# Initialize Jinja2 environment
TEMPLATES_DIR = Path(__file__).parent / "templates"
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

OUTPUT_FORMAT_EXTENSIONS = {
    "xml": ".xml",
    # Add other formats here if needed
}


@click.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.option("--output", type=click.Path(), help="Output file path")
@click.option(
    "--output-format",
    type=click.Choice(OUTPUT_FORMAT_EXTENSIONS.keys()),
    default="xml",
    help="Output format",
)
def moodle_convert(input_file, output, output_format):
    """Convert Moodle-compatible quiz files from YAML to the specified format."""
    input_path = Path(input_file)

    # Determine output file path
    if output:
        output_path = Path(output)
    else:
        output_path = input_path.with_suffix(OUTPUT_FORMAT_EXTENSIONS[output_format])

    # Parse the input YAML file
    quizzes = parse_yaml_file(input_path)

    # Handle output format
    if output_format == "xml":
        template = env.get_template("quiz_template.xml")
        output_content = template.render(quizzes=quizzes)
    else:
        raise ValueError(f"Unsupported output format: {output_format}")

    # Write the output to a file
    with output_path.open("w", encoding="utf-8") as output_file:
        output_file.write(output_content)

    click.echo(f"Converted {len(quizzes)} quizzes to {output_format.upper()} format.")


if __name__ == "__main__":
    moodle_convert()
