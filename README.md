# OSINT Threat Classifier

Este projeto demonstra um pipeline simples de OSINT com classificação de ameaças usando Machine Learning.

## Funcionalidades

- Coleta de notícias em tempo real via RSS
- Classificação de textos em "ameaça" ou "inofensivo"
- Exibição com destaque visual

## Como rodar

1. Clone este repositório:
```sh
git clone https://github.com/LeoVichi/threats_classifier.git
cd threats_classifier
```

2.  e ative o ambiente virtual:
```sh
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:
```sh
pip install -r requirements.txt
```

4. Execute:
```bash
python classifier.py
```

### Autor
Desenvolvido por [Leonardo Vichi](https://github.com/LeoVichi) para o Workshop intitulado "Bootcamp em Machine Learning para Estudos em Defesa: Inteligência Artificial, Redes Neurais, Mineração de Dados e Inteligência em Fontes Abertas" ministrado em 04ABR2025 na Escola de Guerra Naval por ocasião da 4ª Jornada de Prospectiva em Defesa.
