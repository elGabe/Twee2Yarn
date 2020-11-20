
import re

# Open the twee file to parse
file = open('test.twee', 'r')
# Asign the content of the twee file to a string
content = file.read()

# List of characters from the content string
copy_string = list(content)

#List of characters to be modified and written as text
new_string = copy_string

#Open (or create) the output .yarn file
output_file = open('output.yarn', 'w')

def regex_replace(regex, replacement_function):
    global copy_string
    global new_string
    reg = re.compile(regex)
    matches = reg.finditer(content)
    for m in matches:
        new_string = list(reg.sub(replacement_function(m), "".join(new_string)))

def passage_header(m):
    name = "".join(copy_string[m.start()+3:m.end()])
    return "=== \n\ntitle: "+name +"\ntags: \n---\n\n"


def speaker_name(m):
    return "".join(copy_string[m.start()+1:m.end()-1])


regex_replace(r'(\:\:\s?\w+)', passage_header)
regex_replace(r'(\|\W?\w+\W+\|)', speaker_name)

output_file.write("".join(new_string))

print('\n---------------- \nSuccess!\n----------------')