from tkinter import *

CinzaClaro = '#e4e4e4'
Branco = '#fff'
AzulClaro = '#4089ff'

expressao = ''


def inserir_numero(numero):
    global expressao
    expressao += numero if len(label['text']) < 10 else ''
    label['text'] += numero if len(label['text']) < 10 else ''


def apagar_expressao():
    global expressao
    label['text'] = ''
    expressao = ''


def apagar_numero(evento):
    global expressao
    label['text'] = label['text'][:-1]
    expressao = expressao[:-1]


def adicionar_operacao(sinal):
    global expressao

    if len(expressao) != 0:
        label['text'] = ''
        if any(operador in expressao[-1] for operador in ['+', '-', '*', '/']):
            expressao = expressao[:-1]
        expressao = str(eval(expressao)) + sinal


def calcular():
    global expressao
    if len(expressao) != 0:
        if any(operador in expressao[-1] for operador in ['+', '-', '*', '/']):
            expressao = expressao[:-1]
        expressao = str(eval(expressao))
        label['text'] = expressao


janela = Tk()
janela.geometry('300x400')
janela.title('Calculadora')
janela.resizable(False, False)
janela.configure(bg=CinzaClaro)
janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=1)
janela.columnconfigure(2, weight=1)
janela.columnconfigure(3, weight=1)
janela.rowconfigure(1, weight=1)
janela.rowconfigure(2, weight=1)
janela.rowconfigure(3, weight=1)
janela.rowconfigure(4, weight=1)
janela.rowconfigure(5, weight=1)

label = Label(janela, text='', font='Arial 20', bg=Branco, relief='groove', borderwidth=1, width=1)
janela.bind('<BackSpace>', apagar_numero)
label.grid(row=0, column=0, columnspan=5, sticky='we', pady=5, padx=5)

botao_zero = Button(janela, text='0', relief='groove', bg=AzulClaro, font='Arial 12',
                    command=lambda: inserir_numero('0'))
botao_zero.grid(row=5, column=0, columnspan=2, sticky='nswe', padx=5, pady=5)

botao_um = Button(janela, text='1', relief='groove', bg=AzulClaro, font='Arial 12',
                  command=lambda: inserir_numero('1'))
botao_um.grid(row=4, column=2, sticky='nswe', padx=5, pady=5)

botao_dois = Button(janela, text='2', relief='groove', bg=AzulClaro, font='Arial 12',
                    command=lambda: inserir_numero('2'))
botao_dois.grid(row=4, column=1, sticky='nswe', padx=5, pady=5)

botao_tres = Button(janela, text='3', relief='groove', bg=AzulClaro, font='Arial 12',
                    command=lambda: inserir_numero('3'))
botao_tres.grid(row=4, column=0, sticky='nswe', padx=5, pady=5)

botao_quatro = Button(janela, text='4', relief='groove', bg=AzulClaro, font='Arial 12',
                      command=lambda: inserir_numero('4'))
botao_quatro.grid(row=3, column=0, sticky='nswe', padx=5, pady=5)

botao_cinco = Button(janela, text='5', relief='groove', bg=AzulClaro, font='Arial 12',
                     command=lambda: inserir_numero('5'))
botao_cinco.grid(row=3, column=1, sticky='nswe', padx=5, pady=5)

botao_seis = Button(janela, text='6', relief='groove', bg=AzulClaro, font='Arial 12',
                    command=lambda: inserir_numero('6'))
botao_seis.grid(row=3, column=2, sticky='nswe', padx=5, pady=5)

botao_sete = Button(janela, text='7', relief='groove', bg=AzulClaro, font='Arial 12',
                    command=lambda: inserir_numero('7'))
botao_sete.grid(row=2, column=0, sticky='nswe', padx=5, pady=5)

botao_oito = Button(janela, text='8', relief='groove', bg=AzulClaro, font='Arial 12',
                    command=lambda: inserir_numero('8'))
botao_oito.grid(row=2, column=1, sticky='nswe', padx=5, pady=5)

botao_nove = Button(janela, text='9', relief='groove', bg=AzulClaro, font='Arial 12',
                    command=lambda: inserir_numero('9'))
botao_nove.grid(row=2, column=2, sticky='nswe', padx=5, pady=5)

botao_igual = Button(janela, text='=', relief='groove', bg=AzulClaro, font='Arial 12',
                     command=calcular)
botao_igual.grid(row=5, column=2, columnspan=2, sticky='nswe', padx=5, pady=5)

botao_apagar = Button(janela, text='C', relief='groove', bg=AzulClaro, font='Arial 12',
                      command=apagar_expressao)
botao_apagar.grid(row=1, column=0, columnspan=3, sticky='nswe', padx=5, pady=5)

botao_divido = Button(janela, text='/', relief='groove', bg=AzulClaro, font='Arial 12',
                      command=lambda: adicionar_operacao('/'))
botao_divido.grid(row=1, column=3, sticky='nswe', padx=5, pady=5)

botao_vezes = Button(janela, text='X', relief='groove', bg=AzulClaro, font='Arial 12',
                     command=lambda: adicionar_operacao('*'))
botao_vezes.grid(row=2, column=3, sticky='nswe', padx=5, pady=5)

botao_menos = Button(janela, text='-', relief='groove', bg=AzulClaro, font='Arial 12',
                     command=lambda: adicionar_operacao('-'))
botao_menos.grid(row=3, column=3, sticky='nswe', padx=5, pady=5)

botao_mais = Button(janela, text='+', relief='groove', bg=AzulClaro, font='Arial 12',
                    command=lambda: adicionar_operacao('+'))
botao_mais.grid(row=4, column=3, sticky='nswe', padx=5, pady=5)

janela.mainloop()
