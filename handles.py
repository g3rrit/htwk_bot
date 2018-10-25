#add your modules here ->
from info import info
from example import example
from restart import restart
from man import man
from install import install
from bongoloch import bongoloch

HANDLES = [
    example.Example_Handle(),
    restart.Restart_Handle(),
    info.Info_Handle(),
    man.Man_Handle(),
    install.Install_Handle(),
    bongoloch.Bongoloch_Handle()
]


