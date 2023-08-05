
```markdown
# API de Detecção de Anomalias em Dados Industriais

Esta é uma API para detectar anomalias em dados industriais. Ela utiliza três algoritmos de detecção de anomalias: Isolation Forest, Local Outlier Factor (LOF) e One-Class SVM. Além disso, também faz uso do cálculo do Intervalo Interquartil (IQR) para identificação de anomalias.

## Uso da API

Para usar a API, siga os passos abaixo:

1. Clone o repositório em sua máquina local:

```
git clone https://github.com/dheiver/API-SCADA-BR.git
cd API-SCADA-BR
```

2. Crie e ative um ambiente virtual (recomendado):

```
virtualenv venv
# Para Windows:
venv\Scripts\activate
# Para macOS/Linux:
source venv/bin/activate
```

3. Instale as dependências do projeto a partir do arquivo `requirements.txt`:

```
pip install -r requirements.txt
```

4. Execute o servidor da aplicação:

```
python app.py
```

A API estará em execução, e você poderá enviar solicitações para a rota `/detect_anomalies` usando a estrutura JSON mencionada anteriormente. O resultado será uma lista contendo os valores anômalos detectados.

## Endpoints da API

### Detectar Anomalias [POST /detect_anomalies]

Detecta anomalias em um conjunto de dados.

#### Parâmetros

- `data`: Uma lista de números representando o conjunto de dados.
- `contamination` (opcional): Um número decimal entre 0 e 1 que representa a porcentagem esperada de anomalias. O valor padrão é 0.05.

#### Exemplo de Solicitação

```
curl -X POST -H "Content-Type: application/json" -d '{"data": [120, 130, 140, 150, 160], "contamination": 0.05}' http://localhost:5000/detect_anomalies
```

#### Exemplo de Resposta

```json
{
    "anomalies": [120, 160]
}
```

## Melhorias Futuras

A aplicação pode ser aprimorada de diversas maneiras, incluindo:

- Adicionar suporte para outros tipos de dados, como texto, imagens e vídeos.
- Incorporar métodos adicionais de detecção de anomalias, como análise de tendência, análise de desvio padrão e análise de cluster.
- Implementar visualizações gráficas para facilitar a interpretação dos resultados.
- Adicionar suporte para geração de relatórios.

## Contribuindo

Contribuições são bem-vindas! Se você quiser contribuir para esta API, por favor, abra um pull request explicando suas alterações e melhorias propostas.

## Licença

Este projeto está licenciado sob a Licença MIT. Sinta-se livre para utilizar e modificar conforme necessário.

## Autor

Nome do Autor - [GitHub](https://github.com/nome-do-autor)
```

Agora o `README.md` está formatado de forma correta, apresentando todas as seções de forma clara e legível. Lembre-se de substituir "Nome do Autor" e "https://github.com/nome-do-autor" pelas informações reais do criador ou mantenedor do projeto.
