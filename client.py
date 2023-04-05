# Packages: dbus-python numpy matplotlib PyGObject

import dbus
import numpy as np
import matplotlib.pyplot as plt
from dbus.mainloop.glib import DBusGMainLoop
import time
from gi.repository import GLib

DBusGMainLoop(set_as_default=True)

session_bus = dbus.SessionBus()
proxy = session_bus.get_object("eu.kazjote.InteractiveViz", '/eu/kazjote/InteractiveViz')
interactive_viz = dbus.Interface(proxy,
    dbus_interface='eu.kazjote.InteractiveViz')

x = np.linspace(-10, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.savefig('/tmp/plot.svg')

interactive_viz.ReloadPicture('/tmp/plot.svg')
interactive_viz.connect_to_signal('ArgumentsChanged', lambda args: print(f'Arguments changed: {args}'))

loop = GLib.MainLoop()
loop.run()