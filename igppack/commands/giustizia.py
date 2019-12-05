from typing import *
from royalnet.commands import *
from royalnet.utils import *
from royalnet.backpack.tables import User
from sqlalchemy import func
from igppack.tables import *


class GiustiziaCommand(Command):
    name: str = "giustizia"

    description: str = "Numero dei giustiziati"

    syntax: str = ""

    aliases = ["gt"]

    async def run(self, args: CommandArgs, data: CommandData) -> None:

        username = args.optional(0)
        variazione = args.optional(1)
        blocco = await data.get_author(error_if_none=True)
        if blocco is not 1 and variazione is not None:
            await data.reply(f"Non sei autorizzato a modificare le giustizie.")
        else:
            if username is None:
                user: User = await data.get_author(error_if_none=True)
            else:
                found: Optional[User] = await asyncify(
                    data.session
                        .query(self.alchemy.get(User))
                        .filter(func.lower(self.alchemy.get(User).username) == func.lower(username))
                        .one_or_none
                )
                if not found:
                    raise InvalidInputError("Utente non trovato.")
                else:
                    user = found

            if user.giustizia is None:

                giustizia = self.alchemy.get(Giustizia)(user = user, conteggio = 0)
                data.session.add(giustizia)
                await data.session_commit()

            else:
                giustizia = user.giustizia

            if variazione is not None:
                varint = int(variazione)
                giustizia.conteggio = giustizia.conteggio + varint
                await data.session_commit()

            await data.reply(f"{user.username} sarà giustiziato: {giustizia.conteggio} volte")




#/giustizia → tuo punteggio
#/giustizia [nome] → punteggio di nome
#/giustizia [nome] +1 → aggiunge 1 a punteggio di nome