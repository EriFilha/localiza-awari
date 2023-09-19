class Categoria:
    def __init__(self, nome, descricao, tempo_para_100kmh):
        self.nome = nome
        self.descricao = descricao
        self.tempo_para_100kmh = tempo_para_100kmh

class Carro:
    def __init__(self, placa, ano, cor, modelo, quilometragem, valor_diario, observacao, categoria):
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.modelo = modelo
        self.quilometragem = quilometragem
        self.valor_diario = valor_diario
        self.observacao = observacao
        self.categoria = categoria

class Reserva:
    def __init__(self, codigo, cliente, carro, data_inicio, data_fim):
        self.codigo = codigo
        self.cliente = cliente
        self.carro = carro
        self.status = True
        self.data_inicio = data_inicio
        self.data_fim = data_fim

class Cliente:
    def __init__(self, nome, cpf, idade, data_nascimento, num_carteira_motorista, foto_carteira_motorista, ano_vencimento_carteira, endereco, telefone_contato, email):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.data_nascimento = data_nascimento
        self.num_carteira_motorista = num_carteira_motorista
        self.foto_carteira_motorista = foto_carteira_motorista
        self.ano_vencimento_carteira = ano_vencimento_carteira
        self.endereco = endereco
        self.telefone_contato = telefone_contato
        self.email = email

class Funcionario:
    def __init__(self, nome, cpf, idade, data_contratacao, salario, qtd_alugueis_realizados, status, telefone_contato):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.data_contratacao = data_contratacao
        self.salario = salario
        self.qtd_alugueis_realizados = qtd_alugueis_realizados
        self.status = status
        self.telefone_contato = telefone_contato

class Promocao:
    def __init__(self, titulo, descricao, data_validade):
        self.titulo = titulo
        self.descricao = descricao
        self.data_validade = data_validade

categoria_utilitario = Categoria("Utilitario", "Semi-novo", 2.0)

carro1 = Carro("DCH1234", 2022, "Preto", "Onix", 1000, 400, "incrível", categoria_utilitario)

print("Informações do Carro:")
print(f"Placa: {carro1.placa}")
print(f"Ano: {carro1.ano}")
print(f"Modelo: {carro1.modelo}")
