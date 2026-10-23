import customtkinter as ctk
import qrcode
from PIL import Image, ImageTk

ctk.set_appearance_mode('dark')

# jane -----------------
janela = ctk.CTk()
janela.geometry('400x500')
janela.title('Sistema Gerador de QRCODE')
janela.resizable(False,False)
# ----------------------------

imagem_qr = None



def gerar_qrcode():
    global imagem_qr
    texto = entrada.get()

    if(texto != ''):
        qr = qrcode.make(texto)
        qr = qr.resize((300,300))
        imagem_qr = ImageTk.PhotoImage(qr)
        resultado.configure(image=imagem_qr,text='')
    else:
        resultado.configure(text='Este campo não pode estar vazio!!',text_color='red')




# Elementos da Janela -----------------------------------
titulo = ctk.CTkLabel(janela,
                    text = 'Sistema Gerador de QRCODE',
                    text_color='yellow',
                    font=('Arial',25,'bold'))
titulo.pack(pady=10)
# --------------------------------------------------------


# Entrada -------------------
entrada = ctk.CTkEntry(janela,
                    width=300,
                    height=40,
                    placeholder_text='Digite a URL ou o PIX',
                    border_color='yellow')
entrada.pack(pady = 10)
# ----------------------------------


# Botão ---------------------------
btn = ctk.CTkButton(janela,
                    width=100,
                    height=20,
                    fg_color='white',
                    text='Gerar QRCODE',
                    text_color='black',
                    hover_color="#AEAEAE",
                    cursor= 'hand2',
                    command=gerar_qrcode)
btn.pack(pady=10)
# -----------------------------------------




# Resultado -------------------------------------
resultado = ctk.CTkLabel(janela,
                        text='')
resultado.pack(pady = 20)
# -------------------------------------------



janela.mainloop()
