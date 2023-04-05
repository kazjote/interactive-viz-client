# Packages: dbus-python numpy matplotlib PyGObject

import dbus
import numpy as np
import matplotlib.pyplot as plt
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
import json

DBusGMainLoop(set_as_default=True)

session_bus = dbus.SessionBus()
proxy = session_bus.get_object("eu.kazjote.InteractiveViz", '/eu/kazjote/InteractiveViz')
interactive_viz = dbus.Interface(proxy,
    dbus_interface='eu.kazjote.InteractiveViz')

x = np.linspace(-10, 10, 100)

def params_changed(params):
    params_dict = json.loads(params)
    
    y = x * params_dict['slope'] + params_dict['slope'] + np.random.normal(0, 4, x.shape)
    plt.plot(x, y)
    plt.savefig('/tmp/plot.svg')
    plt.close()
    
    interactive_viz.ReloadPicture('/tmp/plot.svg')


interactive_viz.connect_to_signal('ArgumentsChanged', params_changed)

loop = GLib.MainLoop()
loop.run()