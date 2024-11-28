import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve

def obter_dados_usuario():
    print("Digite os coeficientes da função objetivo (ex: 3x + 5y):")
    c1 = float(input("Coeficiente de x: "))
    c2 = float(input("Coeficiente de y: "))
    
    print("\nDigite o número de restrições:")
    num_restricoes = int(input())
    
    restricoes = []
    for i in range(num_restricoes):
        print(f"\nDigite os coeficientes e o valor da restrição {i+1} no formato ax + by <= c:")
        a = float(input("Coeficiente de x (a): "))
        b = float(input("Coeficiente de y (b): "))
        c = float(input("Valor à direita da desigualdade (c): "))
        restricoes.append((a, b, c))
    
    return c1, c2, restricoes

def desenhar_grafico(c1, c2, restricoes):
    x = np.linspace(0, 20, 400)
    y = np.linspace(0, 20, 400)
    X, Y = np.meshgrid(x, y)
    
    plt.figure(figsize=(10, 8))
    
    # Plotar as restrições
    for a, b, c in restricoes:
        if b != 0:
            y_reta = (c - a * x) / b
            plt.plot(x, y_reta, label=f'{a}x + {b}y <= {c}')
        else:
            x_reta = c / a
            plt.axvline(x=x_reta, color='red', linestyle='--', label=f'{a}x + {b}y <= {c}')
    
    # Plotar região viável
    for a, b, c in restricoes:
        if b != 0:
            plt.fill_between(x, 0, (c - a * x) / b, alpha=0.2)
    
    # Plotar a função objetivo
    z = c1 * X + c2 * Y
    plt.contour(X, Y, z, levels=20, cmap="coolwarm", alpha=0.5)
    
    plt.xlim(0, 20)
    plt.ylim(0, 20)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.title("Gráfico da Função Objetivo e Restrições")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()
    plt.show()

def main():
    c1, c2, restricoes = obter_dados_usuario()
    desenhar_grafico(c1, c2, restricoes)

if __name__ == "__main__":
    main()