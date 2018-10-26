## htwk_bot

#### running the bot

requirement:
- python3 

python modules:
- see [requirements](requirements.txt) (pip3 install -r requirements.txt)

#### adding a module
If you want to add your own module follow these steps:
- create a subfolder (example/)
- add a empty file called __init__.py (example/__init__.py)
- create your module (example/example.py)
- create a class that extends from Handle in your module with a member function get_message(self, bot, client, message)
- add a object of your class to the list HANDLES in the file main.py
