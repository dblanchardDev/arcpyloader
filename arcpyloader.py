# coding: utf-8
'''Loads the correct arcgisscripting DLL for ArcPy to function
when relaunched from within another Python scripts.'''

#All literal strings will be Unicode instead of bytes
from	__future__	import unicode_literals

import logging

# Try loading arcpy as normal
try:
	import arcpy #pylint: disable=W0611

# If error occurs, attempt to correct module loading paths
except Exception:
	logging.info("ArcPy module failed to load, attempting to correct paths")

	import platform, re, sys

	# Remove all paths pointing to wrong architecture
	if platform.architecture()[0] == "64bit":
		p = re.compile(r"desktop[\d\.]+(?:\\|\/)bin$", re.IGNORECASE)

	else:
		p = re.compile(r"desktop[\d\.]+(?:\\|\/)bin64$", re.IGNORECASE)

	wrong = [s for s in sys.path if p.search(s) is not None]

	for x in wrong:
		sys.path.remove(x)

	# Try importing with cleaned-up paths
	try:
		import arcpy

	except Exception as e:
		logging.critical("Unable to load ArcPy after path corrections - %s", e)
		raise(e)