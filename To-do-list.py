from tkinter import *

def add_todo():
    todo_item = entry_todo.get()
    if todo_item:
        listbox_todos.insert(END, todo_item)
        entry_todo.delete(0, END)

def delete_todo():
    try:
        index = listbox_todos.curselection()[0]
        listbox_todos.delete(index)
    except IndexError:
        pass

window = Tk()
window.geometry("700x700")
window.title("To-Do List App")

label_title = Label(window,
                    text="To-Do List",
                    font=("Arial", 30, "bold"),
                    fg="white",  
                    bg="navy",   
                    width=20,
                    height=2,
                    relief=RAISED)
label_title.pack(pady=20)

label_add_todo = Label(window,
                       text="Add Todo:",
                       font=("Arial", 20, "bold"),
                       fg="white",  
                       bg="purple")  
label_add_todo.place(x=10, y=150)

label_todos = Label(window,
                    text="Todos:",
                    font=("Arial", 20, "bold"),
                    fg="white",  
                    bg="green")  
label_todos.place(x=10, y=300)

entry_todo = Entry(window, font=("Arial", 16))
entry_todo.place(x=170, y=150, width=300)

button_add_todo = Button(window,
                         text="Add Todo",
                         bg="orange",
                         fg="black",
                         font=("Arial", 14),
                         command=add_todo,
                         relief=RAISED,
                         bd=3)
button_add_todo.place(x=470, y=150, width=100)

button_delete_todo = Button(window,
                            text="Delete Todo",
                            bg="red",
                            fg="white",
                            font=("Arial", 14),
                            command=delete_todo,
                            relief=RAISED,
                            bd=3)
button_delete_todo.place(x=590, y=150, width=110)

listbox_todos = Listbox(window, font=("Arial", 16), bg="lightgrey", selectbackground="lightblue")
listbox_todos.place(x=200, y=300, width=540, height=300)

window.mainloop()
