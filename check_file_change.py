"""
How to run it:

$ python3 files_io/check_file_change.py

In a separate console run:

$ python3 files_io/text_write_file.py
"""
import os
from time import sleep

# Watch for changes
root_dir = os.path.abspath(os.path.dirname(__file__)) + '/'
filename = root_dir + "change_this_file.txt"

# Show when was the last time the file was modified
last_modified_time = os.stat(filename).st_mtime
print("Last modified: {t}".format(t=last_modified_time))

# Append to the file and compare the modified time
with open(filename, 'a') as f:
    f.write("hello: world \n")
    f.closed

# Read the content of the file again
with open(filename, 'r') as f:
    read_data = f.read()
    print(read_data)
    f.closed

new_modified_time = os.stat(filename).st_mtime
print("Last modified: {t}".format(t=new_modified_time))

# check every 2 seconds if the file was modified
while True:
    new_modified_time = os.stat(filename).st_mtime

    # Verify if the file was modified
    if new_modified_time > last_modified_time:
        last_modified_time = new_modified_time
        print("The file was updated at {t}! \n".format(t=last_modified_time))
    sleep(2)
