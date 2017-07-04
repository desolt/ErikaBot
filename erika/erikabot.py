import discord


class ErikaBot(discord.Client):
    def __init__(self, config):
        super().__init__()
        self.config = config

    def run(self):
        super().run(self.config['token'])

    async def on_ready(self):
        print('ErikaBot reporting for duty!')

    async def on_message(self, message):
        if message.content.startswith('er!') and len(message.content) > 3:
            args = message.content.split(' ')
            command = args[0][3:]
            await self.process_command(message.channel, command, args)

    async def process_command(self, source, command, args):
        print(command)
        print(args)

        if 'hello' in command:
            await self.send_message(source, 'Guess who\'s back...')

