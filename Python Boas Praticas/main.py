from fabrica_fila import FabricaFila


fila_normal = FabricaFila.get_fila("normal")
fila_normal.atualiza_fila()
fila_normal.atualiza_fila()
print(fila_normal.chama_cliente(3))
print(fila_normal.chama_cliente(4))

fila_prioritaria = FabricaFila.get_fila("prioritaria")
fila_prioritaria.atualiza_fila()
fila_prioritaria.atualiza_fila()
print(fila_prioritaria.chama_cliente(4))
print(fila_prioritaria.chama_cliente(5))
print(fila_prioritaria.estatistica("13/09/2023", "005", "detail"))
