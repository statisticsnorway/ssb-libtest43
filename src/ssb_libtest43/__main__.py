"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """SSB Libtest43."""


if __name__ == "__main__":
    main(prog_name="ssb-libtest43")  # pragma: no cover
