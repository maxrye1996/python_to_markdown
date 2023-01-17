import os

# specify the directory containing the Python files
python_dir = 'Python/'

# specify the directory to create the Markdown files in
markdown_dir = 'Markdown/'

# check if the markdown directory exists, if not create it
if not os.path.exists(markdown_dir):
    os.makedirs(markdown_dir)

# loop through all the Python files in the directory
for filename in os.listdir(python_dir):
    # only process Python files
    if filename.endswith('.py'):
        # open the Python file
        with open(os.path.join(python_dir, filename), 'r') as python_file:
            # read the contents of the Python file
            python_code = python_file.read()
        
        # create the new filename for the Markdown file
        markdown_filename = os.path.splitext(filename)[0] + '.md'
        
        # open the Markdown file for writing
        with open(os.path.join(markdown_dir, markdown_filename), 'w') as markdown_file:
            # write the code block to the Markdown file
            markdown_file.write('```python\n')
            markdown_file.write(python_code)
            markdown_file.write('\n```\n')

print('Markdown files created successfully!')
