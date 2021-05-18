import tkinter as tk
import tkinter.ttk as ttk
from KakuroSolver import *

row_data=None
column_data=None
blanks=None
blist=None
sum1 =None
constvar=None
res=None


def save_input():
    global row_data
    row_data=int(e1.get())
    global column_data
    column_data=int(e2.get())

    global blanks
    blanks=str(e3.get())
    blanks_list= blanks.split()
    map_object=map(int, blanks_list)
    global blist
    blist=list(map_object)
    text_box.delete(1.0, "end-1c")
    text_box.insert("end-1c", str("Rows "+ str(row_data)+"\n"+"Columns "+ str(column_data)+"\n"+"Blanks "+ str(blist)))

master = tk.Tk()
master.geometry("400x400")
# tk.Label(master, text=str3, pady=10,).grid(row=0)
tk.Label(master, text="Rows",pady=10).grid(row=0)
tk.Label(master, text="Columns").grid(row=1)
tk.Label(master, text="Blanks").grid(row=2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
text_box = tk.Text(master, width = 25, height = 10)
scrollb = ttk.Scrollbar(master, command=text_box.yview)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
text_box.grid(row = 3, column = 0, columnspan = 2)
tk.Button(master, text='Quit', command=master.quit).grid(row=6, column=0, sticky=tk.EW, pady=40)
tk.Button(master, text='Enter', command=save_input).grid(row=6, column=1, sticky=tk.EW, pady=40)

scrollb.grid(row=3, column=5, sticky='nsew')
text_box['yscrollcommand'] = scrollb.set

tk.mainloop()


print ("Rows ", row_data)
print ("Columns ", column_data)
print(blist)

rows=row_data
columns=column_data
kakuro = kakuro(rows,columns)
Add_Blanks(kakuro,blist)

def save_linput():
    global sum1
    sum1 = int(e1.get())
    global constvar
    constvar=str(e2.get())
    global res
    res = tuple(map(int, constvar.split(' '))) 
    Add_Constraint(kakuro,Game_Constraint(sum1,res))
    print (sum1,res)
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    # text_box2.delete(1.0, "end-1c")
    text_box2.insert("end-1c\n", str("Sum "+ str(sum1)+"\n"+"Columns "+ str(res)+"\n"))

saster = tk.Tk()
saster.geometry("400x400")
# str2=""
# tk.Label(saster, text=str2, pady=10,).grid(row=0)
tk.Label(saster, text="Sum", pady=10).grid(row=0)
tk.Label(saster, text="variable num").grid(row=1)
e1 = tk.Entry(saster)
e2 = tk.Entry(saster)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
text_box2 = tk.Text(saster, width = 25, height = 10)
scrollb = ttk.Scrollbar(saster, command=text_box2.yview)
text_box2.grid(row = 3, column = 0, columnspan = 2)

tk.Button(saster, text='Quit', command=saster.quit).grid(row=6, column=0, sticky=tk.EW, pady=40)
tk.Button(saster, text='Enter', command=save_linput).grid(row=6, column=1, sticky=tk.EW, pady=40)

scrollb.grid(row=3, column=5, sticky='nsew')
text_box2['yscrollcommand'] = scrollb.set

tk.mainloop()




# print()
# display(kakuro)
# if not Is_Solvable(kakuro):
#     print ("Not Solvable")
# puzzle1=backtrack(kakuro)
# if Is_Solved(puzzle1):
#     print ("\nPuzzle Solved\n")
#     display(puzzle1)
# else:
#     print ("Couldnt solve the puzzle")

# str1="This is the output screen.\nThe unsolved Puzzle, status and the solved puzzle \nwill be displayed here"


daster = tk.Tk()
daster.geometry("400x400")
# str=""
# tk.Label(daster, text=str1, pady=10,).grid(row=0)
tk.Label(daster, text="Output", pady=10,).grid(row=0)

text_box1 = tk.Text(daster, width = 40, height = 20)
scrollb = ttk.Scrollbar(daster, command=text_box1.yview)
text_box1.grid(row = 3, column = 1, columnspan = 5)
tk.Button(daster, text='Quit', command=daster.quit).grid(row=12, column=0, sticky=tk.EW, pady=40,)
scrollb.grid(row=3, column=6, sticky='nsew')
text_box1['yscrollcommand'] = scrollb.set

text_box1.delete(1.0, "end-1c")
text_box1.insert("end-1c", str(guidisplay(kakuro))+"\n")

print (guidisplay(kakuro))
if not Is_Solvable(kakuro):
    print ("Not Solvable")
    text_box1.insert("end-1c", "Not Solvable"+"\n")
puzzle1=backtrack(kakuro)
if Is_Solved(puzzle1):
    print ("\nPuzzle Solved\n")
    text_box1.insert("end-1c", "Puzzle Solved\n"+"\n")
    text_box1.insert("end-1c", str(guidisplay(kakuro))+"\n")
    display(puzzle1)
else:
    text_box1.insert("end-1c", "Couldn't solve the puzzle"+"\n")
    print ("Couldn't solve the puzzle")

tk.mainloop()
