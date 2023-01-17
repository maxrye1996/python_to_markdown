import os

# specify the source directory and destination file
src_dir = 'Python/'
dest_file = 'python_docs.txt'

# open the destination file in write mode
with open(dest_file, 'w') as out_file:
    # iterate through the files in the source directory
    for filename in os.listdir(src_dir):
        # only process .py files
        if filename.endswith('.py'):
            # write the filename in uppercase
            out_file.write(filename.upper())
            out_file.write('\n')
            with open(os.path.join(src_dir, filename), 'r') as in_file:
                out_file.write(in_file.read())
                out_file.write('\n')
