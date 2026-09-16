import customtkinter as ctk
ctk.set_appearance_mode('dark') # Definindo a cor do fundo

#Janela -----------
janela = ctk.CTk()
janela.geometry('1050x1050') # Definindo a dimensão
janela.resizable(False, False) # Impedir o usuario
janela.title('Calculadora de Viagem')
janela.iconbitmap('car_23964.ico')
#------------------

#Corpo da janela -----------
titulo = ctk.CTkLabel(janela,
                    text='APP VIAGEM',
                    text_color="#b0d3f0",
                    font=('Verdana',45,'bold'),) #Tipo, tamanho e formato
titulo.pack(pady=25)



distancia = ctk.CTkEntry(janela,
                        width=400,
                        height=40,
                        border_color='#b0d3f0',
                        placeholder_text='Digite a distância da viagem em KM')
distancia.pack(pady=10)



consumo = ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color='#b0d3f0',
                    placeholder_text='Digite o consumo do veículo')
consumo.pack(pady=10)

preco = ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color='#b0d3f0',
                    placeholder_text='Digite o preço atual do combustível')
preco.pack(pady=10)
#------------------------

# Função
def calcular():
    try:
        total = (int(distancia.get()) / float(consumo.get())) * float(preco.get())
        resultado.configure(text=f'Gasto total: R${total:.2f}')
    except:
        resultado.configure(text='Digite um valor válido!!')

# Botão para execução
btn = ctk.CTkButton(janela,
                    width=150,
                    height=35,
                    text='Calcular Gasto',
                    fg_color='#5f7485',
                    text_color="#FFFFFF",
                    hover_color="#43525f",
                    cursor='hand2',
                    border_width=2,
                    border_color='#ffffff',
                    font=('verdana',12, 'bold'),
                    command=calcular)
btn.pack(pady=20)


# A exibição do resultado
resultado = ctk.CTkLabel(janela,
                        text='',
                        font=('verdana',18,'bold'))
resultado.pack(pady=10)



janela.mainloop()