
import requests
import datetime
import pyjokes
from tkinter import *

class Tarefa:
    def __init__(self, descricao, data_hora):
        self.descricao = descricao
        self.data_hora = data_hora

    def executar(self):
        pass

class Lembrete(Tarefa):
    def executar(self):
        print(f"Lembrete: {self.descricao} - {self.data_hora}")

class InformacaoMeteorologica(Tarefa):
    def executar(self):
        temperatura = 25
        condicao = "Ensolarado"
        print(f"Informação Meteorológica: {condicao}, {temperatura}°C - {self.data_hora}")

class Piada(Tarefa):
    def executar(self):
        Piada = pyjokes.get_joke()
        print(Piada)

class AssistenteVirtual:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def executar_tarefas(self):
        for tarefa in self.tarefas:
            tarefa.executar()

# Exemplo de uso
if __name__ == "__main__":
    assistente = AssistenteVirtual()

    lembrete = Lembrete("Reunião importante", datetime.datetime(2023, 12, 1, 10, 0))
    info_meteorologica = InformacaoMeteorologica("Previsão do tempo", datetime.datetime(2023, 12, 1, 8, 0))
    piada = Piada("Contar uma piada", datetime.datetime.now())

    assistente.adicionar_tarefa(lembrete)
    assistente.adicionar_tarefa(info_meteorologica)
    assistente.adicionar_tarefa(piada)

    assistente.executar_tarefas()

janela = Tk()
janela.title("Assistente Virtual")
texto = Label(janela, text="Clique no botão para exibir as informações ")
texto.grid(column=0, row=0)
botao = Button(janela, text="informaçoes da Assistente", command=assistente.executar_tarefas)
botao.grid(column=0, row=1)
texto_info = Label(janela, print(assistene.executar_tarefas))
texto_info.grid(column=0, row=2)

janela.mainloop()