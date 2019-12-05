import typing
import random
from royalnet.commands import *


class RageCommand(Command):
    name: str = "rage"

    aliases = ["madden"]

    description: str = "Arrabbiati per qualcosa, come una software house californiana."

    _MAD = ["MADDEN MADDEN MADDEN MADDEN",
            "EA bad, praise Geraldo!",
            "Stai sfogando la tua ira sul bot!",
            "Basta, io cambio gilda!",
            "Fondiamo la IGP2!",
            "Ubaldo non si infama!",
            "Si stava meglio nell'era di Piero!",
            "Ubaldo si sta rivoltando nella tomba!"]

    async def run(self, args: CommandArgs, data: CommandData) -> None:
        await data.reply(f"😠 {random.sample(self._MAD, 1)[0]}")
