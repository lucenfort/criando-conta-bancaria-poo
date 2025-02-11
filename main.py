class ContaBancaria:
    def __init__(self, titular):
        # Inicialize a conta bancária com o nome do titular, saldo 0 e uma lista para armazenar as operações realizadas
        self.titular = titular
        self.saldo = 0
        self.operacoes = []

    def depositar(self, valor):
        # Adicione o valor ao saldo e registre a operação
        self.saldo += valor
        self.operacoes.append(f"+{valor}")

    def sacar(self, valor):
        # Verifique se há saldo suficiente para o saque
        if self.saldo + valor >= 0:  # valor já é negativo
            self.saldo += valor
            self.operacoes.append(str(valor))
        else:
            # Registre a operação e retorne a mensagem de saque negado
            self.operacoes.append("Saque não permitido")

    def extrato(self):
        # Exiba o extrato no formato correto, usando vírgulas como separadores
        operacoes_str = ", ".join(self.operacoes)
        print(f"Operações: {operacoes_str}; Saldo: {self.saldo}")

# Entrada e execução
nome_titular = input().strip()  
conta = ContaBancaria(nome_titular)  

entrada_transacoes = input().strip() 
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]  

for valor in transacoes:
    if valor > 0:
        conta.depositar(valor)  
    else:
        conta.sacar(valor)  

conta.extrato()
