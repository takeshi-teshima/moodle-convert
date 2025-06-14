# -*- coding: utf-8 -*-
from pathlib import Path
import click
from jinja2 import Environment, FileSystemLoader
from src.parsers.yaml_parser import parse_yaml_file
import importlib.resources


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
    parsed = parse_yaml_file(input_path)

    # Handle output format
    if output_format == "xml":
        template = env.get_template("quiz_template.xml")
        output_content = template.render(**parsed)
    else:
        raise ValueError(f"Unsupported output format: {output_format}")

    # Write the output to a file
    with output_path.open("w", encoding="utf-8") as output_file:
        output_file.write(output_content)

    n_quizzes = len(parsed["quizzes"])
    click.echo(f"Converted {n_quizzes} quizzes to {output_format.upper()} format.")


@click.command()
def moodle_convert_scaffold():
    """
    Print the contents of templates/scaffold.yaml to stdout.
    """
    scaffold_resource = importlib.resources.files("src.templates") / "scaffold.yaml"
    with scaffold_resource.open("r", encoding="utf-8") as f:
        click.echo(f.read(), nl=False)


if __name__ == "__main__":
    moodle_convert()
