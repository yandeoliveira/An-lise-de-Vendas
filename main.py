import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
                             QDateEdit, QMessageBox)

# Função para carregar os dados


def carregar_dados():
    try:
        return pd.read_csv('vendas.csv')
    except FileNotFoundError:
        QMessageBox.critical(
            None, "Erro", "Arquivo vendas.csv não encontrado.")
        sys.exit()

# Função para mostrar o gráfico de vendas por período


def grafico_vendas_periodo(data_inicial, data_final):
    dados_vendas = carregar_dados()
    dados_vendas['data'] = pd.to_datetime(dados_vendas['data'])

    # Converter as datas para datetime
    data_inicial = pd.to_datetime(data_inicial)
    data_final = pd.to_datetime(data_final)

    dados_vendas = dados_vendas[(dados_vendas['data'] >= data_inicial) & (
        dados_vendas['data'] <= data_final)]

    if dados_vendas.empty:
        QMessageBox.warning(
            None, "Aviso", "Nenhum dado encontrado para o intervalo selecionado.")
        return

    vendas_por_data = dados_vendas.groupby(
        'data')['valor_venda'].sum().reset_index()

    plt.figure(figsize=(10, 5))
    plt.plot(vendas_por_data['data'],
             vendas_por_data['valor_venda'], marker='o')
    plt.title('Vendas por Período')
    plt.xlabel('Data')
    plt.ylabel('Valor Total de Vendas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Função para mostrar o gráfico de vendas por produto


def grafico_vendas_produto(data_inicial, data_final):
    dados_vendas = carregar_dados()
    dados_vendas['data'] = pd.to_datetime(dados_vendas['data'])

    # Converter as datas para datetime
    data_inicial = pd.to_datetime(data_inicial)
    data_final = pd.to_datetime(data_final)

    dados_vendas = dados_vendas[(dados_vendas['data'] >= data_inicial) & (
        dados_vendas['data'] <= data_final)]

    if dados_vendas.empty:
        QMessageBox.warning(
            None, "Aviso", "Nenhum dado encontrado para o intervalo selecionado.")
        return

    vendas_por_produto = dados_vendas.groupby(
        'produto')['valor_venda'].sum().reset_index()

    plt.figure(figsize=(10, 5))
    sns.barplot(x='produto', y='valor_venda', data=vendas_por_produto)
    plt.title('Vendas por Produto')
    plt.xlabel('Produto')
    plt.ylabel('Valor Total de Vendas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Função para exibir estatísticas resumidas


def exibir_estatisticas(data_inicial, data_final):
    dados_vendas = carregar_dados()
    dados_vendas['data'] = pd.to_datetime(dados_vendas['data'])

    # Converter as datas para datetime
    data_inicial = pd.to_datetime(data_inicial)
    data_final = pd.to_datetime(data_final)

    dados_vendas = dados_vendas[(dados_vendas['data'] >= data_inicial) & (
        dados_vendas['data'] <= data_final)]

    if dados_vendas.empty:
        QMessageBox.warning(
            None, "Aviso", "Nenhum dado encontrado para o intervalo selecionado.")
        return

    total_vendas = dados_vendas['valor_venda'].sum()
    media_vendas = dados_vendas['valor_venda'].mean()
    produto_mais_vendido = dados_vendas.groupby(
        'produto')['valor_venda'].sum().idxmax()

    estatisticas = f"Total de Vendas: R$ {total_vendas:.2f}\n" \
        f"Média de Vendas: R$ {media_vendas:.2f}\n" \
        f"Produto Mais Vendido: {produto_mais_vendido}"

    QMessageBox.information(None, "Estatísticas Resumidas", estatisticas)

# Classe principal da aplicação


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Análise de Vendas')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        label = QLabel('Selecione o intervalo de datas:')
        layout.addWidget(label)

        self.data_inicial = QDateEdit(self)
        self.data_inicial.setCalendarPopup(True)
        self.data_inicial.setDate(pd.to_datetime('2024-01-01'))
        layout.addWidget(self.data_inicial)

        self.data_final = QDateEdit(self)
        self.data_final.setCalendarPopup(True)
        self.data_final.setDate(pd.to_datetime('2024-12-31'))
        layout.addWidget(self.data_final)

        botao_grafico_periodo = QPushButton('Gráfico de Vendas por Período')
        botao_grafico_periodo.clicked.connect(lambda: grafico_vendas_periodo(
            self.data_inicial.date().toPyDate(), self.data_final.date().toPyDate()))
        layout.addWidget(botao_grafico_periodo)

        botao_grafico_produto = QPushButton('Gráfico de Vendas por Produto')
        botao_grafico_produto.clicked.connect(lambda: grafico_vendas_produto(
            self.data_inicial.date().toPyDate(), self.data_final.date().toPyDate()))
        layout.addWidget(botao_grafico_produto)

        botao_estatisticas = QPushButton('Exibir Estatísticas Resumidas')
        botao_estatisticas.clicked.connect(lambda: exibir_estatisticas(
            self.data_inicial.date().toPyDate(), self.data_final.date().toPyDate()))
        layout.addWidget(botao_estatisticas)

        self.setLayout(layout)


# Executar a aplicação
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
