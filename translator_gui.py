import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator

# Supported languages
languages = GoogleTranslator(source='auto', target='english').get_supported_languages(as_dict=True)

language_names = list(languages.keys())

# Function to perform translation
def translate_text():
    input_text = input_box.get("1.0", tk.END).strip()
    src_lang = source_lang_combo.get().lower()
    dest_lang = dest_lang_combo.get().lower()

    if not input_text:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Please enter some text.")
        return

    try:
        translated = GoogleTranslator(source=src_lang, target=dest_lang).translate(input_text)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, translated)
    except Exception as e:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, f"Error: {str(e)}")

# GUI setup
root = tk.Tk()
root.title("Google Translator (Python GUI)")
root.geometry("600x400")
root.resizable(False, False)

# Input Label & Box
tk.Label(root, text="Enter Text", font=('Arial', 12)).place(x=30, y=20)
input_box = tk.Text(root, height=5, width=65)
input_box.place(x=30, y=50)

# From Language
tk.Label(root, text="From Language", font=('Arial', 10)).place(x=30, y=160)
source_lang_combo = ttk.Combobox(root, values=language_names, width=30, state="readonly")
source_lang_combo.place(x=30, y=185)
source_lang_combo.set("english")

# To Language
tk.Label(root, text="To Language", font=('Arial', 10)).place(x=320, y=160)
dest_lang_combo = ttk.Combobox(root, values=language_names, width=30, state="readonly")
dest_lang_combo.place(x=320, y=185)
dest_lang_combo.set("hindi")

# Translate Button
tk.Button(root, text="Translate", font=('Arial', 12), command=translate_text).place(x=250, y=230)

# Output Label & Box
tk.Label(root, text="Translated Text", font=('Arial', 12)).place(x=30, y=270)
output_box = tk.Text(root, height=5, width=65)
output_box.place(x=30, y=300)

# Run the app
root.mainloop()
