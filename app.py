import tkinter as tk
from tkinter import scrolledtext, messagebox
from sklearn.feature_extraction.text import TfidfVectorizer

def extract():
    text = input_box.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter text."); return
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf = vectorizer.fit_transform([text])
    keywords = sorted(zip(vectorizer.get_feature_names_out(), tfidf.toarray()[0]), key=lambda x: x[1], reverse=True)
    output_box.delete("1.0", tk.END)
    for word, score in keywords[:15]:
        output_box.insert(tk.END, f"{word}: {score:.4f}\n")

root = tk.Tk(); root.title("Keyword Extractor"); root.geometry("700x550")
tk.Label(root, text="Keyword Extractor", font=("Arial", 18, "bold")).pack(pady=10)
tk.Label(root, text="Enter text:").pack(anchor="w", padx=15)
input_box = scrolledtext.ScrolledText(root, height=8, font=("Arial", 12)); input_box.pack(fill="both", expand=True, padx=15, pady=5)
tk.Button(root, text="Extract Keywords", command=extract, font=("Arial", 12, "bold"), bg="#2563eb", fg="white").pack(pady=10)
tk.Label(root, text="Top Keywords:").pack(anchor="w", padx=15)
output_box = scrolledtext.ScrolledText(root, height=8, font=("Consolas", 11)); output_box.pack(fill="both", expand=True, padx=15, pady=5)
root.mainloop()
