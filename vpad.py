import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('Flow Editor')
main_application.wm_iconbitmap('icon.ico')

####################  MAIN MENU  ########################

main_menu = tk.Menu(main_application)


# file
file_menu = tk.Menu(main_menu,tearoff=0)

# file icons\
new_icon = tk.PhotoImage(file = 'icons/new.png')
open_icon = tk.PhotoImage(file = 'icons/open.png')
save_icon = tk.PhotoImage(file = 'icons/save.png')
save_as_icon = tk.PhotoImage(file = 'icons/save_as.png')
exit_icon = tk.PhotoImage(file = 'icons/exit.png')


#edit
edit_menu = tk.Menu(main_menu,tearoff=0)

#edit icons
copy_icon = tk.PhotoImage(file = 'icons/copy.png')
paste_icon = tk.PhotoImage(file = 'icons/paste.png')
cut_icon = tk.PhotoImage(file = 'icons/cut.png')
clear_all_icon = tk.PhotoImage(file = 'icons/clear_all.png')
find_icon = tk.PhotoImage(file = 'icons/find.png')


#view
view_menu = tk.Menu(main_menu,tearoff=0)

#view icons
tool_bar_icon = tk.PhotoImage(file = 'icons/tool_bar.png')
status_bar_icon = tk.PhotoImage(file = 'icons/status_bar.png')


#color theme
colortheme_menu = tk.Menu(main_menu,tearoff=0)

#colortheme icons
light_default_icon = tk.PhotoImage(file = 'icons/light_default.png')
light_plus_icon = tk.PhotoImage(file = 'icons/light_plus.png')
dark_icon = tk.PhotoImage(file = 'icons/dark.png')
red_icon = tk.PhotoImage(file = 'icons/red.png')
monokai_icon = tk.PhotoImage(file = 'icons/monokai.png')
night_blue_icon = tk.PhotoImage(file = 'icons/night_blue.png')

#color theme variable + color themes + color dictionary
theme_choice = tk.StringVar()
color_themes = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)
color_dict = {
    'Light Default ' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' :('#ededed', '#6b9dc2')
}


#cascade
main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label='Edit', menu=edit_menu)
main_menu.add_cascade(label='View', menu=view_menu)
main_menu.add_cascade(label='Color Theme', menu=colortheme_menu)


main_application.config(menu=main_menu)

#-------------------  END MAIN MENU  -------------------#


####################  TOOLBAR  ########################

tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill = tk.X)

#font box
font_tuple = tk.font.families()
font_keeper = tk.StringVar()
font_box = ttk.Combobox(tool_bar, textvariable=font_keeper, width=30, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0, column=0, padx=3, pady=1)



#size box
size_keeper = tk.IntVar()
size_box = ttk.Combobox(tool_bar, textvariable = size_keeper, width= 8, state='readonly')
size_box['values'] = tuple(range(1,81,2))
size_box.current(8)
size_box.grid(row=0, column=1, padx=6, pady=1)


#bold button
bold_icon = tk.PhotoImage(file='icons/bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=6, pady=1)

#italic button
italic_icon = tk.PhotoImage(file='icons/italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=6, pady=1)

#underline button
underline_icon = tk.PhotoImage(file='icons/underline.png')
underline_btn = ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=6, pady=1)

#font color button
font_color_icon = tk.PhotoImage(file='icons/font_color.png')
font_color_btn = ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0, column=5, padx=6, pady=1)

#align left
align_left_icon = tk.PhotoImage(file='icons/align_left.png')
align_left_btn = ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=6, pady=1)

#align center
align_center_icon = tk.PhotoImage(file='icons/align_center.png')
align_center_btn = ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=6, pady=1)

# align right

align_right_icon = tk.PhotoImage(file='icons/align_right.png')
align_right_btn = ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=6, pady=1)

#-------------------  END TOOLBAR  -------------------#


####################  TEXT EDITOR  ########################

text_editor = tk.Text()
text_editor.config(wrap='word', relief=tk.FLAT)

#scroll bar
scroll_bar = tk.Scrollbar()
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(expand=True, fill=tk.BOTH)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

#font family and font size functionality

current_font_family = 'Arial'
current_font_size = 17

def change_font(main_application): #you can also type (event=None)
    global current_font_family
    current_font_family = font_keeper.get()
    text_editor.configure(font=(current_font_family, current_font_size))

