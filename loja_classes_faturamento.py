class Loja:
    def __init__(self):
        self.valor_unit = {
            'coca': 1.50,
            'pepsi': 1.50,
            'fanta': 1.25,
            'tubaina': 1.00,
            'torresmo': 3.00,
            'pinga': 0.50,
            'pipa': 4.50,
            'bilhar': 0.25,
            'ovo_colorido': 2.00
        }
    
    def calcular_vendas(self):
        qtd_coca = int(input("Quantas cocas? "))
        qtd_pepsi = int(input("Quantas pepsi? "))
        qtd_fanta = int(input('Quantas fantas? '))
        qtd_tubaina = int(input('Quantas tubainas? '))
        qtd_torresmo = int(input('Quantos torresmos? '))
        qtd_pinga = int(input('Quantas pingas? '))
        qtd_pipa = int(input('Quantas pipas? '))
        qtd_bilhar = int(input('Quantas fichas de bilhar? '))
        qtd_ovo_colorido = int(input('Quantos ovos coloridos? '))
        
        valor_total_vendas = (
            qtd_torresmo * self.valor_unit['torresmo'] +
            qtd_tubaina * self.valor_unit['tubaina'] +
            qtd_bilhar * self.valor_unit['bilhar'] +
            qtd_coca * self.valor_unit['coca'] +
            qtd_fanta * self.valor_unit['fanta'] +
            qtd_ovo_colorido * self.valor_unit['ovo_colorido'] +
            qtd_pinga * self.valor_unit['pinga'] +
            qtd_pipa * self.valor_unit['pipa']
        )
        return valor_total_vendas
    
    def calcular_faturamento(self):
        valor_total_vendas = self.calcular_vendas()
        custo = int(input('Quanto foi gasto no mês? '))
        faturamento = valor_total_vendas - custo
        return faturamento
    
    def calcular_margem_lucro(self):
        valor_total_vendas = self.calcular_vendas()
        faturamento = self.calcular_faturamento()
        margem = valor_total_vendas / faturamento
        return margem

# Exemplo de uso:
loja = Loja()
valor_total_vendas = loja.calcular_vendas()
faturamento = loja.calcular_faturamento()
margem = loja.calcular_margem_lucro()

print('O valor total das vendas foi {} Reais. O valor total do custo da loja foi {} Reais. O faturamento da loja foi {} Reais. A margem de Lucro foi {} ' .format(valor_total_vendas, custo, faturamento, margem))
