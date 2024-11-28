import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Coeficientes da função objetivo (lucro por unidade)
c = [-16, -30, -50]  # Negativo porque o solver minimiza por padrão

# Restrições de desigualdade (Ax <= b)
A = [
    [3/12, 3.5/12, 5/12],    # Tempo de fabricação
    [4/12, 5/12, 8/12],      # Tempo de montagem
    [1/12, 1.5/12, 3/12],    # Tempo de testes
    [-1, 0, 0],              # Mínimo do modelo A
    [0, -1, 0],              # Mínimo do modelo B
    [0, 0, -1],              # Mínimo do modelo C
]

b = [
    120,  # Tempo de fabricação disponível
    160,  # Tempo de montagem disponível
    48,   # Tempo de testes disponível
    -20,  # Produção mínima do modelo A
    -120, # Produção mínima do modelo B
    -60,  # Produção mínima do modelo C
]

# Limites das variáveis (não negatividade e mínimos obrigatórios)
x_bounds = (0, None)
bounds = [x_bounds, x_bounds, x_bounds]

# Resolvendo o problema
res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")

# Fixando x_C para visualização (por exemplo, x_C = 60, mínimo obrigatório)
x_C = 60

# Restrições no plano x_A e x_B
x_A = np.linspace(0, 200, 400)
fabricacao = (120 - (5/12) * x_C - (3/12) * x_A) / (3.5/12)
montagem = (160 - (8/12) * x_C - (4/12) * x_A) / (5/12)
testes = (48 - (3/12) * x_C - (1/12) * x_A) / (1.5/12)

# Região viável (limitação superior)
fabricacao = np.maximum(fabricacao, 0)
montagem = np.maximum(montagem, 0)
testes = np.maximum(testes, 0)

# Plotando o gráfico
plt.figure(figsize=(10, 8))

# Restrição de fabricação
plt.plot(x_A, fabricacao, label="Tempo de Fabricação")
# Restrição de montagem
plt.plot(x_A, montagem, label="Tempo de Montagem")
# Restrição de testes
plt.plot(x_A, testes, label="Tempo de Testes")

# Marcando limites mínimos
plt.axvline(20, color='red', linestyle='--', label="Mínimo de A")
plt.axhline(120, color='green', linestyle='--', label="Mínimo de B")

# Solução ótima
if res.success:
    plt.scatter(res.x[0], res.x[1], color="purple", s=100, label="Solução Ótima")

# Configurações do gráfico
plt.xlim(0, 200)
plt.ylim(0, 200)
plt.xlabel("Produção do Modelo A (x_A)")
plt.ylabel("Produção do Modelo B (x_B)")
plt.title("Região Viável e Solução Ótima")
plt.legend()
plt.grid()
plt.show()

# Mostrar solução ótima no terminal
if res.success:
    print("Solução ótima encontrada!")
    print(f"Produção ótima do modelo A: {res.x[0]:.2f} unidades")
    print(f"Produção ótima do modelo B: {res.x[1]:.2f} unidades")
    print(f"Produção ótima do modelo C: {res.x[2]:.2f} unidades")
    print(f"Lucro máximo: ${-res.fun:.2f}")
else:
    print("O solver não conseguiu encontrar uma solução.")
