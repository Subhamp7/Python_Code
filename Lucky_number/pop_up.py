import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()
# the input dialog
def index_name(requirement):
    promt_req=("Enter the {} required number:").format(requirement)
    USER_INP = simpledialog.askstring(title="LUCKY",
                                      prompt=promt_req)
    print(("The {} number you entered is {} ").format(requirement,USER_INP))
    return int(USER_INP)

