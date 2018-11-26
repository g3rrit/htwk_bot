import git

from bot import Handle


class Restart_Handle(Handle):
    command = "retart"

    def on_message(self, bot, client, message, raw_message):
        g: git.Git = git.Git(".")
        ans = g.pull("https://github.com/pearisgreen/htwk_bot.git", "sToEps")

        bot.send_message("git:" + ans)

        # os.execv(sys.executable, ["python3"] + sys.argv)
        exit(0)

    def man(self):
        return [
            "uage: !retart",
            "make the bot pull all pending change",
            "and retart itelf"
        ]
