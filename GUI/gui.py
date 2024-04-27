import customtkinter as ct
import google.generativeai as genai
from key import key 
import pyperclip

genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-pro')


def g(prompt, t1):
  final=model.generate_content(prompt)
  print(final.text)
  t1.insert(ct.END, text=final.text)

def command(e1, e2, e3, e4, e5, t1):
    nome=e1.get()
    idade=e2.get()
    personalidade=e3.get()
    história=e4.get()
    dl=e5.get()
    if dl == "":
        dl = "English"

    prompt=(f'Create a character the best well write you can, this character is named {nome}, is {idade} have the {personalidade} personality. Write a background story that is {história}. The story must written be in {dl}')
    g(prompt, t1)



def initial(root):
    e1=ct.CTkEntry(root, placeholder_text="Character name")
    e1.pack(pady=10)

    e2=ct.CTkEntry(root, placeholder_text="Character age")
    e2.pack(pady=10)

    e3=ct.CTkEntry(root, placeholder_text="Character personality")
    e3.pack(pady=10)

    e4=ct.CTkEntry(root, placeholder_text="Background")
    e4.pack(pady=10)

    e5=ct.CTkEntry(root, placeholder_text="Desired Leanguage")
    e5.pack(pady=10)

    b1=ct.CTkButton(root, text="Generate", command=lambda:command(e1, e2, e3, e4, e5, t1))
    b1.pack(pady=10)

    t1=ct.CTkTextbox(root, height=290, width=520)
    t1.pack(pady=25)

    
    b1=ct.CTkButton(root, text="Copy to clipboard", command=lambda:pyperclip.copy(t1.get(1.0, ct.END)))
    b1.pack(pady=10)


    print(1)


def main():
    root = ct.CTk()
    root.geometry("650x700")
    root.title("KaGeMi - Gemini Powered Character Generator")

    initial(root)
    
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

main()