# Packages: dbus-python numpy matplotlib PyGObject

import dbus
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
import json

DBusGMainLoop(set_as_default=True)

session_bus = dbus.SessionBus()
proxy = session_bus.get_object("eu.kazjote.InteractiveViz", '/eu/kazjote/InteractiveViz')
interactive_viz = dbus.Interface(proxy,
    dbus_interface='eu.kazjote.InteractiveViz')

x = np.linspace(-10, 10, 100)

matplotlib.use('Gtk4Agg')

fig = plt.figure()
ax = fig.add_subplot(111)
plt.ion()
fig.show()

def params_changed(params):
    ax.cla()
    params_dict = json.loads(params)
    
    y = x * params_dict['slope'] + params_dict['slope'] + np.random.normal(0, 4, x.shape)
    ax.plot(x, y)
    # plt.savefig('/tmp/plot.svg')
    
    interactive_viz.ReloadPicture('/tmp/plot.svg')


interactive_viz.connect_to_signal('ArgumentsChanged', params_changed)

loop = GLib.MainLoop()
loop.run()