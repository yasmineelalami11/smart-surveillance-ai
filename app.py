
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import time

st.set_page_config(
    page_title="Smart Surveillance AI",
    page_icon="🎥",
    layout="wide"
)
st.markdown("""
<style>
.stApp {
    background-color: #0B1020 !important;
    color: #FFFFFF !important;
}

[data-testid="stSidebar"] {
    background-color: #111827 !important;
}

h1, h2, h3, p, label, span, div {
    color: #FFFFFF !important;
}

[data-testid="stMetricValue"],
[data-testid="stMetricLabel"] {
    color: #FFFFFF !important;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>
    .main {
        background-color: #0b1020;
    }
    .block-container {
        padding-top: 1.5rem;
    }
    h1, h2, h3 {
        color: #ffffff;
    }
    p, label, span, div {
        color: #e8edf7;
    }
    .metric-card {
        background: linear-gradient(135deg, #121a33, #1f2a4a);
        padding: 22px;
        border-radius: 18px;
        border: 1px solid rgba(0, 255, 180, 0.25);
        box-shadow: 0 0 18px rgba(0,255,180,0.08);
    }
    .alert-box {
        padding: 18px;
        border-radius: 15px;
        background-color: #2b1111;
        border-left: 6px solid #ff4b4b;
        color: white;
        font-weight: 600;
    }
    .normal-box {
        padding: 18px;
        border-radius: 15px;
        background-color: #102b1c;
        border-left: 6px solid #1ed760;
        color: white;
        font-weight: 600;
    }
    .info-box {
        padding: 18px;
        border-radius: 15px;
        background-color: #121a33;
        border-left: 6px solid #00d4ff;
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: #080c18;
    }
</style>
""", unsafe_allow_html=True)


# =========================
# DATA
# =========================
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("dataset_surveillance_sequences.csv")
    except:
        np.random.seed(42)
        n = 80
        df = pd.DataFrame({
            "sequence_id": [f"SEQ_{i:04d}" for i in range(1, n+1)],
            "nb_frames": np.random.choice([16, 24, 32], n),
            "hauteur_image": 32,
            "largeur_image": 32,
            "nb_personnes_detectees": np.random.randint(1, 8, n),
            "vitesse_moyenne": np.round(np.random.uniform(0.1, 3.5, n), 2),
            "zone_sensible": np.random.choice([0, 1], n),
            "variation_mouvement": np.round(np.random.uniform(0.05, 1.0, n), 2),
            "score_risque": np.round(np.random.uniform(0.05, 0.98, n), 2)
        })
        df["classe"] = (df["score_risque"] >= 0.5).astype(int)
        df["comportement"] = df["classe"].map({0: "Normal", 1: "Suspect"})
    return df

df = load_data()

# =========================
# SIDEBAR
# =========================
st.sidebar.title("🎥 Smart Surveillance AI")
st.sidebar.markdown("Plateforme intelligente de détection des comportements suspects.")
page = st.sidebar.radio(
    "Navigation",
    ["🏠 Dashboard", "🎬 Analyse vidéo", "🚨 Alertes", "📷 Caméras", "📊 Rapports", "⚙️ Paramètres IA"]
)

st.sidebar.markdown("---")
st.sidebar.info("Projet basé sur : YOLO + CNN + LSTM")


# =========================
# HEADER
# =========================
def header(title, subtitle):
    st.title(title)
    st.markdown(f"<p style='font-size:18px;color:#b7c5e5'>{subtitle}</p>", unsafe_allow_html=True)
    st.markdown("---")


