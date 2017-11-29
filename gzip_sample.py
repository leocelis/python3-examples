import gzip

with gzip.open('files_io/gzipped_file.txt.gz', 'rb') as f:
    file_content = f.read()
    print(file_content)
