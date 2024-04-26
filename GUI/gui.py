import customtkinter as ct

def initial(root):
    e1=ct.CTkEntry(root, placeholder_text="Character name")
    e1.pack(pady=10)

    e2=ct.CTkEntry(root, placeholder_text="Character age")
    e2.pack(pady=10)

    e3=ct.CTkEntry(root, placeholder_text="Character personality")
    e3.pack(pady=10)

    e4=ct.CTkEntry(root, placeholder_text="Background")
    e4.pack(pady=10)

    b1=ct.CTkButton(root, text="Generate")
    b1.pack()


    print(1)


def main():
    root = ct.CTk()
    root.geometry("600x590")
    root.title("Character Generator")

    initial(root)
    
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

main()