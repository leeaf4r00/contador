import PySimpleGUI as sg
import datetime
import sys

# Definir o layout da janela
layout = [
    [sg.Text('Insira os valores abaixo:')],
    [sg.Text('Tipo:'), sg.Radio('Cédula', 'tipo', key='tipo_cedula', enable_events=True),
     sg.Radio('Moeda', 'tipo', key='tipo_moeda', default=True, enable_events=True)],
    [sg.Text('Valor:'), sg.Combo(['R$2', 'R$5', 'R$10', 'R$20', 'R$50', 'R$100', 'R$200'], key='valor_cedula',
                                 visible=False), sg.Combo(['R$0.05', 'R$0.10', 'R$0.25', 'R$0.50', 'R$1'], key='valor_moeda', visible=True)],
    [sg.Text('Quantidade:'), sg.InputText(key='quantidade')],
    [sg.Button('Adicionar'), sg.Button('Apagar')],
    [sg.Text('')],
    [sg.Text('Relatório')],
    [sg.Text('Total de moedas: R$0.00', key='total_moedas')],
    [sg.Text('Total de cédulas: R$0.00', key='total_cedulas')],
    [sg.Button('Gerar Relatório'), sg.Button('Fechar')],
    [sg.Multiline('', key='relatorio', size=(50, 10), font='Courier')]
]

window = sg.Window('Controle de Moedas e Cédulas', layout)

# Variáveis globais
transacoes = []

# Funções
def validar_valor(valor):
    if not valor.startswith('R$'):
        sg.popup('Insira um valor válido')
        return None
    try:
        valor_num = float(valor.replace("R$", "").replace(",", "."))
    except ValueError:
        sg.popup('Insira um valor válido')
        return None
    return valor_num

def adicionar_transacao(tipo, valor, quantidade):
    global transacoes
    transacoes.append((tipo, valor, quantidade))

def apagar_transacao():
    global transacoes
    if transacoes:
        transacoes.pop()

def calcular_saldo():
    saldo_moedas = 0
    saldo_cedulas = 0
    for tipo, valor, quantidade in transacoes:
        if tipo == 'Moeda':
            saldo_moedas += quantidade * valor
        elif tipo == 'Cédula':
            saldo_cedulas += quantidade * valor
    return saldo_moedas, saldo_cedulas

def atualizar_selecao():
    if values['tipo_cedula']:
        window['valor_cedula'].update(visible=True)
        window['valor_moeda'].update(visible=False)
    else:
        window['valor_cedula'].update(visible=False)
        window['valor_moeda'].update(visible=True)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Fechar':
        break

    if event == 'tipo_cedula' or event == 'tipo_moeda':
        atualizar_selecao()

    elif event == 'Adicionar':
        tipo = 'Moeda' if values['tipo_moeda'] else 'Cédula'
        valor = values['valor_moeda'] if values['tipo_moeda'] else values['valor_cedula']
        valor = validar_valor(valor)
        if valor is None:
            continue
        quantidade = int(values['quantidade'])
        adicionar_transacao(tipo, valor, quantidade)
        saldo_moedas, saldo_cedulas = calcular_saldo()
        window['total_moedas'].update(f'Total de moedas: R${saldo_moedas:.2f}')
        window['total_cedulas'].update(
            f'Total de cédulas: R${saldo_cedulas:.2f}')

    elif event == 'Gerar Relatório':
        saldo_moedas, saldo_cedulas = calcular_saldo()
        relatorio = f'Total de moedas: R${saldo_moedas:.2f}\nTotal de cédulas: R${saldo_cedulas:.2f}\n\nDetalhes:\n'
        for tipo, valor, quantidade in transacoes:
            relatorio += f'{tipo} - {valor} - Quantidade: {quantidade}\n'
        window['relatorio'].update(relatorio)

    elif event == 'Apagar':
        apagar_transacao()
        saldo_moedas, saldo_cedulas = calcular_saldo()
        window['total_moedas'].update(f'Total de moedas: R${saldo_moedas:.2f}')
        window['total_cedulas'].update(
            f'Total de cédulas: R${saldo_cedulas:.2f}')

    elif event == 'Novo Caixa':
        transacoes = []
        saldo_moedas, saldo_cedulas = calcular_saldo()
        window['total_moedas'].update(f'Total de moedas: R${saldo_moedas:.2f}')
        window['total_cedulas'].update(
            f'Total de cédulas: R${saldo_cedulas:.2f}')

    elif event == 'Imprimir Relatório':
        pass
        # Implemente a função para imprimir relatório conforme sua necessidade

window.close()
