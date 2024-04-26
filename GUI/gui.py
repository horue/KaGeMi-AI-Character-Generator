import customtkinter as ct

def initial(root):
    e1=ct.CTkEntry(root, placeholder_text="Character name")
    e1.pack(pady=100, padx=100)

    e2=ct.CTkEntry(root, placeholder_text="Character age")
    e2.pack()
    print(1)


def main():
    root = ct.CTk()
    root.geometry("600x450")
    root.title("Character Generator")

    initial(root)
    
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

main()