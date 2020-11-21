
import re
import click

content = ""
copy_string = []
new_string = []

# Replacing passage headers
def passage_header(m):
    match = m.group(0)
    name = "".join(list(match)[3:len(match)])
    return "=== \n\ntitle: "+ name +"\ntags: \n---\n\n"

# Replacing speaker names
def speaker_name(m):
    match = m.group(0)
    return "".join(list(match)[1:len(match)-1])

# Deleting Twine metadata
def twine_metadata(m):
    return ""

# Deletes the "| and the end of the twine lines
def end_of_line_symbol(m):
    match = m.group(0)
    modified_string = list(list(match)[0:len(match)-2])
    modified_string[0] = " "
    return "".join(modified_string)

patterns = {
    r'(\:\:\s?\w+)(\.\w+)?' : passage_header,
    r'(\|\W?\w+\W+\|)' : speaker_name,
    r'(\{"(.*")\})' : twine_metadata,
    r'".+"\|' : end_of_line_symbol
}

def parse_twee(source_path, target_path):
    global content
    global copy_string
    global new_string
    
    # Open the twee file to parse
    file = open(source_path, 'r')
    
    # Asign the content of the twee file to a string
    content = file.read()

    #List of characters to be modified and later written as text
    new_string = list(content)

    output_file = open(target_path, 'w')

    # Replace syntax
    for regex, function in patterns.items():
        regex_replace(regex, function)

    # Append the last "node end" character to the end of the file and write it to a .yarn file
    new_string = list("".join(new_string) + "\n===")
    output_file.write("".join(new_string))

    print('\n---------------- \nSuccess!\n----------------')

# Generic function to replace a regex match with a value taken from a function
def regex_replace(regex, replacement_function):
    global new_string
    new_string = list(re.sub(regex, replacement_function, "".join(new_string), 0, re.MULTILINE))


parse_twee('test.twee', 'output.yarn')