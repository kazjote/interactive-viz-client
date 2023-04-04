import dbus

session_bus = dbus.SessionBus()
proxy = session_bus.get_object("eu.kazjote.InteractiveViz", '/eu/kazjote/InteractiveViz')
