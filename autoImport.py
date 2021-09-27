import os , sys 

versionPython = (sys.version)
pymodbusVersion = 0

try : 
    import pymodbus
    pymodbusVersion = pymodbus.__version__
exception:
    sys.exit("Please install pymodbus module ")

if versionPython >= 3.5 :
    if pymodbus >= 2.5:
        fileUrl = str(pymodbus.__file__)[-8:]
        print(fileUrl)
        #fileUrl = str(fileUrl)
    else:
        sys.exit("pymodbus version must be bigger than >=2.5 ")

else:
    sys.exit("Python version must be bigger than >=3.5 ")