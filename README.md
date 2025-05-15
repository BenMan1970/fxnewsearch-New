# Forex RSI Screener Multi-Timeframe

## Description

Ce projet permet de détecter en temps réel les paires Forex avec des niveaux extrêmes de RSI (suracheté >70 ou survendu <30) sur les timeframes H1, H4 et Daily via TradingView.

Les signaux sont affichés en temps réel via une application **Streamlit**.

---

## Technologies utilisées

- TradingView (PineScript)
- Python
- Streamlit
- JSON

---

## Comment utiliser ?

1. Copie le PineScript dans TradingView.
2. Configure les alertes Webhook vers ton API locale ou simule les données dans `data/signals.json`.
3. Lance l'application Streamlit localement ou dépose-la sur [Streamlit Community Cloud](https://streamlit.io/cloud ).

---

## Déploiement

Pour déployer sur Streamlit :
- Connecte ton compte Streamlit à GitHub
- Importe ce repo
- Clique sur "Deploy"
