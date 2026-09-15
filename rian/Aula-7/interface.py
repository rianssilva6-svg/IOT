import customtkinter as ctk
ctk.set_appearance_mode('dark')

# Janela --------------
janela = ctk.CTk()
janela.geometry('500x300')
janela.resizable(False, False)
janela.title('Sistema de Acesso - 2026')
janela.iconbitmap('security-protection-protect-key-password-login_108554.ico')
#---------------------

#Corpo da Janela -------------
titulo = ctk.CTkLabel(janela,
                    text='Sistema de Login',
                    text_color='#6cf56e',
                    font=('arial',50))

titulo.pack()


login = ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color='#6cf56e',
                    placeholder_text='Digite seu login',
                    )

login.pack(pady=30)



senha = ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color='#6cf56e',
                    placeholder_text='Digite sua senha',
                    show='•••')

senha.pack()


btn = ctk.CTkButton(janela,
                    width=150,
                    height=30,
                    text='Acessar',
                    fg_color="#4bb14c",
                    text_color='white',
                    hover_color="#3f8640",
                    cursor = 'hand2',
                    font=('arial',25))
btn.pack(pady=20)
#-----------------------------


janela.mainloop()