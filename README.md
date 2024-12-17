# Análise de Vendas
Este projeto é uma aplicação de análise de dados que permite visualizar e explorar informações sobre vendas a partir de um arquivo CSV. A aplicação é construída utilizando Python e PyQt5 para a interface gráfica, além de bibliotecas como Pandas, Matplotlib e Seaborn para manipulação e visualização de dados.

## Funcionalidades
- Carregamento de Dados: A aplicação carrega dados de vendas a partir de um arquivo CSV (vendas.csv).
  
- **Gráficos de Vendas:**
  - Gráfico de Vendas por Período: Permite visualizar o total de vendas em um intervalo de datas selecionado.
  - Gráfico de Vendas por Produto: Mostra o total de vendas agrupadas por produto em um intervalo de datas.
- **Estatísticas Resumidas:** Exibe informações como total de vendas, média de vendas e o produto mais vendido em um intervalo de datas selecionado.

## Pré-requisitos
Antes de executar a aplicação, certifique-se de ter o Python instalado em sua máquina. Você também precisará instalar as seguintes bibliotecas:

```
pip install pandas matplotlib seaborn PyQt5
```

## Estrutura do Projeto


- `main.py:` Código-fonte da aplicação.
- `vendas.csv`: Arquivo CSV contendo os dados de vendas.

**Exemplo de vendas.csv**

```
data,produto,quantidade,valor_venda
2024-01-01,iPhone 14,15,15000.00
2024-01-01,Mouse Logitech G502,20,2000.00
```
...
## Como Executar

1. Certifique-se de que o arquivo vendas.csv está no mesmo diretório que o main.py.
2. Execute o script main.py:
````
python main.py
````
3. A interface gráfica será exibida. Selecione o intervalo de datas desejado e clique nos botões para gerar os gráficos ou exibir as estatísticas.
   
## Contribuição
Sinta-se à vontade para contribuir com melhorias ou correções. Para isso, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma nova branch (git checkout -b feature/nome-da-sua-feature).
3. Faça suas alterações e commit (git commit -m 'Adicionando nova funcionalidade').
4. Envie para o repositório remoto (git push origin feature/nome-da-sua-feature).
5. Abra um Pull Request.
   
## Licença
Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.

## Contato
Para mais informações entre em contato [yansantos2410@gmail.com]
Desenvolvedor: Yan de Oliveira

## Informações adicionais
Código fonte do aplicativo se encontra em outra branch do repositório.
