import discord
import util

TOKEN = "NTAzOTk0Nzc1MTM4MDc0NjM0.DrDrOg.jPx2hh-TLOmuSBcnU5gXmifdehA";

class Handle:

    command = None
    
    def on_message(self, client, message):
        pass

    def man(self):
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

        msg_arr = message.content.split();

        # RESTART THE BOT 
        if message.content.startswith("!restart"):
            util.restart_program()

        # INSTALL NEW PYTHON MODULES
        if message.content.startswith("!install"):
            msg_arr = message.content.split()
            if(len(msg_arr) > 1):
                try: 
                    util.install(msg_arr[1])
                    await client.send_message(message.channel, "Module: " + msg_arr[1] + " wurde installiert")
                except Exception as e:
                    await client.send_message(message.channel, str(e))

        # GET THE MANPAGE OF A SPECIFIC COMMAND
        if message.content.startswith("!man"):
            for handle in Bot.get().handles:
                try:
                    if msg_arr[1] == handle.command:
                        man_str = "\n".join(handle.man())
                        await client.send_message(message.channel, "------------\n" + man_str)
                except Exception as e:
                    await client.send_message(message.channel, str(e))

        # GET A LIST OF ALL AVAILABLE COMMANDS
        if message.content.startswith("!help"):
            command_arr = list()
            for handle in Bot.get().handles:
                try:
                    command_list.append(handle.command)
                except Exception as e:
                    await client.send_message(message.channel, str(e))
                    
            try:
                await client.send_message(message.channel, "COMMANDS:\n- ".join(command_list) + "\n to get a more detailed info of each command use !man <command>"
            except Exception as e:
                await client.send_message(message.channel, str(e))


        # HANDLE ALL OTHER COMMANDS
        if msg_arr[0][0] is "!":

            msg_command = msg_arr[0][1:len(msg_arr[0])]

            for handle in Bot.get().handles:
                try:
                    if handle.command == msg_command:
                        handle.on_message(Bot.get(), client, " ".join(msg_arr[1:len(msg_arr)]))
                except Exception as e:
                    await client.send_message(message.channel, str(e))


        # SEND ALL PENDING MESSAGES TO THE SERVER
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