def change_size(main_application):
    global current_font_size
    current_font_size = size_keeper.get()
    text_editor.configure(font=(current_font_family, current_font_size))


font_box.bind('<<ComboboxSelected>>', change_font)
size_box.bind('<<ComboboxSelected>>', change_size)


#bold buton functionality

# print(tk.font.Font(font=text_editor).actual()) # prints {'family': 'Arial', 'size': 12, 'weight': 'normal', 'slant': 'roman', 'underline': 
# 0, 'overstrike': 0}

def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight']=='bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

bold_btn.configure(command=change_bold)

# italic button functionality

def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant']=='italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'roman'))

italic_btn.configure(command=change_italic)

#underline button functionality

def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']==0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline']==1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

underline_btn.configure(command=change_underline)

#font color functionality

# print(color_var) ((234.9140625, 87.33984375, 223.87109375), '#ea57df')
# first three rgb(combination of selected color) and the last one is chosen color.
# thatswhy the value is [1] in *fg=color_var[1]*
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command=change_font_color)    

# Allignment of buttons

# allign left
def allign_left():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'left')

align_left_btn.configure(command=allign_left)    

#allign center
def allign_center():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'center')

align_center_btn.configure(command=allign_center)  

#allign right
def allign_right():
    text_content = text_editor.get(1.0, 'end')
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, text_content, 'right')

align_right_btn.configure(command=allign_right)  

text_editor.configure(font=('Arial', 17))

#-------------------  END TEXT EDITOR  -------------------#


####################  STATUS BAR  ########################


status_bar = ttk.Label(main_application, text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed = False
def counter(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c'))#.replace(' ',''))----replaces spaces so that it can't be counted
        status_bar.config(text=(f'characters : {characters}, words : {words}'))
    text_editor.edit_modified(False)  # if this happens(agar text modified na hua to) then it will count whole length

text_editor.bind('<<Modified>>', counter)      


#-------------------  END STATUS BAR  -------------------#


####################  MAIN MENU FUNCTIONALITY  ########################
## variable
url = ''

# new functionality
def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)


# new menu functionality
file_menu.add_command(label='new', image=new_icon, compound=tk.LEFT, accelerator='ctrl + N', command=new_file )

# open functionality
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir = os.getcwd(), title ='Select File', filetypes=(('text', '*.txt'), ('all files', '*.*')) ) # ye last wale file naming ke right side ke combobox m aayenge
    try:
        with open(url, 'r')as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read()) #1.0 position se insert karna h...aur fr.read() ko insert krna h
    except FileNotFoundError:
        return
    except:  #any error ..just return
        return
    main_application.title(os.path.basename(url))  #user ke according opened file ka title rkha jayega  

#open menu functionality
file_menu.add_command(label='open', image=open_icon, compound=tk.LEFT, accelerator='ctrl + O', command=open_file)

#save functionality
def save_file(event=None):
    global url
    try:
        if url: # phle se hi saved flie opened ho to
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content) #no opening of asking save box
        else:
            url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('text file', '*.txt'), ('all files', '*.*')))
            content2=text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return

# save menu functionality
file_menu.add_command(label='save', image=save_icon, compound=tk.LEFT, accelerator='ctrl + S', command=save_file )

# save as functionality
def save_as_file(event=None):
    global url
    try:
        content = str(text_editor.get(1.0, tk.END))
        url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('text file', '*.txt'), ('all files', '*.*')))
        url.write(content)
        url.close()
    except:
        return

# save as menu functionality
file_menu.add_command(label='save_as', image=save_as_icon, compound=tk.LEFT, accelerator='ctrl + Alt + S', command = save_as_file) 

