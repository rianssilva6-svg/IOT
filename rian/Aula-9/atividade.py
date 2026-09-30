import customtkinter as ctk
ctk.set_appearance_mode('dark')

janela = ctk.CTk()
janela.geometry('600x450')
janela.resizable(False,False)
janela.title('Sistema Escolar 2026')
janela.iconbitmap('boletim.ico')

titulo = ctk.CTkLabel(janela,
                    text='Sistema Escola',
                    text_color="#e8eb5b",
                    font=('Verdana',45,'bold'),)
titulo.pack(pady=25)

nota1 = ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color='#e8eb5b',
                    placeholder_text='Digite a 1º nota da unidade')
nota1.pack(pady=10)

nota2 = ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color='#e8eb5b',
                    placeholder_text='Digite a 2º nota da unidade')
nota2.pack(pady=10)

nota3 = ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color='#e8eb5b',
                    placeholder_text='Digite a 3º nota da unidade')
nota3.pack(pady=10)

def gerarResultado():
    try:
        n1 = (float(nota1.get()))
        n2 = (float(nota2.get()))
        n3 = (float(nota3.get()))

        media = (n1+n2+n3) / 3

        if (media<5):
            resultado.configure(text=f'Reprovado!! Média: {media:.1f}', text_color='red')
        elif(media==5):
            resultado.configure(text=f'Recuperação!! Média: {media:.1f}',text_color='yellow')
        else:
            resultado.configure(text=f'Aprovado!! Média: {media:.1f}',text_color='green')

    except:
        resultado.configure(text='Digite um valor valido!!')

btn = ctk.CTkButton(janela,
                    width=150,
                    height=35,
                    text='Calcular Media',
                    fg_color="#918856",
                    text_color="#FFFFFF",
                    hover_color="#969738",
                    cursor='hand2',
                    border_width=2,
                    border_color='#e8eb5b',
                    font=('verdana',12, 'bold'),
                    command=gerarResultado)
btn.pack(pady=20)


resultado = ctk.CTkLabel(janela,
                        text='',
                        font=('verdana',18,'bold'))
resultado.pack(pady=10)

janela.mainloop()