import os
import time
os.system('cls')

while True:
    print("===== Lista de atividades =====\n"
        "1 - Maior e menor de idade\n"
        "2 - Verificar idade\n"
        "3 - Verificar temperatura\n"
        "4 - Maior e menor número\n"
        "5 - Crie uma senha\n"
        "6 - Numero par e impar\n"
        "7 - Verificar salário\n"
        "8 - Operação matemática\n"
        "9 - Finalizar Sistema\n")

    escolha = int(input("Escolha: "))

    match escolha:
        case 1:
            idade = 18
            if idade >= 18:
                print(f"Idade: {idade} - Maior de idade")
                time.sleep(3)
                os.system('cls')
            else:
                print(f"Idade: {idade} - Menor de idade")
                time.sleep(3)
                os.system('cls')
        
        case 2:
            os.system('cls')
            idade = int(input("Digite sua idade: "))
            if idade < 12:
                print("Criança")
                time.sleep(3)
                os.system('cls')
            elif idade >= 13 and idade <= 17:
                print("Adolescente")
                time.sleep(3)
                os.system('cls')
            elif idade >= 18 and idade <=58:
                print("Adulto")
                time.sleep(3)
                os.system('cls')
            elif idade > 60:
                print("Idoso")
                time.sleep(3)
                os.system('cls')
                
        case 3:
            os.system('cls')
            temperatura = int(input("Digite uma temperatura: "))
            if temperatura < 15:
                print("Está frio!!")
                time.sleep(3)
                os.system('cls')
            elif temperatura >=15 and temperatura <= 25:
                print("Está agradavel!!")
                time.sleep(3)
                os.system('cls')
            else:
                print("Está quente!!")
                time.sleep(3)
                os.system('cls')
                
        case 4:
            os.system('cls')
            num1 = int(input("Digite o 1° número: "))
            num2 = int(input("Digite o 2° número: "))
            
            if num1 > num2:
                print(f"O {num1} é maior que o {num2}")
                time.sleep(3)
                os.system('cls')
            else:
                print(f"O {num2} é maior que o {num1}")
                time.sleep(3)
                os.system('cls')
                
        case 5:
            os.system('cls')
            senha = input("Digite uma senha: ")
            if senha == "python123":
                print("Acesso Permitido")
                time.sleep(3)
                os.system('cls')
            else:
                print("Acesso Negado")
                time.sleep(3)
                os.system('cls')
                
        case 6:
            os.system('cls')
            num = int(input("Digite um número: "))
            if num %2 == 0:
                print("Numero par")
                time.sleep(3)
                os.system('cls')
            else:
                print("Numero impar")
                time.sleep(3)
                os.system('cls')
                
        case 7:
            os.system('cls')
            salario = float(input("Digite o valor do seu salário: "))
            if salario > 5000:
                print("Salário alto!!")
                time.sleep(3)
                os.system('cls')
            else:
                print("Salário dentro da media!!")
                time.sleep(3)
                os.system('cls')
                
        case 8:
            os.system('cls')
            num1 = int(input("Digite o 1° número: "))
            num2 = int(input("Digite o 2° número: "))
            
            print("Agora escolha uma operação matemática\n"
                "1 - Adição\n"
                "2 - Subtração\n"
                "3 - Multiplicação\n"
                "4 - Divisão\n")
            
            escolha = int(input("Escolha: "))
            
            match escolha:
                case 1:
                    soma = num1 + num2
                    print(f"A soma é {soma}")
                    time.sleep(3)
                    os.system('cls')
                case 2:
                    subtrair = num1 - num2
                    print(f"A subtração é {subtrair}")
                    time.sleep(3)
                    os.system
                case 3:
                    multiplicar = num1 * num2
                    print(f"A multiplicação é {multiplicar}")
                    time.sleep(3)
                    os.system('cls')
                case 4:
                    dividir = num1 / num2
                    print(f"A divisão é {dividir}")
                    time.sleep(3)
                    os.system('cls')
        case 9:
            break
        case _:
            print("valor invalido")
