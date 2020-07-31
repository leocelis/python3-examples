"""
Read as bytes, extract as bytes, convert to text
"""
import io
import tarfile

# open tar.gz file
f = io.open("tarfile_example.tar.gz", 'rb')
# read as bytes
fb = io.BytesIO(f.read())
tar = tarfile.open(fileobj=fb, mode='r:gz')

# iterate through files
for name in tar.getmembers():
    # extract specific file
    if name.name == "tarfile_example.txt":
        # extract file, read as bytes, output as text
        ef = tar.extractfile(name)
        efb = io.BytesIO(ef.read())
        c = efb.read().decode('UTF-8')
        print(c)
