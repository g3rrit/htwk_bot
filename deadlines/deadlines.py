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
                self.edit_date(int(msg_array[1]), "".join(msg_array[2:len(msg_array)]))
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
        # TODO
        self.update()
        for date in self.dates:
            bot.send_message( "ID[" + str(date["id"]) + "] MODULE: " +  date["module"] + " - DATE: " + date["date"].strftime("%d.%m.%y %H Uhr") + " |")

    def add_date(self, date_str, module_str):
        try:
            date = {
                "id": len(self.dates),
                "date": datetime.strptime(date_str, "%d.%m.%y:%H"),
                "module": module_str
            }
            self.dates.append(date)
        except:
            raise Exception("Wrong format:" + date_str + " " + module_str + ". See man " + self.command)
        self.update()

    def edit_date(self, date_id, date):
        # TODO
        self.update()

    def remove_date(self, date_id):
        # TODO
        self.update()

    def update(self):
        self.dates = [date for date in self.dates if date["date"] > datetime.now()]
        self.save_dates()


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
