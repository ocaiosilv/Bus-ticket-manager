import tkinter as tk
from tkinter import messagebox


class InterfaceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Viagens de Ônibus")
        self.root.geometry("600x400")

        self.frame_atual = None
        self.mostrar_menu_principal()

    def limpar_tela(self):
        if self.frame_atual:
            self.frame_atual.destroy()

    def mostrar_menu_principal(self):
        self.limpar_tela()
        self.frame_atual = tk.Frame(self.root, padx=20, pady=20)
        self.frame_atual.pack(expand=True, fill="both")

        tk.Label(self.frame_atual, text="SISTEMA DE VIAGENS", font=("Helvetica", 20, "bold")).pack(pady=20)

        tk.Button(self.frame_atual, text="Modo Administrador", width=25, height=2,
                  command=self.mostrar_tela_admin).pack(pady=10)

        tk.Button(self.frame_atual, text="Modo de Vendas", width=25, height=2,
                  command=self.mostrar_tela_vendas).pack(pady=10)

        tk.Button(self.frame_atual, text="Sair", width=25, height=2,
                  command=self.root.quit).pack(pady=10)

    def mostrar_tela_admin(self):
        self.limpar_tela()
        self.frame_atual = tk.Frame(self.root, padx=20, pady=20)
        self.frame_atual.pack(expand=True, fill="both")

        tk.Label(self.frame_atual, text="Tela do Administrador", font=("Helvetica", 16)).pack(pady=10)

        tk.Button(self.frame_atual, text="Adicionar Viagem").pack(pady=5, fill="x")
        tk.Button(self.frame_atual, text="Editar Viagem").pack(pady=5, fill="x")
        tk.Button(self.frame_atual, text="Remover Viagem").pack(pady=5, fill="x")

        tk.Button(self.frame_atual, text="Voltar", command=self.mostrar_menu_principal).pack(pady=20)

    def mostrar_tela_vendas(self):
        self.limpar_tela()
        self.frame_atual = tk.Frame(self.root, padx=20, pady=20)
        self.frame_atual.pack(expand=True, fill="both")

        tk.Label(self.frame_atual, text="Buscar Viagens", font=("Helvetica", 16)).pack(pady=10)

        tk.Label(self.frame_atual, text="Origem:").pack(anchor="w")
        entry_origem = tk.Entry(self.frame_atual)
        entry_origem.pack(fill="x", pady=5)

        tk.Label(self.frame_atual, text="Destino:").pack(anchor="w")
        entry_destino = tk.Entry(self.frame_atual)
        entry_destino.pack(fill="x", pady=5)

        def buscar():
            origem = entry_origem.get()
            destino = entry_destino.get()
            messagebox.showinfo("Resultado", f"Procurando viagens de {origem} para {destino}")

        tk.Button(self.frame_atual, text="Buscar", command=buscar).pack(pady=10)

        tk.Button(self.frame_atual, text="Voltar", command=self.mostrar_menu_principal).pack(pady=20)


# --- Ponto de Entrada ---
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceApp(root)
    root.mainloop()
