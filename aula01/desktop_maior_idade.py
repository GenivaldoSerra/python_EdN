import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def verificar_idade():
    try:
        nome = nome_entry.get().strip()
        ano_nascimento = int(ano_entry.get().strip())

        if not nome:
            messagebox.showerror("Erro", "Por favor, digite seu nome.")
            return
        
        ano_atual = datetime.now().year

        if ano_nascimento > ano_atual:
            messagebox.showerror("Erro", "O ano de nascimento não pode ser maior que o ano atual.")
            return
        
        idade = ano_atual - ano_nascimento
        status = "maior" if idade >= 18 else "menor"

        mensagem = f"Olá {nome}, sua idade é {idade} anos. Você é {status} de idade."
        messagebox.showinfo("Resultado", mensagem)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um ano de nascimento válido.")

def limpar_campos():
    nome_entry.delete(0, tk.END)
    ano_entry.delete(0, tk.END)
    nome_entry.focus()

root = tk.Tk()
root.title("AVS - Age Verification System")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

titulo = tk.Label(root, text="Age Verification System", font=("Arial", 16, "bold"), bg="#f0f0f0")
titulo.pack(pady=20)

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

tk.Label(frame, text="Nome:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, sticky="w", padx=10, pady=5)
nome_entry = tk.Entry(frame, font=("Arial", 12), width=25)
nome_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Ano de Nascimento:", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, sticky="w", padx=10, pady=5)
ano_entry = tk.Entry(frame, font=("Arial", 12), width=25)
ano_entry.grid(row=1, column=1, padx=10, pady=5)

botao_verificar = tk.Button(
    root, 
    text="Verificar Idade", 
    font=("Arial", 12), 
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    padx=20,
    pady=5,
)
botao_verificar.pack(pady=20)

botao_limpar = tk.Button(
    root,
    text="Limpar Campos",
    font=("Arial", 12),
    bg="#f44336",
    fg="white",
    activebackground="#d32f2f",
    padx=20,
    pady=5,
)
botao_limpar.pack(pady=20)

rodape = tk.Label(root, text="© 2025 - AVS - Age Verification System", font=("Arial", 9), bg="#f0f0f0", fg="#888")
rodape.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
