import tkinter as tk


def show_text():
    text = entry.get()
    print(f"Wprowadzony tekst: {text}")  # Wprowadzony tekst: sdfsdfsfsafsdfs


app = tk.Tk()
app.title("Pole wprowadzanie")

entry = tk.Entry(app)
entry.pack()

button = tk.Button(app, text="Pokaż tekst", command=show_text)

button.pack(side=tk.BOTTOM)

app.mainloop()
