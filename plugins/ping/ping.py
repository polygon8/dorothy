from errbot import BotPlugin, botcmd


class Ping(BotPlugin):
    """
    pong
    """

    @botcmd
    def ping(self, message, args):
        """
        Replies with 'pong'
        """
        return 'pong'
