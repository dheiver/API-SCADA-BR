# Anomaly Detection API

Esta é uma API baseada em Flask que fornece detecção de anomalias usando vários métodos como Isolation Forest, Local Outlier Factor (LOF) e One-Class SVM. A API recebe dados de entrada e um valor de contaminação como parâmetros e retorna as anomalias detectadas.

## Primeiros Passos

### Pré-requisitos

- Python 3.x
- Flask
- Numpy
- Pandas
- Matplotlib
- scikit-learn

Você pode instalar as dependências necessárias usando pip:

```
pip install flask numpy pandas matplotlib scikit-learn
```

### Executando a API

1. Clone este repositório em sua máquina local.
2. Instale as dependências necessárias conforme mencionado na seção "Pré-requisitos".
3. Inicie o servidor Flask:

```
python app.py
```

A API estará disponível em `http://127.0.0.1:5000/`.

## Uso

Para detectar anomalias, envie uma solicitação POST para o endpoint `/detect_anomalies` com o seguinte conteúdo JSON:

```
{
  "data": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
  "contamination": 0.1
}
```

- `data`: Uma lista de valores numéricos para detecção de anomalias.
- `contamination`: A proporção de anomalias esperada nos dados.

A API retornará uma resposta JSON com as anomalias detectadas:

```
{
  "anomalias": [80, 90, 100]
}
```

## Métodos Utilizados para Detecção de Anomalias

1. Método IQR (Interquartile Range): Identifica anomalias usando o método IQR.
2. Isolation Forest: Um método de conjunto para detecção de anomalias.
3. Local Outlier Factor (LOF): Um método baseado em densidade local para detecção de anomalias.
4. One-Class SVM: Um método baseado em máquina de vetores de suporte para detecção de anomalias.

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou quiser adicionar novos recursos, sinta-se à vontade para criar um pull request ou abrir uma issue.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.
