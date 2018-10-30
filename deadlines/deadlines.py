from datetime import datetime
from bot import Handle


class Deadlines_Handle(Handle):
    command = "deadlines"

    dates = []

    def on_message(self, bot, client, message, raw_message):
        msg_array = message.split()
        msg_array = [msg.strip for msg in msg_array]

        if len(msg_array) == 0 or msg_array[0] == "list":
            bot.send_message("list")
        elif msg_array[0] == "add":
            bot.send_message("add")
        elif msg_array[0] == "edit":
            bot.send_message("edit")
        elif msg_array[0] == "remove":
            bot.send_message("remove")

        bot.send_message(str(msg_array))

    def man(self):
        # TODO
        return []

    def send_deadlines(self, bot):
        for date in self.dates:
            bot.send_message(date)


'''


DATE_FILE = "dates/dates"
class Deadlines:
    Instance = None
    def __init__(self):
        self.dates = []

    def get():
        if not Deadlines.Instance:
            Deadlines.Instance = Deadlines()
        return Deadlines.Instance

    def save(self):
        with open(DATE_FILE, "wb") as file:
            pickle.dump(self.dates, file, pickle.HIGHEST_PROTOCOL)

    def load(self):
        with open(DATE_FILE, "rb") as file:
            self.dates = pickle.load(file)
    
    def add_date(self, date_str, module_str):
        try:
            date = {
                "id" : len(self.dates),
                "date" : datetime.strptime(date_str, "%d.%m.%y:%H"),
                "module" : module_str
            }
            self.dates.append(date)
        except: 
            raise Exception("wrong format")

        self.save()
        return date

    def remove_date(self, count):
        new_dates = [date for date in self.dates if date["id"] != count]
        self.dates = new_dates
        print(self.dates)
        self.save()

    def get_dates(self):
        return self.dates

    def update(self):
        new_dates = [date for date in self.dates if date["date"] > datetime.now()]
        self.dates = new_dates
        print(self.dates)
        self.save()

def date_to_string(date):
    return "| ID[" + str(date["id"]) + "] MODULE: " +  date["module"] + " - DATE: " + date["date"].strftime("%d.%m.%y %H Uhr") + " |"


        if message.content.startswith("!addDate"):
            print(message.content)
            msg_arr = message.content.split()
            try:
                date_str = msg_arr[1]
                module = msg_arr[2]
                date = Deadlines.get().add_date(date_str, module)
                await client.send_message(message.channel, "Deadline hinzugefuegt | " + date_to_string(date))
            except Exception as e:
                print(e)
                await client.send_message(message.channel, "ungueltige eingabe | !addDate <dd.mm.yy:hh> <modul>")

        if message.content.startswith("!getDates"):
            ret_msg = "\n------DEADLINES-----\n"
            for date in Deadlines.get().get_dates():
                ret_msg = ret_msg + date_to_string(date) + "\n"
                print(ret_msg)
            await client.send_message(message.channel, ret_msg)

        if message.content.startswith("!removeDate"):
            msg_arr = message.content.split()
            try:
                m_id = int(msg_arr[1])
                Deadlines.get().remove_date(m_id)
            except Exception as e:
                print(e)
                await client.send_message(message.channel, "ungueltige eingabe | !removeDate <id>")


'''
