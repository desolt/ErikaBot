from erika.commands.command import Command

help_menu = '```css\n' \
            'er!help - shows this help menu.\n' \
            '```'


class HelpCommand(Command):
    def __init__(self, client):
        super().__init__(client, 'help')

    async def call(self, channel, caller, args):
        if len(args) == 1:
            await self._client.send_message(caller, help_menu)
        else:
            await self._client.send_message(channel, 'Too many arguments!')
