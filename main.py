from gtts import gTTS
import wikipedia as wiki
import sys

bad_sections = ['See also', 'References', 'External links', 'Gallery']


# removes the sections which wouldn't be useful in these formats
def remove_extra(page):
    new_sections = page.sections
    for x in bad_sections:
        if x in new_sections:
            new_sections.remove(x)
    return new_sections

def to_console(page):
    new_sections = remove_extra(page)
    for x in range(len(new_sections)):
        print(new_sections[x])
        print(page.section(new_sections[x]))

"""
currently has issues encoding, certain characters cause issues.
"""
def to_file(page, user_input):
    fileName = user_input + "_wikipedia.txt"
    file = open(fileName, "w")
    new_sections = remove_extra(page)
    #try:
    for x in range(len(new_sections)):
        file.write(new_sections[x])
        file.write('\n')
        print(page.section(new_sections[x]))
        file.write(page.section(new_sections[x]))
        file.write('\n')
    #except:
        print("Error! something went wrong when writing to file!")


def menu():
    print("For the given summary would you like to:")
    print("1. Copy to a text file (currently broken)")
    print("2. Print to the console")
    print("3. Create an mp3 file")
    user_input = input("Please select the number: ")
    return user_input


def to_mp3(page, user_input):
    new_sections = remove_extra(page)
    clean_string = ""
    for x in range(len(new_sections)):
        clean_string += new_sections[x]
        clean_string += '\n'
        clean_string += page.section(new_sections[x])
    tts = gTTS(text=clean_string, lang='en')
    tts.save(user_input + ".mp3")
    print("file has been turned into an mp3")

# main
user_input = input("Enter the Wikipedia page you want to search!")
page = wiki.page(user_input)
print(wiki.summary(user_input))
menu_selection = menu()
if menu_selection is "1":
    to_file(page, user_input)
    print("File successfully saved to: " + user_input + "_wikipedia.txt")
elif menu_selection == "2":
    to_console(page)
elif menu_selection == "3":
    to_mp3(page, user_input)
else:
    print("Invalid input!")






