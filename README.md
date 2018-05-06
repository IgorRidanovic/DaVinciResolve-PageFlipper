Davinci Resolve Page Flipper

DaVinci Resolve V15 introduced the scripting API allowing user to automate traditionally manual procedures via Python or Lua.

This proof of concept cycles through DaVinci Resolve pages at interval set by the UI slider. A possible use case is for an unatended demo station.

Requirements and Dependencies

You need Resolve V15, of course as well as Python and PyQt4. You also need to add several system environment variables described in the API documentation. Alternately you can make your Python script aware of the location of the fusionscript.dll (fusionscript.so) and DaVinciResolveScript.py which are installed along with DaVinci Resolve v15.
