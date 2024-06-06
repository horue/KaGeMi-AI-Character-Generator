import customtkinter as ct
import google.generativeai as genai
from key import key 
import pyperclip

genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-pro')


def g(prompt, t1):
    final=model.generate_content(prompt)
    print(final.text)
    try:
        t1.delete('1.0', 'end')
        t1.insert(ct.END, text=final.text)
    except:
        t1.insert(ct.END, text=final.text)

def command(e1, e2, e3, e4, e5, t1):
    nome=e1.get()
    idade=e2.get()
    personalidade=e3.get()
    história=e4.get()
    dl=e5.get()
    if dl == "":
        dl = "English"
    prompt=(f'Create a character the best well write you can, this character is named {nome}, is {idade} years old, have the {personalidade} personality. Write a background story that is {história}. The story must written be in {dl}')
    g(prompt, t1)

def save(e1, e2, e3, e4, e5, t1):
    if e1.get() == '':
        f = open(f"newfile.txt", "w")
        if t1.get(1.0, ct.END) == '':
            f.write("Woops! You forgot to click the Generate Button!")
        else:
            f.write(t1.get(1.0, ct.END))
    else:
        f = open(f"{e1.get()}.txt", "w")
        f.write(t1.get(1.0, ct.END))



def initial(root):
    l1=ct.CTkLabel(root, text="KaGeMi - AI Character Generator")
    l1.pack(pady=5)

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
    t1.pack(pady=15)

    
    b1=ct.CTkButton(root, text="Copy to clipboard", command=lambda:pyperclip.copy(t1.get(1.0, ct.END)))
    b1.pack(pady=10)

    b2=ct.CTkButton(root, text="Save as TXT", command=lambda:save(e1, e2, e3, e4, e5, t1))
    b2.pack()

def main():
    root = ct.CTk()
    root.geometry("650x700")
    root.title("KaGeMi - AI Character Generator")
    root.after(1, lambda :root.iconbitmap(r'Visual\KaGeMi-Icon_3.ico'))

    initial(root)
    
    root.iconify()
    root.update()
    root.deiconify()
    root.mainloop()

main()