import subprocess
import shutil
import click
from pathlib import Path

# 定数として .cue ファイルのパスを定義
CUE_SCHEMA_PATH = Path(__file__).parent / "yaml_schema.cue"


@click.command()
@click.argument("yaml_file", type=click.Path(exists=True, path_type=Path))
def validate_yaml(yaml_file):
    """
    Validate a YAML file against the CUE schema using `cue vet`.
    """
    # cueコマンドが存在するか確認
    if shutil.which("cue") is None:
        click.echo("Error: 'cue' command not found. Please install it using a package manager like brew.")
        return

    try:
        # subprocessでcue vetを実行
        result = subprocess.run(
            ["cue", "vet", str(yaml_file), str(CUE_SCHEMA_PATH)],
            check=True,
            text=True,
            capture_output=True,
        )
        click.echo("Validation succeeded!")
        click.echo(result.stdout)
    except subprocess.CalledProcessError as e:
        click.echo("Validation failed!")
        click.echo(e.stderr)
