from royalnet.commands import *


class EatCommand(Command):
    name: str = "eat"

    description: str = "Mangia qualcosa!"

    syntax: str = "{cibo}"

    _FOODS = {
                "_default": "🍗 Hai mangiato {food}!\n[i]Ma non è successo nulla.[/i]",
                "asca28": "🚹 Hai mangiato {food}!\n[i]Accipicchia, adesso come facciamo!?[/i]",
                "asca 28": "🚹 Hai mangiato {food}!\n[i]Accipicchia, adesso come facciamo!?[/i]",
                "asca": "🚹 Hai mangiato {food}!\n[i]Accipicchia, adesso come facciamo!?[/i]",
                "j1one": "🚹 Hai mangiato {food}!\n[i]Accipicchia, adesso come facciamo!?[/i]",
                "j1": "🚹 Hai mangiato {food}!\n[i]Accipicchia, adesso come facciamo!?[/i]",
                "jummi": "🚹 Hai mangiato {food}!\n[i]Accipicchia, adesso come facciamo!?[/i]",
                "lori": "🚹 Hai mangiato {food}!\n[i]Accipicchia, adesso come facciamo!?[/i]",
                "carro": "🚹 Hai mangiato {food}!\n[i]Accipicchia, adesso come facciamo!?[/i]",
                "al": "🚹 Hai mangiato {food}!\n[i]Accipicchia, adesso come facciamo!?[/i]",
                "alby": "🚹 Hai mangiato {food}!\n[i]Accipicchia, adesso come facciamo!?[/i]",
                "malbyx": "🚹 Hai mangiato {food}!\n[i]Accipicchia, adesso come facciamo!?[/i]",
    }

    async def run(self, args: CommandArgs, data: CommandData) -> None:
        food = args.joined(require_at_least=1)
        food_string = self._FOODS.get(food.lower(), self._FOODS["_default"])
        await data.reply(food_string.format(food=food.capitalize()))


