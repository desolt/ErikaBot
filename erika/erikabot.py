import discord
from . import commands


class ErikaBot(discord.Client):
    def __init__(self, config):
        super().__init__()
        self.config = config

    def run(self):
        super().run(self.config['token'])

    async def on_ready(self):
        print('ErikaBot reporting for duty!')
        self.register_commands()
        game = discord.Game(name="Go | type er!help", url="https://github.com/desolt", type=0)
        await self.change_presence(game=game)

    def register_commands(self):
        commands.HelpCommand(self)

    async def on_message(self, message):
        if message.content.startswith('er!') and len(message.content) > 3:
            args = message.content.split(' ')
            cmd_name = args[0][3:]
            try:
                await commands.commands[cmd_name].call(message.channel, message.author, args)
            except KeyError:
                await self.send_message(message.channel, 'Command not found!')

    async def process_command(self, source, command, args):
        print(command)
        print(args)

        if 'hello' in command:
            await self.send_message(source, 'Guess who\'s back...')

