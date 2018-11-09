from datetime import datetime
from bot import Handle
import pickle

DATE_FILE = "deadlines/dates"


class Deadlines_Handle(Handle):
    command = "deadlines"

    dates = []

    def __init__(self):
        super().__init__()
        self.load_dates()

    def on_message(self, bot, client, message, raw_message):
        msg_array = message.split()

        if len(msg_array) == 0 or msg_array[0] == "list":
            self.list_dates(bot)
        elif msg_array[0] == "add":
            try:
                self.add_date(msg_array[1], msg_array[2])
            except ValueError:
                raise Exception("Unknown argument: " + msg_array[0] + " " + msg_array[1] + ". See man " + self.command)
        elif msg_array[0] == "edit":
            try:
                self.edit_date(int(msg_array[1]), msg_array[2], "".join(msg_array[3:len(msg_array)]))
            except ValueError:
                raise Exception("Unknown argument: " + msg_array[0] + " " + msg_array[1] + ". See man " + self.command)
        elif msg_array[0] == "remove":
            self.remove_date(int(msg_array[1]))
        else:
            raise Exception("Unknown argument: " + msg_array[0] + ". See man " + self.command)

    def man(self):
        # TODO
        return []

    def save_dates(self):
        with open(DATE_FILE, "wb") as file:
            pickle.dump(self.dates, file, pickle.HIGHEST_PROTOCOL)

    def load_dates(self):
        try:
            with open(DATE_FILE, "rb") as file:
                self.dates = pickle.load(file)
                self.update()
        except:
            # TODO
            pass

    def list_dates(self, bot):
        self.update()
        id_size = len(str(len(self.dates)))
        desc_size = max([len(date["module"]) for date in self.dates])
        date_str = "```--------DEADLINES--------\n"
        for date in self.dates:
            date_str += ("ID: " + str(date["id"]).rjust(id_size) + " --- DESC: " + date["module"].ljust(desc_size)
                         + " --- DATE: " + date["date"].strftime("%d.%m.%y %H:%M Uhr") + " |\n")
        bot.send_message(date_str + "```")

    def add_date(self, date_str, module_str):
        try:
            date = {
                "id": len(self.dates),
                "date": datetime.strptime(date_str, "%d.%m.%y:%H:%M"),
                "module": module_str
            }
            self.dates.append(date)
        except:
            raise Exception("Wrong format:" + date_str + " " + module_str + ". See man " + self.command)
        self.update()

    def edit_date(self, date_id, date, desc):
        self.remove_date(date_id)
        self.add_date(date, desc)

    def remove_date(self, date_id):
        self.dates = [date for date in self.dates if date["id"] != date_id]
        self.update()

    def update(self):
        self.dates = [date for date in self.dates if date["date"] > datetime.now()]
        self.dates.sort(key=lambda date: date["date"])
        for i in range(0, len(self.dates)):
            self.dates[i]["id"] = i
        self.save_dates()