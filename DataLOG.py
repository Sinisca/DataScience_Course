import matplotlib.pyplot as plt
import numpy as np

# Gerar dados aleatórios
x = np.random.rand(50)
y = np.random.rand(50)
sizes = 1000 * np.random.rand(50)
colors = np.random.rand(50)

# Criar o gráfico de dispersão
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5)

# Adicionar rótulos e título
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.title('Gráfico de dispersão com tamanho e cor personalizados')

# Adicionar barra de cores
colorbar = plt.colorbar()
colorbar.set_label('Valor da cor')

# Exibir o gráfico
plt.show()

#Gera arquivo imagem
plt.savefig('meu_grafico.jpg')