# =========================
# DASHBOARD
# =========================
if page == "🏠 Dashboard":
    header("🏠 Dashboard général", "Vue globale de la plateforme de surveillance intelligente.")

    total_sequences = len(df)
    suspects = int((df["comportement"] == "Suspect").sum())
    normals = int((df["comportement"] == "Normal").sum())
    risk_avg = round(df["score_risque"].mean() * 100, 1)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Séquences analysées", total_sequences)
    col2.metric("Comportements suspects", suspects)
    col3.metric("Comportements normaux", normals)
    col4.metric("Risque moyen", f"{risk_avg}%")

    st.subheader("📌 Résumé du système")
    st.markdown("""
    <div class="info-box">
    Cette plateforme permet à un agent de sécurité de suivre les caméras, lancer une analyse vidéo,
    consulter les alertes détectées et visualiser les statistiques du système intelligent.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🧠 Pipeline IA utilisé")
    c1, c2, c3 = st.columns(3)
    c1.markdown("### 1️⃣ YOLO\nDétection des personnes et objets dans les images.")
    c2.markdown("### 2️⃣ CNN\nExtraction des caractéristiques visuelles importantes.")
    c3.markdown("### 3️⃣ LSTM\nAnalyse temporelle des comportements sur plusieurs images.")

    st.subheader("Dernières séquences analysées")
    st.dataframe(df.tail(10), use_container_width=True)


# =========================
# ANALYSE VIDEO
# =========================
elif page == "🎬 Analyse vidéo":
    header("🎬 Analyse vidéo", "Importer une vidéo ou choisir une séquence pour simuler la détection IA.")

    uploaded_video = st.file_uploader("Importer une vidéo de surveillance", type=["mp4", "avi", "mov", "mkv"])

    colA, colB = st.columns([1, 1])

    with colA:
        selected_seq = st.selectbox("Ou choisir une séquence du dataset", df["sequence_id"].tolist())
        seq = df[df["sequence_id"] == selected_seq].iloc[0]

        st.write("### Informations de la séquence")
        st.write(f"Nombre de frames : **{seq['nb_frames']}**")
        st.write(f"Personnes détectées : **{seq['nb_personnes_detectees']}**")
        st.write(f"Vitesse moyenne : **{seq['vitesse_moyenne']}**")
        st.write(f"Zone sensible : **{'Oui' if seq['zone_sensible'] == 1 else 'Non'}**")

    with colB:
        if uploaded_video is not None:
            st.video(uploaded_video)
        else:
            st.markdown("""
            <div class="info-box">
            Aucune vidéo importée. La démonstration utilisera une séquence simulée du dataset.
            </div>
            """, unsafe_allow_html=True)

    if st.button("🚀 Lancer l'analyse IA"):
        progress = st.progress(0)
        status = st.empty()

        steps = [
            "Chargement de la vidéo...",
            "Détection des personnes avec YOLO...",
            "Extraction des caractéristiques avec CNN...",
            "Analyse temporelle avec LSTM...",
            "Génération du résultat final..."
        ]

        for i, step in enumerate(steps):
            status.write(step)
            progress.progress((i + 1) * 20)
            time.sleep(0.4)

        score = float(seq["score_risque"])
        result = "Suspect" if score >= 0.5 else "Normal"

        st.subheader("Résultat de l'analyse")

        if result == "Suspect":
            st.markdown(f"""
            <div class="alert-box">
            🚨 Comportement suspect détecté<br>
            Score de risque : {round(score*100, 2)}%
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="normal-box">
            ✅ Comportement normal<br>
            Score de risque : {round(score*100, 2)}%
            </div>
            """, unsafe_allow_html=True)

        st.success("Analyse terminée avec succès.")


#
elif page == "🚨 Alertes":
    header("🚨 Gestion des alertes", "Historique des comportements suspects détectés par le système.")

    alerts = df[df["comportement"] == "Suspect"].copy()
    alerts["date"] = pd.date_range(end=datetime.now(), periods=len(alerts), freq="h")
    alerts["camera"] = np.random.choice(["Entrée principale", "Parking", "Couloir", "Salle serveur"], len(alerts))
    alerts["niveau"] = pd.cut(
        alerts["score_risque"],
        bins=[0, 0.6, 0.8, 1],
        labels=["Moyen", "Élevé", "Critique"]
    )
    alerts["statut"] = np.random.choice(["Non traité", "En cours", "Traité"], len(alerts))

    st.dataframe(
        alerts[["date", "sequence_id", "camera", "score_risque", "niveau", "statut"]],
        use_container_width=True
    )

    st.subheader("Détail d'une alerte")
    chosen = st.selectbox("Choisir une alerte", alerts["sequence_id"].tolist())
    row = alerts[alerts["sequence_id"] == chosen].iloc[0]

    st.markdown(f"""
    <div class="alert-box">
    Alerte : {chosen}<br>
    Caméra : {row['camera']}<br>
    Niveau : {row['niveau']}<br>
    Score de risque : {round(row['score_risque']*100, 2)}%
    </div>
    """, unsafe_allow_html=True)


# =========================
# CAMERAS
# =========================
elif page == "📷 Caméras":
    header("📷 Caméras connectées", "Suivi de l'état des caméras de surveillance.")

    cameras = [
        {"nom": "Caméra 01", "zone": "Entrée principale", "statut": "Active", "analyse": "Temps réel"},
        {"nom": "Caméra 02", "zone": "Parking", "statut": "Active", "analyse": "Temps réel"},
        {"nom": "Caméra 03", "zone": "Couloir", "statut": "Analyse en cours", "analyse": "YOLO actif"},
        {"nom": "Caméra 04", "zone": "Salle serveur", "statut": "Hors ligne", "analyse": "Non disponible"},
    ]

    cols = st.columns(2)
    for i, cam in enumerate(cameras):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="metric-card">
            <h3>{cam['nom']}</h3>
            <p>Zone : {cam['zone']}</p>
            <p>Statut : {cam['statut']}</p>
            <p>Mode analyse : {cam['analyse']}</p>
            </div>
            """, unsafe_allow_html=True)
            st.write("")


# =========================
# RAPPORTS
# =========================
elif page == "📊 Rapports":
    header("📊 Rapports et statistiques", "Visualisation des résultats obtenus par le système IA.")

    st.subheader("Répartition des comportements")
    counts = df["comportement"].value_counts().reset_index()
    counts.columns = ["Comportement", "Nombre"]
    st.bar_chart(counts.set_index("Comportement"))

    st.subheader("Évolution du score de risque")
    chart_df = df[["sequence_id", "score_risque"]].set_index("sequence_id")
    st.line_chart(chart_df)

    st.subheader("Statistiques générales")
    st.write(df.describe())


# =========================
# PARAMETRES IA
# =========================
elif page == "⚙️ Paramètres IA":
    header("⚙️ Paramètres IA", "Configuration du modèle et des seuils de détection.")

    st.subheader("Configuration du modèle")
    model_name = st.selectbox("Modèle utilisé", ["YOLO + CNN + LSTM", "YOLO seulement", "CNN + LSTM"])
    threshold = st.slider("Seuil de détection suspecte", 0.0, 1.0, 0.5, 0.05)
    conf_yolo = st.slider("Confiance YOLO", 0.0, 1.0, 0.25, 0.05)
    mode = st.radio("Mode d'analyse", ["Vidéo importée", "Temps réel", "Dataset simulé"])

    if st.button("💾 Sauvegarder les paramètres"):
        st.success("Paramètres sauvegardés avec succès.")

    st.markdown(f"""
    <div class="info-box">
    Modèle sélectionné : {model_name}<br>
    Seuil suspect : {threshold}<br>
    Confiance YOLO : {conf_yolo}<br>
    Mode : {mode}
    </div>
    """, unsafe_allow_html=True)
