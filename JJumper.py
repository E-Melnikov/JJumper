import webbrowser
try:
    from Tkinter import *
except:
    from tkinter import *
from platform import system as platform
from os import system

############### APP CONFIGURATION #########################
# Put here list of your current projects
projects = ['CHAT', 'WSM', 'EE', 'ADI']

# Project that will bw open if letters index is not specified
default_project = 'EE'

buttons_font = 'Verdana 12'
input_font = 'Verdana 18'

# Values: True or False
destroy_app_in_the_end = True # True or False

# Your Chrome path (It may be Firefox or Opera too)
chrome_path_windows = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
chrome_path_macos = 'open -a /Applications/Google\ Chrome.app %s'
###########################################################

if platform() == 'Darwin':
    chrome_path = chrome_path_macos
elif platform() == 'Windows':
    chrome_path = chrome_path_windows


def on_key_release(event):
    ctrl = (event.state & 0x4) != 0
    if event.keycode == 88 and ctrl and event.keysym.lower() != "x":
        event.widget.event_generate("<<Cut>>")
    if event.keycode == 86 and ctrl and event.keysym.lower() != "v":
        event.widget.event_generate("<<Paste>>")
    if event.keycode == 67 and ctrl and event.keysym.lower() != "c":
        event.widget.event_generate("<<Copy>>")


if len(projects) == 1:
    width_value = 15
else:
    width_value = 10

root = Tk()
root.title("JJumper")
entry_text = StringVar()


def key(event):
    print("pressed", repr(event.char))
    print('help')


def auto_uppercase(*arg):
    current_entry = entry_text.get()
    print('UPDATE', current_entry)

    if (current_entry
        and current_entry[-1].isdigit()
        and not '-' in current_entry
        and len(current_entry) > 1
        and not current_entry[-2].isdigit()):
        new_line = []
        for letter in current_entry:
            if not letter.isdigit():
                entry_text.set(current_entry.upper())
            if letter.isdigit() and not current_entry[-1] == '-':
                new_line.append('-')
                new_line.append(letter)
                entry.insert(len(entry_text.get()) - 1, '-')
        entry_text.set(entry_text.get().upper())
    else:
        entry_text.set(current_entry.upper())


def func(event):
    print(entry.get())
    open_jira(entry.get())


root.bind('<Return>', func)
root.bind_all("<Key>", on_key_release, "+")
frame = Frame(root)
root.resizable(0,0)
frame.grid()


def open_jira(value, project_name_=default_project):
    base_URL = "https://jira.wixpress.com/browse/"
    if value.isdigit():
        URL = base_URL + "{}-".format(project_name_) + value
    else:
        URL = base_URL + value

    webbrowser.get(chrome_path).open(URL)
    if destroy_app_in_the_end:
        root.destroy()


def retrieve_input(project_name):
    entry_value = entry.get()
    open_jira(entry.get(), project_name)


entry = Entry(root, width=14, font=input_font, textvariable=entry_text)
entry.focus_set()
entry.grid(row=0, column=0, sticky='ew', columnspan=len(projects))

index = 0
for project_name in projects:
    print(project_name)

    Button(root, text=project_name, font=buttons_font, width=width_value, height=1, padx=1, pady=1, bg='#404040',
           activebackground="yellow", borderwidth=2, overrelief="solid",
           fg="#b3b300", command=lambda current_project=project_name:
        retrieve_input(current_project)).grid(row=1, column=index, rowspan=5, sticky='ew')
    index += 1


root.call('wm', 'attributes', '.', '-topmost', '1')

entry_text.trace("w", auto_uppercase)

if platform() == 'Darwin':
    system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')

root.mainloop()
