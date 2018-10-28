from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def make_file(event):
    import glob
    import os
    files = [name for name in glob.glob('*.pl')]
    files.append('quicksort.py')
    name = nameEntry.get()    #input('name is: ')#sys.argv[1]
    path = filedialog.askdirectory() +'/'+ name 
    os.mkdir(path)
    for file in files:
        content = open(file)
        name_file = path+'/'+file
        newfile = open(name_file,mode = 'x')
        for line in content:
            if 'aish' in line:
                newfile.write(line.replace('aish',name))
            elif 'Aish' in line:
                newfile.write(line.replace('Aish',name))
            else:
                newfile.write(line)
    os.remove(path+'/'+'quicksort.py')
    root.destroy()



root = Tk()

root.geometry("240x160")

root.resizable(width=False, height=False)

Label(root, text="Name").grid(row=0,column = 0,ipady = 20)

nameEntry = Entry(root)

nameEntry.grid(row = 0,column = 1)#side=LEFT,padx = 10)

#Label(root, text="Save at").grid(row=1,column = 0,ipady = 20)

#pathEntry = Entry(root)

#pathEntry.grid(row = 1,column = 1)

submitButton = Button(root, text= "Submit")

#Label(root,text = 'Example:').grid(row = 2, column = 0)
#Label(root,text = '/Users/aishgupta/Desktop').grid(row = 2, column = 1)
# When the left mouse button is clicked call the function get_sum
submitButton.bind("<Button-1>", make_file)

submitButton.grid(row = 3,column = 1)#pack(side = LEFT,fill = X)

Label(root, text = 'Aish Gupta').grid(row = 4,column = 1,pady = 50,sticky = E)

root.mainloop()