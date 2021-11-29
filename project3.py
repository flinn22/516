import re # Import the library of regular expressions

# Open a file 
file = input("Please name the file you'd like to open, including .txt: ") # Ask the user to input the name of the file they would like to open, and names it 'file'
import os.path # Use the os.path module to access the file system and open the file
if os.path.exists(file): # If the file exists...
    print ("It exists!") # Print "It exists!"
else: # If the file doesn't exist...
    file = input("Please try again: ") # Ask the user again to input the name of the file they would like to open, and names it 'file'

with open(file) as file_doc: # Open the file as a DOC file
    file_content = file_doc.read() # Label reading the DOC file as "file_content"

# Change two features from UK to US-style English
output = re.sub('yse', 'yze', file_content, flags=re.I) # Substitute each instance of "yze" (US) for "yse" (UK) inside of "file_content,"" from above. 
# (The flag re.I makes sure upper and lower-case words are recognized). Then assign the results to the variable "output."

output2 = re.sub('lled', 'led', output, flags=re.I) # Substitute each instance of "led" (US) for "lled" (UK) inside of "output," from above. 
# Then, assign the results to the variable "output2."

# Save the output in a file
with open('output.txt', "a+") as f: # This opens the file in which we'll save the output.  A+ shows we'll append information to this file.
    f.write(output2) # This writes output2 into the output.txt file