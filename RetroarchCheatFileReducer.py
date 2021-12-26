"""
Retroarch Cheat File Reducer
Scripted by: RB
AKA: Git-Forked
Source Code:  https://github.com/Git-Forked/RetroarchCheatFileReducer/

NOTES:
requires: pip install easygui
or set a file manually.
"""

"""
SIMPLE CONFIGURATION
"""

# Print extra data to screen. True or False.
verbose = False

# Use EasyGUI. True or False.
use_easygui = True

"""
ADVANCED CONFIGURATION
"""

# Use EasyGUI to choose a file or set one manually @ file_path
if use_easygui == True:
    import easygui
    file_path = easygui.fileopenbox()
else:
    # Alternately set a file manually to work with.
    # Do this if your choice to use EasyGUI is False.
    file_path = "/home/user/Desktop/Test.cht"

"""
PROCESS
"""

print("Opened file: " + file_path + "\n")

# n for cheat incrementation, always starts at 0
n = 0

# substring_previous always set to "" to delcare empty string variable
substring_previous = ""

# replaced_content always set to "" to delcare empty string variable
replaced_content = ""

# Open the file for reading and make edits to the file content.
with open(file_path, 'r') as file:
    for line in file:
        # Strip line breaks
        line = line.strip()
        # Ignore empty lines
        if not line.isspace():
            # Ignore the "cheats = ??"" line.
            if not "cheats" in line:
                # Make sure line contains "cheats".
                if "cheat" in line:
                    # Get the substring number. (String in string technique.)
                    start = line.index('cheat')     # From "cheat"
                    end = line.index('_',start+1)   # To "_"
                    substring = line[start+5:end]   # The substring number
                    # Check whether or not to increment n.
                    if substring_previous != "" and substring_previous != substring:
                        # Another cheat was found.
                        if verbose == True: print("\n-----Next cheat found.")
                        # increment n by 1
                        n+=1
                        # Replacement text as new_line.
                        new_line = "\n" + line.replace(substring, str(n), 1)
                    else:
                        # Replacement text as new_line.
                        new_line = line.replace(substring, str(n), 1)
                    # Verbose printing to console.
                    if verbose == True: print("[Replace " + substring + " with " + str(n) + "]")
                    if verbose == True: print("Original : " + line)
                    if verbose == True: print("Replaced : " + new_line)
                    # Concatenate the new string and add an end-line break
                    replaced_content = replaced_content + new_line + "\n"
                    # Save a variable for substring as substring_previous
                    substring_previous = substring

# Write cheat total to top of file.
replaced_content = "cheats = " + str(n+1) + "\n" + replaced_content
# Print new content to the console.
if verbose == True: print("\nNew content: \n\n" + replaced_content)

# Print total cheats to console.
print("\nTotal cheats processed: " + str(n+1) + "\n")

# Write new content to file.
if use_easygui == True:
    file_path = easygui.filesavebox()
with open(file_path, 'w') as file:
        file.write(replaced_content)
print("Filed saved as: " + file_path + "\n")
