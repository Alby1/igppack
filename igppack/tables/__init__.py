from .giustizia import Giustizia

# Enter the tables of your Pack here!
available_tables = [
    Giustizia,

]

# Don't change this, it should automatically generate __all__
__all__ = [table.__name__ for table in available_tables]