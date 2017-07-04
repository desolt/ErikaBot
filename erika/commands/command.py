commands = {}


class Command(object):
    def __init__(self, client, name):
        self._client = client
        self.name = name

        commands[name] = self

    async def call(self, channel, caller, args):
        raise NotImplementedError('call(self, args) not implemented!')

