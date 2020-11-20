
import re
import click

content = ""
copy_string = []
new_string = []

def parse_twee(source_path, target_path):
    global content
    global copy_string
    global new_string
    
    # Open the twee file to parse
    file = open(source_path, 'r')
    # Asign the content of the twee file to a string
    content = file.read()

    # List of characters from the content string
    copy_string = list(content)

    #List of characters to be modified and written as text
    new_string = copy_string

    #Open (or create) the output .yarn file
    output_file = open(target_path, 'w')

    # Replace syntax
    regex_replace(r'(\:\:\s?\w+)', passage_header)
    regex_replace(r'(\|\W?\w+\W+\|)', speaker_name)
    regex_replace(r'(\{"(.*")\})', twine_metadata)
    regex_replace(r'".+"\|', end_of_line_symbol)

    # Add the last node end character to the end of the file
    new_string = list("".join(new_string) + "\n===")

    output_file.write("".join(new_string))

    print('\n---------------- \nSuccess!\n----------------')

# Generic function to replace a regex match with a defined value
def regex_replace(regex, replacement_function):
    global copy_string
    global new_string
    reg = re.compile(regex, re.MULTILINE)
    matches = reg.finditer(content)
    for m in matches:
        new_string = list(reg.sub(replacement_function(m), "".join(new_string), ))

# Replacing passage headers
def passage_header(m):
    name = "".join(copy_string[m.start()+3:m.end()])
    return "=== \n\ntitle: "+ name +"\ntags: \n---\n\n"

# Replacing speaker names
def speaker_name(m):
    return "".join(copy_string[m.start()+1:m.end()-1])

# Deleting Twine metadata
def twine_metadata(m):
    return ""

def end_of_line_symbol(m):
    modified_string = list(copy_string[m.start():m.end()-2])
    modified_string[0] = " "
    return "".join(modified_string)

parse_twee('test.twee', 'output.yarn')