import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Função para resolver equações de primeiro grau
def resolver_primeiro_grau(a, b):
    x = sp.Symbol('x')
    eq = a * x + b
    solucao = sp.solve(eq, x)
    return solucao

# Função para resolver equações de segundo grau
def resolver_segundo_grau(a, b, c):
    x = sp.Symbol('x')
    eq = a * x**2 + b * x + c
    solucoes = sp.solve(eq, x)
    return solucoes

# Função para resolver equações de terceiro grau
def resolver_terceiro_grau(a, b, c, d):
    x = sp.Symbol('x')
    eq = a * x**3 + b * x**2 + c * x + d
    solucoes = sp.solve(eq, x)
    return solucoes

# Função para resolver equações de primeiro, segundo e terceiro grau digitadas pelo usuário
def resolver_equacao_usuario():
    tipo = input("Digite o tipo de equação (1 para primeiro grau, 2 para segundo grau, 3 para terceiro grau): ")
    x = sp.Symbol('x')
    try:
        if tipo == '1':
            a = float(input("Digite o coeficiente a: "))
            b = float(input("Digite o coeficiente b: "))
            eq = a * x + b
            solucao = sp.solve(eq, x)
            print("Solução da equação de primeiro grau:", solucao)
            plotar_grafico(eq)
        elif tipo == '2':
            a = float(input("Digite o coeficiente a: "))
            b = float(input("Digite o coeficiente b: "))
            c = float(input("Digite o coeficiente c: "))
            eq = a * x**2 + b * x + c
            solucoes = sp.solve(eq, x)
            print("Soluções da equação de segundo grau:", solucoes)
            plotar_grafico(eq)
        elif tipo == '3':
            a = float(input("Digite o coeficiente a: "))
            b = float(input("Digite o coeficiente b: "))
            c = float(input("Digite o coeficiente c: "))
            d = float(input("Digite o coeficiente d: "))
            eq = a * x**3 + b * x**2 + c * x + d
            solucoes = sp.solve(eq, x)
            print("Soluções da equação de terceiro grau:", solucoes)
            plotar_grafico(eq)
        else:
            print("Tipo de equação inválido. Digite 1, 2 ou 3.")
    except Exception as e:
        print("Erro ao interpretar a equação. Verifique os coeficientes.")
        print("Detalhes do erro:", e)

# Função para plotar o gráfico da equação
def plotar_grafico(equacao):
    x = sp.Symbol('x')
    f_lambdified = sp.lambdify(x, equacao, 'numpy')
    x_vals = np.linspace(-10, 10, 400)
    y_vals = f_lambdified(x_vals)

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=str(equacao))
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title('Gráfico da Equação')
    plt.grid(True)
    plt.legend()
    plt.show()

# Chama a função para resolver a equação digitada pelo usuário
resolver_equacao_usuario()