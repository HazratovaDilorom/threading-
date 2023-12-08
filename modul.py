import threading
import time
from  ism import*
from  familiya import*
from ochistva import*

a1=threading.Thread(target=ism)
a2=threading.Thread(target=familiya)
a3=threading.Thread(target=ochistva)
a1.start()
a2.start()
a3.start()

