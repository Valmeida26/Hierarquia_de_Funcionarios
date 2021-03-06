#Hierarquia de funcionarios: um programa que printa a função dos funcionarios de uma empresa
#conforme seu cargo e registra a hora e data em que ele foi rodado.

from datetime import datetime

data_atual = datetime.now().strftime('%d-%m-%y')
hora_atual = datetime.now().strftime( '%H:%M:%S')


class Empresa:

    def __init__(self, nome):
        self.nome = nome


class Diretor(Empresa):

    def Contratos(self):
        print(self.nome, 'Sua agenda terá: Elaboração de contratos, e reuniões com o jurídico')

    def dias_de_trabalho_no_mes(self):
        print(self.nome, f'Defina os dias de trabalho dos colaboradores no mês de referente a data {data_atual}')


class Gestor(Empresa):

    def Liderar_equipe(self):
        print(self.nome, 'Faça uma reunião para motivar a equipe e traçar estratégias futuras.')

    def local_de_trabalho(self):
        print(self.nome, 'Fiscalize a organização e a produção de equipamentos nos locais de trabalho')

class Funcionario(Empresa):

    def fabrica(self):
        print(self.nome, 'Sua função é construir componentes de computadores')

    def escritorio(self):
        print(self.nome,'Você está encarregado de auxiliar em serviços de escritório')


class Colaborador:

    def __str__(self):
        return f"Olá, {self.nome}, Expediente de trabalho iniciado no dia {data_atual} as {hora_atual}"


class Gerente:

    def __str__(self):
        return f"Olá, {self.nome}, Expediente de trabalho iniciado no dia {data_atual} as {hora_atual}"


class Diretoria:

    def __str__(self):
        return f"Olá, {self.nome}, Expediente de trabalho iniciado no dia {data_atual} as {hora_atual}"


class diretor(Diretor, Diretoria):
    pass
vinicius = diretor("Vinicius")
vinicius.Contratos()
print(f'{vinicius}\n')

class gerente(Gestor, Gerente):
    pass
sandro = gerente("Sandro")
sandro.local_de_trabalho()
print(f'{sandro}\n')

class funcionario (Funcionario, Colaborador):
    pass
joao = funcionario("João")
joao.fabrica()
print(f'{joao}\n')










