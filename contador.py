from tkinter import *
import sqlite3
import tkinter as tk

root = Tk()

conn = sqlite3.connect('controle_moedas_cedulas.db')
cursor = conn.cursor()

# Criar tabela se não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS MOEDAS
                    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                     DESCRICAO TEXT NOT NULL,
                     QUANTIDADE INT NOT NULL,
                     VALOR REAL NOT NULL);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS CEDULAS
                    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                     DESCRICAO TEXT NOT NULL,
                     QUANTIDADE INT NOT NULL,
                     VALOR REAL NOT NULL);''')

conn.commit()


def contar_moedas():
    valores = [0.01, 0.05, 0.10, 0.25, 0.50, 1.00]
    total = 0.0
    for i in range(6):
        quantidade = int(
            input("Digite a quantidade de moedas de %.2f:" % valores[i]))
        total += quantidade * valores[i]
        # Insere ou atualiza o registro no banco de dados
        cursor.execute("SELECT * FROM MOEDAS WHERE DESCRICAO=?",
                       ('MOEDA DE %.2f' % valores[i],))
        result = cursor.fetchone()
        if result is None:
            cursor.execute("INSERT INTO MOEDAS (DESCRICAO, QUANTIDADE, VALOR) VALUES (?, ?, ?)",
                           ('MOEDA DE %.2f' % valores[i], quantidade, valores[i]))
        else:
            cursor.execute("UPDATE MOEDAS SET QUANTIDADE=?, VALOR=? WHERE DESCRICAO=?",
                           (quantidade, valores[i], 'MOEDA DE %.2f' % valores[i]))
        conn.commit()
    return total


def contar_cedulas():
    valores = [2, 5, 10, 20, 50, 100, 200]
    total = 0.0
    for i in range(7):
        quantidade = int(
            input("Digite a quantidade de cedulas de R$%d:" % valores[i]))
        total += quantidade * valores[i]
        # Insere ou atualiza o registro no banco de dados
        cursor.execute("SELECT * FROM CEDULAS WHERE DESCRICAO=?",
                       ('CEDULA DE R$%d' % valores[i],))
        result = cursor.fetchone()
        if result is None:
            cursor.execute("INSERT INTO CEDULAS (DESCRICAO, QUANTIDADE, VALOR) VALUES (?, ?, ?)",
                           ('CEDULA DE R$%d' % valores[i], quantidade, valores[i]))
        else:
            cursor.execute("UPDATE MOEDAS SET QUANTIDADE=?, VALOR=? WHERE DESCRICAO=?",
                           (quantidade, valores[i], 'CEDULA DE R$%d' % valores[i]))
        conn.commit()
    return total


def inserir_moeda():
    descricao = moeda_text.get()
    quantidade = int(quantidade_text.get())
    valor = float(valor_text.get())
    cursor.execute("SELECT * FROM MOEDAS WHERE DESCRICAO=?", (descricao,))
    result = cursor.fetchone()
    if result is None:
        cursor.execute("INSERT INTO MOEDAS (DESCRICAO, QUANTIDADE, VALOR) VALUES (?, ?, ?)",
                       (descricao, quantidade, valor))
    else:
        cursor.execute("UPDATE MOEDAS SET QUANTIDADE=?, VALOR=? WHERE DESCRICAO=?",
                       (quantidade, valor, descricao))
    conn.commit()
    moeda_text.delete(0, END)
    quantidade_text.delete(0, END)
    valor_text.delete(0, END)


def inserir_cedula():
    descricao = cedula_text.get()
    quantidade = int(quantidade_cedula_text.get())
    valor = float(valor_cedula_text.get())
    cursor.execute("SELECT * FROM CEDULAS WHERE DESCRICAO=?", (descricao,))
    result = cursor.fetchone()
    if result is None:
        cursor.execute("INSERT INTO CEDULAS (DESCRICAO, QUANTIDADE, VALOR) VALUES (?, ?, ?)",
                       (descricao, quantidade, valor))
    else:
        cursor.execute("UPDATE CEDULAS SET QUANTIDADE=?, VALOR=? WHERE DESCRICAO=?",
                       (quantidade, valor, descricao))
    conn.commit()
    cedula_text.delete(0, END)
    quantidade_cedula_text.delete(0, END)
    valor_cedula_text.delete(0, END)


def gerar_relatorio():
    conn = sqlite3.connect('controle_moedas_cedulas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM MOEDAS")
    moedas = cursor.fetchall()

    cursor.execute("SELECT * FROM CEDULAS")
    cedulas = cursor.fetchall()

    conn.close()

    total_moedas = sum([m[2] * m[3] for m in moedas])
    total_cedulas = sum([c[2] * c[3] for c in cedulas])

    print(f"Total de moedas: R${total_moedas:.2f}")
    print(f"Total de cédulas: R${total_cedulas:.2f}")

    root_relatorio = tk.Tk()
    root_relatorio.title("Relatório")
    root_relatorio.geometry("300x150")

    label_moedas = Label(
        root_relatorio, text=f"Total de moedas: R${total_moedas:.2f}")
    label_moedas.pack()

    label_cedulas = Label(
        root_relatorio, text=f"Total de cédulas: R${total_cedulas:.2f}")
    label_cedulas.pack()

    root_relatorio.mainloop()


root = Tk()
root.title("Controle de Moedas e Cédulas")
root.geometry("300x300")

label_instrucao = Label(root, text="Insira os valores abaixo:")
label_instrucao.grid(row=0, column=0, columnspan=2)

label_moeda = Label(root, text="Moeda:")
label_moeda.grid(row=1, column=0)

label_quantidade = Label(root, text="Quantidade:")
label_quantidade.grid(row=1, column=1)

label_valor = Label(root, text="Valor:")
label_valor.grid(row=1, column=2)

moeda_text = Entry(root)
moeda_text.grid(row=2, column=0)

quantidade_text = Entry(root)
quantidade_text.grid(row=2, column=1)
label_moeda = Label(root, text="Moeda:")
label_moeda.grid(row=1, column=0)

label_quantidade = Label(root, text="Quantidade:")
label_quantidade.grid(row=1, column=1)

label_valor = Label(root, text="Valor:")
label_valor.grid(row=1, column=2)

moeda_text = Entry(root)
moeda_text.grid(row=2, column=0)

quantidade_text = Entry(root)
quantidade_text.grid(row=2, column=1)

valor_text = Entry(root)
valor_text.grid(row=2, column=2)

botao_moeda = Button(root, text="Inserir moeda", command=inserir_moeda)
botao_moeda.grid(row=3, column=2)
valor_text = Entry(root)
valor_text.grid(row=2, column=2)

botao_moeda = Button(root, text="Inserir moeda", command=inserir_moeda)
botao_moeda.grid(row=3, column=2)

label_cedula = Label(root, text="Cédula:")
label_cedula.grid(row=4, column=0)

label_quantidade_cedula = Label(root, text="Quantidade:")
label_quantidade_cedula.grid(row=4, column=1)

label_valor_cedula = Label(root, text="Valor:")
label_valor_cedula.grid(row=4, column=2)

cedula_text = Entry(root)
cedula_text.grid(row=5, column=0)

quantidade_cedula_text = Entry(root)
quantidade_cedula_text.grid(row=5, column=1)

valor_cedula_text = Entry(root)
valor_cedula_text.grid(row=5, column=2)

botao_cedula = Button(root, text="Inserir cédula", command=inserir_cedula)
botao_cedula.grid(row=6, column=2)

botao_relatorio = Button(root, text="Gerar relatório",
                         command=gerar_relatorio)
botao_relatorio.grid(row=7, column=1)

root.mainloop()
