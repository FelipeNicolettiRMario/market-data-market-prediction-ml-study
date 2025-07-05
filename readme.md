# 📈 Market Direction Prediction Using Machine Learning

Este projeto é um estudo prático de Machine Learning aplicado ao mercado financeiro, com foco em prever a direção do preço de um ativo utilizando **Regressão Logística**, **SVM**, etc...

---

## ✅ Objetivo

Criar um modelo simples, porém robusto, para prever se o preço de um ativo (neste caso, o Dólar Americano — USD/BRL) irá **subir ou cair** na próxima semana.

---

## ✅ Técnicas Utilizadas

- **Regressão Logística** (classificação binária)
- **Pipeline com StandardScaler** (normalização + modelo)
- **Séries Temporais com Split Temporal (sem embaralhamento)**
- **Threshold Tuning (Ajuste do Limiar de Probabilidade)**
- **Métricas de Classificação**: Precision, Recall, F1-score
- **Simulação de Retorno Acumulado (Backtest Simplificado)**

---

## ✅ Principais Features
- **ma_ratio** → Relação entre médias móveis de curto e médio prazo.
- **volatility** → Volatilidade histórica.
- **Close** → Preço de fechamento semanal.
- **ma_12** → Média móvel de 12 semanas.

---

## ✅ Principais Lições
- O modelo consegue prever a direção com desempenho razoável, mesmo com um modelo simples.
- Ajustar o **threshold** pode transformar drasticamente a performance da estratégia, aumentando o retorno acumulado ao priorizar trades mais confiáveis.
- Modelos treinados em períodos específicos (ex.: pandemia) podem ter dificuldades em outros regimes econômicos, levantando a importância da adaptabilidade.

---

## ✅ Como Rodar o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/market-direction-prediction.git
cd market-direction-prediction
```

2. Instale as dependências:
```bash
pip install -r requirements.txt 
```
3. Execute o notebook:
```bash
jupyter notebook main.ipynb
```

ATENÇÃO: Esse projeto não deve ser utilizado para fins de investimento real. É apenas um estudo acadêmico e não garante resultados financeiros. Sempre faça sua própria pesquisa e consulte profissionais qualificados antes de investir.
