from tkinter import *
from tkinter import colorchooser,filedialog,ttk,font
from tkinter import messagebox
import os

# u=Image.open("save.png")
# u.save("save.ico")

root=Tk()
root.title("Text-Editor-By-Suraj")
root.geometry("1200x880")
#######################-------Creating Menu-------#######################
main_menu=Menu(root)
root.iconbitmap("save.ico")

############-------Add image for File -------############

new_icon=PhotoImage(file="new.png")
open_icon=PhotoImage(file="open.png")
save_icon=PhotoImage(file="save.png")
save_as_icon=PhotoImage(file="save_as.png")

############-------Creating  File Menu-------############

file_menu=Menu(main_menu,tearoff=0)
############-------Creating  New File Functionality-------############
url=''
def new_file(event=None):
    text_editor.delete(1.0,END)
file_menu.add_command(label="New",image=new_icon,compound=LEFT,command=new_file,accelerator='CRT+N')
############-------Creating  Open File Functionality-------############
def open_file(event=None):
    global url
    url=filedialog.askopenfilename(filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    with open(url,'r') as fr:
        root.title(os.path.basename(url))
        read=fr.read()
        text_editor.delete(1.0,END)
        text_editor.insert(1.0,read)
file_menu.add_command(label="Open",image=open_icon,compound=LEFT,command=open_file,accelerator='CRT+O')

############-------Creating  Save File Functionality-------############
def save_file(event=None):
    global url
    if url:
         with open(url,'w',encoding='utf-8') as frw:
            con=text_editor.get(1.0,END)
            frw.write(con)
    else:
        url=filedialog.asksaveasfilename( defaultextension='.txt',filetypes=(('Text Document,"*.txt'),("All Document,'*.*")))
        with open(url,'w') as fw:
            w=text_editor.get(1.0,END)
            fw.write(w)

file_menu.add_command(label="Save",image=save_icon,compound=LEFT,command=save_file,accelerator='CRT+S')
############-------Creating  Save As File Functionality-------############

def save_as(event=None):
    global url
    url=filedialog.asksaveasfilename( defaultextension='.txt',filetypes=(('Text Document,"*.txt'),("All Document,'*.*")))
    with open(url,'w') as sr:
        w2=text_editor.get(1.0,END)
        sr.write(w2)
file_menu.add_command(label="Save As",image=save_as_icon,compound=LEFT,command=save_as,accelerator='CRT+Alt+S')
main_menu.add_cascade(label="File",menu=file_menu)

############-------Add image for Edit -------############

copy_icon=PhotoImage(file="copy.png")
paste_icon=PhotoImage(file="paste.png")
cut_icon=PhotoImage(file="cut.png")
clear_all_icon=PhotoImage(file="edit_clear.png")

############-------Creating  Edit Menu-------############
edit_menu=Menu(main_menu,tearoff=0)
edit_menu.add_command(label="Copy",image=copy_icon,compound=LEFT,command=lambda:text_editor.event_generate("<Control c>"),accelerator='CRT+C')
edit_menu.add_command(label="Paste",image=paste_icon,compound=LEFT,command=lambda:text_editor.event_generate("<Control v>"),accelerator='CRT+V')
edit_menu.add_command(label="Cut",image=cut_icon,compound=LEFT,command=lambda:text_editor.event_generate("<Control x>",accelerator='CRT+X'))
edit_menu.add_command(label="Clear All",image=clear_all_icon,compound=LEFT,command=lambda:text_editor.delete(1.0,END))

main_menu.add_cascade(label="Edit",menu=edit_menu)

############-------Creating  Edit Menu-------############
def color():
    '''it is use for change the background color'''
    color_var=colorchooser.askcolor()
    text_editor.configure(bg=color_var[1])
main_menu.add_cascade(label="Color Theme",command=color)

def quitapp(event=None):
    p=text_editor.get(1.0,END)
    value=messagebox.askquestion("cancel",'Are You Want To Cancel Without Save?')
    
    if value=="no":
        global url
        url=filedialog.asksaveasfilename( defaultextension='.txt',filetypes=(('Text Document,"*.txt'),("All Document,'*.*")))
        with open(url,'w') as ns:
            text1=(text_editor.get(1.0,END))
            ns.write(text1)
    else:
        root.destroy()

def editor_detalis(event=None):
    messagebox.showinfo("Text-Editor-By-Suraj",'This Is A Simple Text Editor Using Python Devolped By Suraj Yadav')
main_menu.add_cascade(label="About Text-editor",command=editor_detalis)
main_menu.add_cascade(label="Exit",command=quitapp)


############-------Externail Function font family-------############
l=ttk.Label(root)
l.pack(fill=X)
font_family=StringVar()
font_family_style=ttk.Combobox(l,width=17,textvariable=font_family,state='readonly')
font_family_style['values']=styles=(font.families())
font_family_style.current(styles.index("Arial"))
font_family_style.grid(row=0,column=0,padx=5)

############-------Externail Function font size-------############

font_size=StringVar()
font_size_style=ttk.Combobox(l,textvariable=font_size,width=8,state='readonly')
font_size_style['values']=tuple(range(8,80,2))
font_size_style.current(3)
font_size_style.grid(row=0,column=1,padx=5)

############-------Externail Button Adding Image -------############
bold_icon=PhotoImage(file="Boldtext_1053.png")
italic_icon=PhotoImage(file="italictext_1051.png")
underline_icon=PhotoImage(file="Underline_icon-icons.com_55789.png")
color_icon=PhotoImage(file="color.png")
############-------Externail Function Button-------############

bold_btn=ttk.Button(l,image=bold_icon,)

############-------function for Bold Button -------############

def change_bold(event=None):
    '''This function change the text to Bold'''
    text_proparty=font.Font(font=text_editor['font'])
    if text_proparty.actual()['weight']=='normal':
        text_editor.configure(font=(font_family.get(),font_size.get(),'bold'))

    elif text_proparty.actual()['slant']=='italic':
        text_editor.configure(font=(font_family.get(),font_size.get(),'bold','italic'))
    else:
        text_editor.configure(font=(font_family.get(),font_size.get(),'normal'))
           
    

bold_btn.configure(command=change_bold)
bold_btn.grid(row=0,column=3,padx=5)

italic_btn=ttk.Button(l,image=italic_icon)

############-------function for italic Button -------############
def change_italic(event=None):
    
    '''This function change the text to italic'''
    text_proparty=font.Font(font=text_editor['font'])
    if text_proparty.actual()['slant']=='roman':
        text_editor.configure(font=(font_family.get(),font_size.get(),'italic'))
    else:
        text_editor.configure(font=(font_family.get(),font_size.get(),'roman'))


italic_btn.configure(command=change_italic)



italic_btn.grid(row=0,column=4,padx=5)

underline_btn=ttk.Button(l,image=underline_icon)

############--------Function for underline-------############
def change_underline(event=None):
    '''Function for underline'''
    text_propart=font.Font(font=text_editor['font'])
    if text_propart.actual()['underline']==0:
        text_editor.configure(font=(font_family.get(),font_size.get(),'underline'))
    else:
        text_editor.configure(font=(font_family.get(),font_size.get(),))


underline_btn.configure(command=change_underline)
underline_btn.grid(row=0,column=5,padx=5)


color_btn=ttk.Button(l,image=color_icon)
color_btn.grid(row=0,column=6)

############--------Functionlity For Color Button-------############
def color_change(event=None):
    '''it is use for change the text color''' 
    color_var=colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
color_btn.configure(command=color_change)

############-------Creating Text Editor-------############
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
text=StringVar()
text_editor=Text(root,yscrollcommand=scrollbar.set, )
text_editor.pack(expand=True,fill=BOTH)
text_editor.focus()
scrollbar.config(command=text_editor.yview)
############-------Change The Font Family Style And font Size Style-------############
current_font_family='Arial'
current_font_size=14
def change_font_family(event=None):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def change_font_size(event=None):
    global current_font_size
    current_font_size=font_size.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_size_style.bind("<<ComboboxSelected>>",change_font_size)
font_family_style.bind("<<ComboboxSelected>>",change_font_family)

root.config(menu=main_menu)

###########-------Creating Shortcut Key-------###########
root.bind("<Control-n>",new_file)
root.bind("<Control-o>",open_file)
root.bind("<Control-s>",save_file)
root.bind("<Control-Alt-s>",save_as)






root.mainloop()
