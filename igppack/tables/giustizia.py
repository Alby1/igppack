from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import *
from royalnet.backpack.tables import *

class Giustizia:
    __tablename__ = "giustizia"

    @declared_attr
    def user_id(self):
        return Column(Integer, ForeignKey("users.uid"), primary_key=True)

    @declared_attr
    def user(self):
        return relationship("User", backref=backref("giustizia", uselist=False))

    @declared_attr
    def conteggio(self):
        return Column(Integer)

