# Variável para controle de saída
continuarPrograma = ''

# Funções de operações matemáticas
def adicao(a, b):
    return a + b

def subracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    else:
        return a / b

# Função calculadora, sempre retorna um valor
def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao.lower() == 'adição':
        return adicao(num1, num2)
    elif operacao == '-' or operacao.lower() == 'subtração':
        return subracao(num1, num2)
    elif operacao == '*' or operacao.lower() == 'multiplicação':
        return multiplicacao(num1, num2)
    elif operacao == '/' or operacao.lower() == 'divisão':
        return divisao(num1, num2)
    else:
        return "Operação inválida"

# Laço principal
while continuarPrograma.lower() != 'n':
    try:
        # Captura dos números e da operação desejada
        primeiroNumero = float(input("Informe o primeiro número: "))
        segundoNumero = float(input("Informe o segundo número: "))
        tipoOperacao = input("Escolha a operação (+, -, *, / ou adição, subtração, multiplicação, divisão): ")

        # Chama a função calculadora
        resultado = calculadora(primeiroNumero, segundoNumero, tipoOperacao)
        
        # Exibe o resultado
        print(f'O resultado da operação foi: {resultado}')

        # Pergunta se o usuário deseja continuar
        continuarPrograma = input("Deseja realizar outra operação? (S/N): ").strip()
    except ValueError:
        print("Erro: Por favor, insira um número válido.")
