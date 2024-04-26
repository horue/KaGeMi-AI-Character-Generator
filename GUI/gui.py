import customtkinter as ct
import google.generativeai as genai
from key import key 

genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-pro')


def g(prompt):
  final=model.generate_content(prompt)
  print(final.text)


def command(e1, e2, e3, e4):
    nome=e1.get()
    idade=e2.get()
    personalidade=e3.get()
    história=e4.get()

    prompt=(f'Create a character the best well write you can, this character is named {nome}, is {idade} have the {personalidade} personality. Write a background story that is {história}')
    g(prompt)



def initial(root):
    e1=ct.CTkEntry(root, placeholder_text="Character name")
    e1.pack(pady=10)

    e2=ct.CTkEntry(root, placeholder_text="Character age")
    e2.pack(pady=10)

    e3=ct.CTkEntry(root, placeholder_text="Character personality")
    e3.pack(pady=10)

    e4=ct.CTkEntry(root, placeholder_text="Background")
    e4.pack(pady=10)

    b1=ct.CTkButton(root, text="Generate", command=lambda:command(e1, e2, e3, e4))
    b1.pack(pady=10)

    t1=ct.CTkTextbox(root)
    t1.pack(pady=30)

    
    b1=ct.CTkButton(root, text="Copy to clipboard", command=lambda:print(1))
    b1.pack(pady=10)


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