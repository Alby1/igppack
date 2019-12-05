from .giustizia import GiustiziaCommand
from .rage import RageCommand
# Enter the commands of your Pack here!
available_commands = [
    GiustiziaCommand,
    RageCommand,


]

# Don't change this, it should automatically generate __all__
__all__ = [command.__name__ for command in available_commands]