# exit functionality
def exit_file(event=None):
    global url, text_changed    
    try:
        if text_changed: #this was false before means its asking while zero edit
            mbox = messagebox.askyesnocancel('Warning!', 'Do you want to save this file?')
            if mbox is True: #means if mbox is yes
                if url:
                    content = str(text_editor.get(1.0, tk.END))
                    with open(url, 'w', encoding='utf-8')as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))        
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('text file', '*.txt'), ('all files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False: #means user selected no
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return

# exit menu functionality
file_menu.add_command(label='exit', image=exit_icon, compound=tk.LEFT, accelerator='ctrl + Q', command=exit_file)


#edit menu functionality
edit_menu.add_command(label='copy', image=copy_icon, compound=tk.LEFT, accelerator='ctrl + C',command=lambda:text_editor.event_generate('<Control c>'))
edit_menu.add_command(label='paste', image=paste_icon, compound=tk.LEFT, accelerator='ctrl + V',command=lambda:text_editor.event_generate('<Control v>'))
edit_menu.add_command(label='cut', image=cut_icon, compound=tk.LEFT, accelerator='ctrl + X',command=lambda:text_editor.event_generate('<Control x>'))
edit_menu.add_command(label='clear all', image=clear_all_icon, compound=tk.LEFT, accelerator='ctrl + Alt + X',command=lambda:text_editor.delete(1.0, tk.END)) 

# find functionality
def find_func(even=None):

    def find():
        word = find_index.get() 
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word: # if user has inputed something
            start_pos: '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos: #if no word founded
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos) 
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')

    def replace():
        word = find_index.get() 
        replace_text = replace_index.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, tk.END)



    find_dialog= tk.Toplevel() # toplevel to create a dialogbox
    find_dialog.geometry('450x250+500+200') #..+500+200 means area left from both sides
    find_dialog.title('Find')
    find_dialog.resizable(0,0) # for not resizing it

    ## frame
    find_frame = ttk.LabelFrame(find_dialog, text='Find/Replace')
    find_frame.pack(pady = 20)

    ##label
    find_label = ttk.Label(find_frame, text='Find : ')
    replace_label = ttk.Label(find_frame, text='Replace : ')

    #index
    find_index = ttk.Entry(find_frame, width= 30)
    replace_index = ttk.Entry(find_frame, width= 30)

    #button
    find_button = ttk.Button(find_frame, text='Find', command = find)
    replace_button = ttk.Button(find_frame, text='Replace', command = replace)

    #label grid
    find_label.grid(row=0, column = 0, padx = 4, pady = 4)
    replace_label.grid(row=1, column = 0, padx = 4, pady = 4)

    # entry grid
    find_index.grid(row=0, column = 1, padx = 4, pady = 4)
    replace_index.grid(row=1, column = 1, padx = 4, pady = 4)
    
    #button grid
    find_button.grid(row=2, column = 0, padx = 4, pady = 4)
    replace_button.grid(row=2, column = 1, padx = 4, pady = 4)

    find_dialog.mainloop()


# find menu functionality
edit_menu.add_command(label='find', image=find_icon, compound=tk.LEFT, accelerator='ctrl + F', command=find_func) 

# view menu functionality
show_toolbar = tk.BooleanVar()
show_toolbar.set(True) 
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)


def hide_toolbar():
    global show_toolbar 
    if show_toolbar: # if its showing
        tool_bar.pack_forget()
        show_toolbar = False
    else: # if you dont wanna show ..# saara kch fir se arrange krna hoga
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side = tk.TOP, fill = tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True
    
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False 
    else :
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True



view_menu.add_checkbutton(label='tool bar',onvalue=True, offvalue= False, variable=show_toolbar, image=tool_bar_icon, compound=tk.LEFT, command=hide_toolbar) 
view_menu.add_checkbutton(label='status bar', onvalue=True, offvalue= False, variable=show_statusbar, image=status_bar_icon, compound=tk.LEFT, command=hide_statusbar) 

# colortheme menu functionality

# Expanded way---

# colortheme_menu.add_radiobutton(label='light default', image=light_default_icon, compound=tk.LEFT)
# colortheme_menu.add_radiobutton(label='light plus', image=light_plus_icon, compound=tk.LEFT)
# colortheme_menu.add_radiobutton(label='dark', image=dark_icon, compound=tk.LEFT)
# colortheme_menu.add_radiobutton(label='clear all', image=red_icon, compound=tk.LEFT) 
# colortheme_menu.add_radiobutton(label='monokai', image=monokai_icon, compound=tk.LEFT) 
# colortheme_menu.add_radiobutton(label='night blue', image=night_blue_icon, compound=tk.LEFT) 

#color theme
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(bg=bg_color, fg=fg_color)
count= 0
for i in color_dict:
    colortheme_menu.add_radiobutton(label=i, image=color_themes[count], variable = theme_choice, compound=tk.LEFT, command=change_theme)
    count += 1

#-------------------  END MAIN MENU FUNCTIONALITY -------------------#

#bind shortcut keys

main_application.bind('<Control-n>', new_file)
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Alt-s>", save_as_file)
main_application.bind("<Control-q>", exit_file)
main_application.bind("<Control-f>", find_func)


main_application.mainloop() 