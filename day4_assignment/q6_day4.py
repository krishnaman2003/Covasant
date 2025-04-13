"""
Question-6:
#MaxFile class 
from pkg.file import File 
fs = File(".")
fs.getMaxSizeFile(2) # gives two max file names 
fs.getLatestFiles(datetime.date(2018,2,1))
#Returns list of files after 1st Feb 2018 
"""

from pkg.file import File
import datetime
fs = File(".")
max_size_files = fs.getMaxSizeFile(2)
print("Max size files:", max_size_files)
latest_files = fs.getLatestFiles(datetime.date(2018, 2, 1))
print("Files modified after 2018-02-01:", latest_files)
