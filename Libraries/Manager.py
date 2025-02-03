import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import datetime

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f0f0")

        # List to hold tasks as dictionaries with name, priority, and due date
        self.tasks = []
        
        # Load tasks from file on startup
        self.load_tasks()

        # Set up the GUI
        self.setup_ui()

    def setup_ui(self):
        # Title label
        title_label = tk.Label(self.root, text="Task Manager", font=("Helvetica", 20, "bold"), bg="#f0f0f0", fg="#4CAF50")
        title_label.pack(pady=20)

        # Entry field for new tasks
        self.task_entry = tk.Entry(self.root, font=("Helvetica", 14), width=30, bd=2, relief="solid", fg="#333333")
        self.task_entry.pack(pady=10)

        # Priority Dropdown
        self.priority_var = tk.StringVar(self.root)
        self.priority_var.set("Low")  # Default priority
        priority_menu = tk.OptionMenu(self.root, self.priority_var, "Low", "Medium", "High")
        priority_menu.config(font=("Helvetica", 12), width=20)
        priority_menu.pack(pady=5)

        # Entry field for due date
        self.due_date_entry = tk.Entry(self.root, font=("Helvetica", 12), width=30, bd=2, relief="solid", fg="#333333")
        self.due_date_entry.insert(0, "YYYY-MM-DD")  # Default placeholder
        self.due_date_entry.pack(pady=5)

        # Add Task button
        add_task_button = tk.Button(self.root, text="Add Task", font=("Helvetica", 14), bg="#4CAF50", fg="white", command=self.add_task)
        add_task_button.pack(pady=10)

        # Task Listbox (shows tasks)
        self.task_listbox = tk.Listbox(self.root, font=("Helvetica", 12), height=8, width=40, bd=2, selectmode=tk.SINGLE, fg="#333333", bg="#FFFFFF")
        self.task_listbox.pack(pady=10)

        # Buttons for task actions
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=10)

        remove_task_button = tk.Button(button_frame, text="Remove Task", font=("Helvetica", 12), bg="#FF5722", fg="white", command=self.remove_task)
        remove_task_button.pack(side=tk.LEFT, padx=10)

        edit_task_button = tk.Button(button_frame, text="Edit Task", font=("Helvetica", 12), bg="#FFC107", fg="white", command=self.edit_task)
        edit_task_button.pack(side=tk.LEFT, padx=10)

        clear_all_button = tk.Button(self.root, text="Clear All", font=("Helvetica", 14), bg="#FF9800", fg="white", command=self.clear_all)
        clear_all_button.pack(pady=10)

        # Search Bar
        self.search_entry = tk.Entry(self.root, font=("Helvetica", 12), width=30, bd=2, relief="solid", fg="#333333")
        self.search_entry.insert(0, "Search tasks...")
        self.search_entry.bind("<KeyRelease>", self.search_task)
        self.search_entry.pack(pady=5)

    def add_task(self):
        task_name = self.task_entry.get().strip()
        priority = self.priority_var.get()
        due_date = self.due_date_entry.get().strip()

        if task_name != "":
            # Validate due date format (YYYY-MM-DD)
            try:
                datetime.datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                messagebox.showwarning("Invalid Date", "Please enter a valid due date (YYYY-MM-DD).")
                return

            task = {"name": task_name, "priority": priority, "due_date": due_date}
            self.tasks.append(task)
            self.update_task_listbox()
            self.clear_input_fields()
            self.save_tasks()
        else:
            messagebox.showwarning("Input Error", "Please enter a valid task.")

    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_task_listbox()
            self.save_tasks()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")

    def edit_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            selected_task = self.tasks[selected_task_index]
            
            new_task_name = simpledialog.askstring("Edit Task", "Enter new task name:", initialvalue=selected_task["name"])
            if new_task_name:
                selected_task["name"] = new_task_name

            new_priority = simpledialog.askstring("Edit Task", "Enter new priority (Low, Medium, High):", initialvalue=selected_task["priority"])
            if new_priority in ["Low", "Medium", "High"]:
                selected_task["priority"] = new_priority

            new_due_date = simpledialog.askstring("Edit Task", "Enter new due date (YYYY-MM-DD):", initialvalue=selected_task["due_date"])
            if new_due_date:
                try:
                    datetime.datetime.strptime(new_due_date, "%Y-%m-%d")
                    selected_task["due_date"] = new_due_date
                except ValueError:
                    messagebox.showwarning("Invalid Date", "Please enter a valid due date (YYYY-MM-DD).")
                    return

            self.update_task_listbox()
            self.save_tasks()

        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to edit.")

    def clear_all(self):
        confirm = messagebox.askyesno("Clear All", "Are you sure you want to clear all tasks?")
        if confirm:
            self.tasks.clear()
            self.update_task_listbox()
            self.save_tasks()

    def search_task(self, event):
        search_text = self.search_entry.get().lower()
        filtered_tasks = [task for task in self.tasks if search_text in task["name"].lower()]
        self.update_task_listbox(filtered_tasks)

    def update_task_listbox(self, filtered_tasks=None):
        self.task_listbox.delete(0, tk.END)
        tasks_to_show = filtered_tasks if filtered_tasks else self.tasks
        for task in tasks_to_show:
            display_text = f"{task['name']} | {task['priority']} | Due: {task['due_date']}"
            self.task_listbox.insert(tk.END, display_text)

    def clear_input_fields(self):
        self.task_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)
        self.due_date_entry.insert(0, "YYYY-MM-DD")

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task['name']}|{task['priority']}|{task['due_date']}\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    name, priority, due_date = line.strip().split("|")
                    self.tasks.append({"name": name, "priority": priority, "due_date": due_date})
        except FileNotFoundError:
            pass


# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
