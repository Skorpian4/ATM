import os,time

s_inicial = 400
s_atual = s_inicial

def retirar(s_atual,q):
    q = float(input('Indique a quantidade que deseja retirar: '))
    if q < 0 or q > s_atual:
        if q > s_atual:
            os.system('cls')
            print('Saldo insuficiente para retirar.')
            time.sleep(3)
            os.system('cls')
        else:
            os.system('cls')
            print('Não pode retirar quantidades negativas')
            time.sleep(3)
            os.system('cls')
    else:
        os.system('cls')
        s_atual = s_atual - q
        print('Quantidade retirada.')
        time.sleep(2)
        os.system('cls')
        return s_atual

def deposito(s_atual,dep):
    dep = float(input('Indique a quantidade que deseja depositar: '))
    if dep < 0:
        os.system('cls')
        print('Não pode depositar quantidades negativas')
        time.sleep(3)
        os.system('cls')
    else:
        os.system('cls')
        s_atual = s_atual + dep
        print('Ação bem sucedida.')
        time.sleep(2)
        os.system('cls')
        return s_atual
    
def saldo():
    print(f"Saldo atual: €{s_atual:.2f}")
    time.sleep(3)
    os.system('cls')
    pass

while True:
    print("1. Retirar dinheiro")
    print("2. Depositar dinheiro")
    print("3. Verificar Saldo")
    print("4. Encerrar")
    
    escolha = input("Escolha a opção desejada: ")
    
    if escolha == "1":
        retirar()
        pass
    elif escolha == "2":
        deposito()
        pass
    elif escolha == "3":
        saldo()
        pass
    elif escolha == "4":
        os.system('cls')
        print("Programa encerrado. Obrigado!")
        break
    else:
        os.system('cls')
        print("Opção inválida. Tente novamente.")
        time.sleep(3)
        os.system('cls')
