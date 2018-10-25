#add your modules here ->
from info import info
from example import example
from restart import restart
from man import man
from install import install

HANDLES  = [     
        example.Example_Handle(),
        restart.Restart_Handle(),
        info.Info_Handle(),
        man.Man_Handle(),
        install.Install_Handle()
]


