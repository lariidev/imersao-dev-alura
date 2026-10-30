# ==========================================
# CALCULADORA SIMPLES EM PYTHON (ORGANIZADA)
# ==========================================

# 1. FUNÇÕES PARA CADA OPERAÇÃO MATEMÁTICA
def adicao(x, y):
    """Retorna a soma de dois números."""
    return x + y

def subtracao(x, y):
    """Retorna a diferença entre dois números."""
    return x - y

def multiplicacao(x, y):
    """Retorna o produto de dois números."""
    return x * y

def divisao(x, y):
    """Retorna o quociente ou uma mensagem de erro se dividir por zero."""
    if y == 0:
        return "Erro: Não é possível dividir por zero!"
    return x / y

def porcentagem(x, y):
    """Retorna a porcentagem: calcula y% de x."""
    return (x * y) / 100

# 2. MENU PRINCIPAL E INTERAÇÃO COM O USUÁRIO
def calculadora():
    print("=" * 35)
    print("      CALCULADORA EM PYTHON        ")
    print("=" * 35)
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Porcentagem (%)")
    print("=" * 35)

    # 3. ENTRADA DA ESCOLHA DO USUÁRIO
    opcao = input("Escolha a operação desejada (1/2/3/4/5): ")

    # Validação simples da opção
    if opcao not in ['1', '2', '3', '4', '5']:
        print("Opção inválida! Digite um número de 1 a 5.")
        return

    # 4. ENTRADA DOS NÚMEROS (convertendo texto para float)
    num1 = float(input("Digite o primeiro número (ou valor base): "))
    num2 = float(input("Digite o segundo número (ou porcentagem %): "))

    # 5. EXECUÇÃO DA OPERAÇÃO BASEADA NA ESCOLHA
    if opcao == '1':
        resultado = adicao(num1, num2)
        print(f"\nResultado: {num1} + {num2} = {resultado}")

    elif opcao == '2':
        resultado = subtracao(num1, num2)
        print(f"\nResultado: {num1} - {num2} = {resultado}")

    elif opcao == '3':
        resultado = multiplicacao(num1, num2)
        print(f"\nResultado: {num1} * {num2} = {resultado}")

    elif opcao == '4':
        resultado = divisao(num1, num2)
        print(f"\nResultado: {num1} / {num2} = {resultado}")

    elif opcao == '5':
        resultado = porcentagem(num1, num2)
        print(f"\nResultado: {num2}% de {num1} = {resultado}")

# 6. INICIAR O PROGRAMA
if __name__ == "__main__":
    calculadora()
