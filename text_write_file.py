filename = 'files_io/change_this_file.txt'

# open file in Append mode
with open(filename, 'a', encoding='utf-8') as out:
    out.write("Random text\n")

# open file in Write mode (overwrite)
with open(filename, 'w', encoding='utf-8') as out:
    out.write("Random text\n")
