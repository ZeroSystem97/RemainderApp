import sys
import time
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter.messagebox import showinfo
from threading import Thread

def get_message():
    rmd_message = simpledialog.askstring("Remainder", "Enter a remainder message:")
    if rmd_message is None:
        return None
    return rmd_message

def get_timer():
    while True:
        rmd_timer = simpledialog.askstring("Timer", "Set a timer for remainder(m):")
        if rmd_timer is None:
            return None
        try:
            timer_value = int(rmd_timer)
            if timer_value <= 0:
                messagebox.showwarning("Incorrect Value", "To set a timer, you must use positive numbers.")
            else:
                return timer_value
        except ValueError:
            messagebox.showwarning("Incorrect Value", "You need to use numbers to set a timer.")

def print_message(rmd_message):
    if rmd_message:
        messagebox.showinfo("Remainder", rmd_message)
    else:
        messagebox.showwarning("No Remainder", "You didn't enter a remainder message!")

def reminder_thread(user_message, timer, root):
    while True:
        time.sleep(timer * 60)
        print_message(user_message)
        user_confirm = messagebox.askyesno("Confirmation", "Do you want to continue running remainder?")
        if not user_confirm:
            if not ask_cancel():
                root.deiconify()
                return
            root.quit()
            sys.exit()

def ask_cancel():
    return messagebox.askyesno("Confirm Exit", "Are you sure you want to cancel and exit?")

def main():
    root = tk.Tk()
    root.withdraw()

    user_message = get_message()
    if user_message is None:
        if not ask_cancel():
            root.deiconify()
            return
        messagebox.showinfo("Cancelled", "No remainder message was set. Exiting...")
        root.quit()
        sys.exit()

    timer = get_timer()
    if timer is None:
        if not ask_cancel():
            root.deiconify()
            return
        messagebox.showinfo("Cancelled", "No timer was set. Exiting...")
        root.quit()
        sys.exit()

    if user_message and timer:
        reminder = Thread(target=reminder_thread, args=(user_message, timer, root), daemon=True)
        reminder.start()

    root.mainloop()

if __name__ == "__main__":
    main()
