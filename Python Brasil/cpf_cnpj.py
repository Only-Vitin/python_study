from validate_docbr import CPF, CNPJ


class CpfCnpj:
    def __init__(self, documento) -> None:
        if self.valida_cpf(documento):
            self.cpf = documento
            print(f"CPF Válido: {self.foramta_cpf()}")
        elif self.valida_cnpj(documento):
            self.cnpj = documento
            print(f"CNPJ Válido: {self.foramta_cnpj()}")
        else:
            print("O documento inserido é inválido")

    def __str__(self) -> str:
        try:
            len(self.cpf)
            return self.foramta_cpf()
        except AttributeError:
            return self.foramta_cnpj()

    def valida_cpf(self, documento):
        if len(documento) == 11:
            valida_cpf = CPF()
            eh_valido = valida_cpf.validate(documento)
            return eh_valido

        return False

    def foramta_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def valida_cnpj(self, documento):
        if len(documento) == 14:
            valida_cnpj = CNPJ()
            eh_valido = valida_cnpj.validate(documento)
            return eh_valido

        return False

    def foramta_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
