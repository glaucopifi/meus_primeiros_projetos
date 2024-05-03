import tkinter as tk  # Importar Tkinter
from tkinter import messagebox
import pyqrcode  # Para criar QR Codes
import os  # Para verificar arquivos no sistema

# Função para criar o QR Code a partir da URL inserida pelo usuário
def create_qr():
    # Obter a URL do campo de entrada
    linkedin_url = url_entry.get()

    # Verificar se o usuário inseriu algo
    if not linkedin_url:
        messagebox.showerror("Erro", "Por favor, insira uma URL do LinkedIn.")
        return

    # Criar o QR Code
    qr = pyqrcode.create(linkedin_url)

    # Salvar o QR Code como arquivo PNG
    filename = "C:\\Users\\glauc\\PYTHON\\meus_primeiros_projetos.png"

    qr.png(filename, scale=8)

    # Verificar se o arquivo foi criado e notificar o usuário
    if os.path.exists(filename):
        messagebox.showinfo("Sucesso", f"QR Code gerado e salvo como '{filename}'")
    else:
        messagebox.showerror("Erro", "O QR Code não pôde ser gerado.")

# Criar a janela principal
root = tk.Tk()  # Instanciar o objeto Tkinter
root.title("Gerador de QR Code para LinkedIn")

# Criar um rótulo para o campo de entrada
url_label = tk.Label(root, text="Entre com seu URL do LinkedIn:")
url_label.pack(pady=10)  # 'pack' para posicionar o widget na tela com espaço de 10 pixels

# Criar um campo de entrada para a URL
url_entry = tk.Entry(root, width=50)  # 'width' para definir o tamanho do campo de texto
url_entry.pack(pady=10)

# Criar um botão para gerar o QR Code
generate_button = tk.Button(root, text="Gerar QR Code", command=create_qr)  # Define a função que será chamada quando o botão for pressionado
generate_button.pack(pady=10)

# Iniciar o loop de eventos da interface gráfica
root.mainloop()  # Mantém a janela aberta para interações do usuário
