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

# 2. MENU PRINCIPAL E INTERAÇÃO COM O USUÁRIO
def calculadora():
    print("=" * 35)
    print("      CALCULADORA EM PYTHON        ")
    print("=" * 35)
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("=" * 35)

    # 3. ENTRADA DA ESCOLHA DO USUÁRIO
    opcao = input("Escolha a operação desejada (1/2/3/4): ")

    # Validação simples da opção
    if opcao not in ['1', '2', '3', '4']:
        print("Opção inválida! Digite um número de 1 a 4.")
        return

    # 4. ENTRADA DOS NÚMEROS (convertendo texto para float)
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # 5. EXECUÇÃO DA OPERAÇÃO BASEADA NA ESCOLHA
    if opcao == '1':
        resultado = adicao(num1, num2)
        print(f"
Resultado: {num1} + {num2} = {resultado}")

    elif opcao == '2':
        resultado = subtracao(num1, num2)
        print(f"
Resultado: {num1} - {num2} = {resultado}")

    elif opcao == '3':
        resultado = multiplicacao(num1, num2)
        print(f"
Resultado: {num1} * {num2} = {resultado}")

    elif opcao == '4':
        resultado = divisao(num1, num2)
        print(f"
Resultado: {num1} / {num2} = {resultado}")

# 6. INICIAR O PROGRAMA
if __name__ == "__main__":
    calculadora()