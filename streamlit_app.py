import streamlit as st
import pandas as pd
import json
import time

# Titre de l'app
st.set_page_config(page_title="Forex RSI Screener", layout="wide")
st.title("📈 Forex RSI Screener - Multi Timeframe")

# Charger les signaux depuis le fichier JSON
def load_signals():
    try:
        with open("data/signals.json", "r") as f:
            return json.load(f)
    except Exception as e:
        st.error("Fichier de signaux introuvable ou corrompu.")
        return {}

# Rafraîchissement auto toutes les X secondes
while True:
    signals = load_signals()

    if signals:
        st.success("✅ Signaux trouvés !")
        df = pd.DataFrame.from_dict(signals, orient='index')
        st.dataframe(df.style.applymap(lambda x: 'background-color: red' if x == "Overbought" else ('background-color: green' if x == "Oversold" else '')))
    else:
        st.info("🔍 Aucun signal trouvé pour le moment.")

    time.sleep(60)  # Actualise toutes les minutes
