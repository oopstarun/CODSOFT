from tkinter import *
from tkinter import messagebox

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        self.title_label = Label(self.root, text='To-Do List', font=('arial', 20, 'bold'), bg='orange', fg='black', borderwidth=2, relief="solid")
        self.title_label.grid(row=0, column=0, sticky="ew")

        self.entry_label = Label(self.root, text='Enter Items', font=('arial', 20, 'bold'), bg='orange', fg='black', borderwidth=2, relief="solid")
        self.entry_label.grid(row=1, column=0, sticky="ew")

        self.text = Text(self.root, bd=5, height=10, font=('arial', 12), borderwidth=2, relief="solid")
        self.text.grid(row=2, column=0, sticky="ew", padx=10, pady=10)

        self.items_label = Label(self.root, text='Items', font=('arial', 20, 'bold'), bg='orange', fg='black', borderwidth=2, relief="solid")
        self.items_label.grid(row=3, column=0, sticky="ew")

        self.main_text = Listbox(self.root, bd=5, height=10, font=("arial", 12), selectmode=SINGLE, borderwidth=2, relief="solid")
        self.main_text.grid(row=4, column=0, sticky="nsew", padx=10, pady=10)

        self.scrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.main_text.yview)
        self.scrollbar.grid(row=4, column=1, sticky="ns")
        self.main_text.config(yscrollcommand=self.scrollbar.set)

        self.add_button = Button(self.root, text="Add Task", font=('arial', 12, 'bold'), bg='orange', fg='black', command=self.add, borderwidth=2, relief="solid")
        self.add_button.grid(row=5, column=0, sticky="ew", padx=10, pady=5)

        self.update_button = Button(self.root, text="Update Task", font=('arial', 12, 'bold'), bg='orange', fg='black', command=self.update_task, borderwidth=2, relief="solid")
        self.update_button.grid(row=6, column=0, sticky="ew", padx=10, pady=5)

        self.delete_button = Button(self.root, text="Delete Task", font=('arial', 12, 'bold'), bg='orange', fg='black', command=self.delete, borderwidth=2, relief="solid")
        self.delete_button.grid(row=7, column=0, sticky="ew", padx=10, pady=5)

        self.load_tasks()

    def add(self):
        content = self.text.get(1.0, END).strip()
        if content:
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content + '\n')
            self.text.delete(1.0, END)

    def update_task(self):
        selected_index = self.main_text.curselection()
        if selected_index:
            content = self.text.get(1.0, END).strip()
            if content:
                self.main_text.delete(selected_index)
                self.main_text.insert(selected_index, content)
                with open('data.txt', 'r') as file:
                    lines = file.readlines()
                with open('data.txt', 'w') as file:
                    for line in lines:
                        if line.strip() != self.main_text.get(selected_index):
                            file.write(line)
                with open('data.txt', 'a') as file:
                    file.write(content + '\n')
                self.text.delete(1.0, END)
            else:
                messagebox.showwarning("Warning", "You must enter updated content.")
        else:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def delete(self):
        selected_index = self.main_text.curselection()
        if selected_index:
            item = self.main_text.get(selected_index)
            self.main_text.delete(selected_index)
            with open('data.txt', 'r') as file:
                lines = file.readlines()
            with open('data.txt', 'w') as file:
                for line in lines:
                    if line.strip() != item:
                        file.write(line)
        else:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def load_tasks(self):
        try:
            with open('data.txt', 'r') as file:
                for line in file:
                    self.main_text.insert(END, line.strip())
        except FileNotFoundError:
            pass

root = Tk()
ul = Todo(root)
root.mainloop()
