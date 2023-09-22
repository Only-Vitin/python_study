import re
from abc import ABC, abstractmethod
from datetime import datetime


class Funcionario:
    def __init__(self, nome, cpf) -> None:
        self._nome = nome
        self._cpf = cpf
    
    def valida_cpf():
        pass
        
    def cadastra_produto():
        pass
    
    def deleta_produto():
        pass

class Produtos(ABC):
    def __init__(self, nome, categoria, codigo, preco) -> None:
        self._nome = self.trata_texto(nome)
        self._categoria = self.trata_texto(categoria)
        self.codigo = codigo
        self.preco = preco
        self.valida_codigo(codigo)

    @abstractmethod
    def __str__(self) -> str:
        pass
    
    def trata_texto(self, texto):
        texto = texto.strip()
        return texto.title()
    
    def valida_codigo(self):
        padrao_codigo = re.compile("[0-9{4}][-][0-9{4}][-][0-9{4}]")
        match = padrao_codigo.match(self.codigo)
        if not match:
            print("Código errado, por favor digite novamente!")
            
            
class Alimentos(Produtos):
    def __init__(self, nome, categoria, codigo, preco, validade) -> None:
        super().__init__(nome, categoria, codigo, preco)
        self._validade = validade
        self.valida_validade(validade)

    def __str__(self) -> str:
        return f"Produto: {self._nome} - Tipo: {self._categoria} - Código: {self.codigo} - Preço: RS:{self.preco} - Validade: {self._validade}"

    def valida_validade(self, validade):
        try:
            data_validade = datetime.strptime(validade, '%d/%m/%Y')
            data_atual = datetime.now()
            if data_validade < data_atual:
                print("Atenção: Data de validade inválida! A data já passou.")
        except ValueError:
            print("Atenção: Data inválida! Por favor, tente novamente.")
            
            
class ProdutosDeLimpeza(Produtos):
    def __init__(self, nome, categoria, codigo, preco, aroma) -> None:
        super().__init__(nome, categoria, codigo, preco)
        self._aroma = aroma

    def __str__(self) -> str:
        return f"Produto: {self._nome} - Tipo: {self._categoria} - Código: {self.codigo} - Preço: RS:{self.preco} - Aroma: {self._aroma}"
