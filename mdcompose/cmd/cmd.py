import click
from mdcompose.main import main
from mdcompose.utils import utils

@click.command("md")

# TODO fix the clik interface

def mdcompose_init():
    main.init_config_file()
    print("config file created")