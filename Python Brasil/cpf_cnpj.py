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

    def valida_cpf(self, documento) -> bool:
        if len(documento) == 11:
            valida_cpf = CPF()
            return valida_cpf.validate(documento)

        return False

    def foramta_cpf(self) -> str:
        mascara = CPF()
        return mascara.mask(self.cpf)

    def valida_cnpj(self, documento) -> bool:
        if len(documento) == 14:
            valida_cnpj = CNPJ()
            return valida_cnpj.validate(documento)

        return False

    def foramta_cnpj(self) -> str:
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
