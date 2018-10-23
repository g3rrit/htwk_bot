import discord
import util

TOKEN = "NTAzOTk0Nzc1MTM4MDc0NjM0.DrDrOg.jPx2hh-TLOmuSBcnU5gXmifdehA";

class Handle:
    def on_message(self, client, message):
        pass

client = discord.Client()

class Bot:
    Instance = None
    def get():
        if Bot.Instance == None:
            Bot.Instance = Bot()
        return Bot.Instance

    def __init__(self):
        self.handles = list()
        self.msg_buffer = list()

    def start(self):
        client.run(TOKEN)

    def add_handle(self, handle):
        self.handles.append(handle)

    def send_message(self, msg):
        self.msg_buffer.append(msg)

    @client.event
    async def on_message(message):
        #dont reply to itself
        if message.author == client.user:
            return

        if message.content.startswith("!restart"):
            util.restart_program()

        for handle in Bot.get().handles:
            try:
                handle.on_message(Bot.get(), client, message)
            except Exception as e:
                await client.send_message(message.channel, str(e))

        for msg in Bot.get().msg_buffer:
            if isinstance(msg, str) and len(msg) > 0:
                await client.send_message(message.channel, msg)
        Bot.get().msg_buffer.clear()

    @client.event
    async def on_ready():
        print("Logged in")
        print(client.user.name)
        print(client.user.id)
        print("------------")


