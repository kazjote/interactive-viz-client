# Packages: dbus-python numpy matplotlib

import dbus
import numpy as np
import matplotlib.pyplot as plt

session_bus = dbus.SessionBus()
proxy = session_bus.get_object("eu.kazjote.InteractiveViz", '/eu/kazjote/InteractiveViz')
interactive_viz = dbus.Interface(proxy,
    dbus_interface='eu.kazjote.InteractiveViz')

x = np.linspace(-10, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.savefig('/tmp/plot.svg')

interactive_viz.ReloadPicture('/tmp/plot.svg')
