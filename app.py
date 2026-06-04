
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import time

st.set_page_config(
    page_title="AI Security Platform",
    page_icon="🛡️",
    layout="wide"
)

# =========================
# PREMIUM CYBER DESIGN
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(0, 212, 255, 0.18), transparent 28%),
        radial-gradient(circle at bottom right, rgba(0, 255, 157, 0.12), transparent 30%),
        linear-gradient(135deg, #050816 0%, #0A0F1C 45%, #111827 100%) !important;
    color: #FFFFFF !important;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #050816 0%, #0B1020 100%) !important;
    border-right: 1px solid rgba(0, 212, 255, 0.25);
}

[data-testid="stSidebar"] * {
    color: #E5E7EB !important;
}

h1 {
    color: #FFFFFF !important;
    font-weight: 900 !important;
    letter-spacing: -1px;
}

h2, h3 {
    color: #FFFFFF !important;
    font-weight: 800 !important;
}

p, label, span, div {
    color: #E5E7EB !important;
}

hr {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,212,255,.45), transparent);
}

[data-testid="stMetric"] {
    background: linear-gradient(135deg, rgba(17, 24, 39, 0.95), rgba(30, 41, 59, 0.85));
    border: 1px solid rgba(0, 212, 255, 0.35);
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0 0 30px rgba(0, 212, 255, 0.12);
}

[data-testid="stMetricValue"] {
    color: #00FF9D !important;
    font-size: 34px !important;
    font-weight: 900 !important;
}

[data-testid="stMetricLabel"] {
    color: #94A3B8 !important;
    text-transform: uppercase;
    font-size: 12px !important;
    letter-spacing: 1px;
}

.stButton > button {
    background: linear-gradient(90deg, #00D4FF, #00FF9D) !important;
    color: #020617 !important;
    border: none !important;
    border-radius: 14px !important;
    font-weight: 900 !important;
    padding: 0.75rem 1.3rem !important;
    box-shadow: 0 0 20px rgba(0, 255, 157, 0.25);
}

.stButton > button:hover {
    box-shadow: 0 0 30px rgba(0, 255, 157, 0.55);
    transform: translateY(-1px);
}

.info-box {
    padding: 22px;
    border-radius: 20px;
    background: linear-gradient(135deg, rgba(17,24,39,.95), rgba(30,41,59,.85));
    border: 1px solid rgba(0, 212, 255, 0.35);
    box-shadow: 0 0 25px rgba(0, 212, 255, 0.12);
}

.alert-box {
    padding: 22px;
    border-radius: 20px;
    background: linear-gradient(135deg, rgba(69, 10, 10, .95), rgba(127, 29, 29, .75));
    border: 1px solid #FF4D4D;
    box-shadow: 0 0 28px rgba(255, 77, 77, 0.25);
}

.normal-box {
    padding: 22px;
    border-radius: 20px;
    background: linear-gradient(135deg, rgba(5, 46, 26, .95), rgba(6, 78, 59, .75));
    border: 1px solid #00FF9D;
    box-shadow: 0 0 28px rgba(0, 255, 157, 0.25);
}

.metric-card {
    padding: 24px;
    border-radius: 22px;
    background: linear-gradient(135deg, rgba(17,24,39,.95), rgba(15,23,42,.9));
    border: 1px solid rgba(0, 212, 255, 0.32);
    box-shadow: 0 0 25px rgba(0, 212, 255, 0.12);
    margin-bottom: 15px;
}

.status-online {
    color: #00FF9D !important;
    font-weight: 900;
}

.status-warning {
    color: #FBBF24 !important;
    font-weight: 900;
}

.status-offline {
    color: #FF4D4D !important;
    font-weight: 900;
}

.badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 999px;
    background: rgba(0, 212, 255, .12);
    border: 1px solid rgba(0, 212, 255, .35);
    color: #00D4FF !important;
    font-weight: 800;
    font-size: 12px;
    letter-spacing: .7px;
    text-transform: uppercase;
}

[data-testid="stDataFrame"] {
    border-radius: 18px;
    overflow: hidden;
    border: 1px solid rgba(0,212,255,.25);
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
st.sidebar.markdown("## 🛡️ AI Security Platform")
st.sidebar.markdown("**Smart Surveillance Command Center**")
st.sidebar.markdown(
    "<span class='badge'>YOLO + CNN + LSTM</span>",
    unsafe_allow_html=True
)
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "🛡️ Security Center",
        "🎥 AI Monitoring",
        "⚠️ Threat Detection",
        "📡 Camera Network",
        "📈 Intelligence Reports",
        "🤖 AI Engine"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Plateforme intelligente de détection des comportements suspects.")


# =========================
# HEADER
# =========================
def header(title, subtitle):
    st.markdown(f"<span class='badge'>AI POWERED SURVEILLANCE</span>", unsafe_allow_html=True)
    st.title(title)
    st.markdown(f"<p style='font-size:18px;color:#94A3B8 !important'>{subtitle}</p>", unsafe_allow_html=True)
    st.markdown("---")


# =========================
# DASHBOARD
# =========================
if page == "🛡️ Security Center":
    header("🛡️ Smart Surveillance Command Center", "Vue globale de la plateforme intelligente de sécurité vidéo.")

    total_sequences = len(df)
    suspects = int((df["comportement"] == "Suspect").sum())
    normals = int((df["comportement"] == "Normal").sum())
    risk_avg = round(df["score_risque"].mean() * 100, 1)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("ACTIVE STREAMS", total_sequences)
    col2.metric("THREATS DETECTED", suspects)
    col3.metric("SAFE EVENTS", normals)
    col4.metric("RISK INDEX", f"{risk_avg}%")

    st.subheader("📌 System Overview")
    st.markdown("""
    <div class="info-box">
    Cette plateforme permet à un agent de sécurité de superviser les caméras, lancer une analyse vidéo,
    consulter les alertes détectées et visualiser les statistiques du système intelligent.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🧠 AI Processing Pipeline")
    c1, c2, c3 = st.columns(3)
    c1.markdown("""
    <div class="metric-card">
    <h3>01 — YOLO Detection</h3>
    <p>Détection rapide des personnes et objets dans chaque frame vidéo.</p>
    </div>
    """, unsafe_allow_html=True)
    c2.markdown("""
    <div class="metric-card">
    <h3>02 — CNN Features</h3>
    <p>Extraction automatique des caractéristiques visuelles importantes.</p>
    </div>
    """, unsafe_allow_html=True)
    c3.markdown("""
    <div class="metric-card">
    <h3>03 — LSTM Timeline</h3>
    <p>Analyse temporelle du comportement sur plusieurs images successives.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Dernières séquences analysées")
    st.dataframe(df.tail(10), use_container_width=True)


# =========================
# ANALYSE VIDEO
# =========================
elif page == "🎥 AI Monitoring":
    header("🎥 AI Monitoring Center", "Analyse vidéo simulée avec pipeline YOLO + CNN + LSTM.")

    uploaded_video = st.file_uploader("Importer une vidéo de surveillance", type=["mp4", "avi", "mov", "mkv"])

    colA, colB = st.columns([1, 1])

    with colA:
        selected_seq = st.selectbox("Choisir une séquence du dataset", df["sequence_id"].tolist())
        seq = df[df["sequence_id"] == selected_seq].iloc[0]

        st.markdown("### Sequence Intelligence")
        st.markdown(f"""
        <div class="info-box">
        Frames : <b>{seq['nb_frames']}</b><br>
        Personnes détectées : <b>{seq['nb_personnes_detectees']}</b><br>
        Vitesse moyenne : <b>{seq['vitesse_moyenne']}</b><br>
        Zone sensible : <b>{'Oui' if seq['zone_sensible'] == 1 else 'Non'}</b>
        </div>
        """, unsafe_allow_html=True)

    with colB:
        if uploaded_video is not None:
            st.video(uploaded_video)
        else:
            st.markdown("""
            <div class="info-box">
            Aucune vidéo importée. La démonstration utilise une séquence simulée du dataset.
            </div>
            """, unsafe_allow_html=True)

    if st.button("🚀 Launch AI Analysis"):
        progress = st.progress(0)
        status = st.empty()

        steps = [
            "Loading video stream...",
            "Running YOLO object detection...",
            "Extracting visual features with CNN...",
            "Analyzing behavior timeline with LSTM...",
            "Generating final decision..."
        ]

        for i, step in enumerate(steps):
            status.write(step)
            progress.progress((i + 1) * 20)
            time.sleep(0.4)

        score = float(seq["score_risque"])
        result = "Suspect" if score >= 0.5 else "Normal"

        st.subheader("AI Decision Result")

        if result == "Suspect":
            st.markdown(f"""
            <div class="alert-box">
            <h3>⚠️ THREAT DETECTED</h3>
            Comportement suspect détecté<br>
            Risk Score : {round(score*100, 2)}%
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="normal-box">
            <h3>✅ SAFE BEHAVIOR</h3>
            Comportement normal<br>
            Risk Score : {round(score*100, 2)}%
            </div>
            """, unsafe_allow_html=True)

        st.success("Analyse terminée avec succès.")


# =========================
# ALERTES
# =========================
elif page == "⚠️ Threat Detection":
    header("⚠️ Threat Detection Center", "Historique des comportements suspects détectés par le système.")

    alerts = df[df["comportement"] == "Suspect"].copy()
    alerts["date"] = pd.date_range(end=datetime.now(), periods=len(alerts), freq="h")
    alerts["camera"] = np.random.choice(["Entrance Gate", "Parking Area", "Main Corridor", "Server Room"], len(alerts))
    alerts["niveau"] = pd.cut(
        alerts["score_risque"],
        bins=[0, 0.6, 0.8, 1],
        labels=["MEDIUM", "HIGH", "CRITICAL"]
    )
    alerts["statut"] = np.random.choice(["OPEN", "INVESTIGATING", "RESOLVED"], len(alerts))

    st.dataframe(
        alerts[["date", "sequence_id", "camera", "score_risque", "niveau", "statut"]],
        use_container_width=True
    )

    st.subheader("Threat Details")
    chosen = st.selectbox("Choisir une alerte", alerts["sequence_id"].tolist())
    row = alerts[alerts["sequence_id"] == chosen].iloc[0]

    st.markdown(f"""
    <div class="alert-box">
    <h3>⚠️ Alert ID : {chosen}</h3>
    Camera Node : {row['camera']}<br>
    Threat Level : {row['niveau']}<br>
    Risk Score : {round(row['score_risque']*100, 2)}%<br>
    Status : {row['statut']}
    </div>
    """, unsafe_allow_html=True)


# =========================
# CAMERAS
# =========================
elif page == "📡 Camera Network":
    header("📡 Camera Network", "Supervision des caméras connectées au système.")

    cameras = [
        {"nom": "Node-01", "zone": "Entrance Gate", "statut": "ONLINE", "analyse": "Real-Time AI"},
        {"nom": "Node-02", "zone": "Parking Area", "statut": "ONLINE", "analyse": "Real-Time AI"},
        {"nom": "Node-03", "zone": "Main Corridor", "statut": "ANALYZING", "analyse": "YOLO Active"},
        {"nom": "Node-04", "zone": "Server Room", "statut": "OFFLINE", "analyse": "Unavailable"},
    ]

    cols = st.columns(2)
    for i, cam in enumerate(cameras):
        status_class = "status-online"
        if cam["statut"] == "ANALYZING":
            status_class = "status-warning"
        elif cam["statut"] == "OFFLINE":
            status_class = "status-offline"

        with cols[i % 2]:
            st.markdown(f"""
            <div class="metric-card">
            <h3>📡 {cam['nom']}</h3>
            <p>Zone : {cam['zone']}</p>
            <p>Status : <span class="{status_class}">{cam['statut']}</span></p>
            <p>AI Mode : {cam['analyse']}</p>
            </div>
            """, unsafe_allow_html=True)


# =========================
# RAPPORTS
# =========================
elif page == "📈 Intelligence Reports":
    header("📈 AI Intelligence Reports", "Statistiques et visualisation des résultats produits par l'IA.")

    st.subheader("Behavior Analytics")
    counts = df["comportement"].value_counts().reset_index()
    counts.columns = ["Comportement", "Nombre"]
    st.bar_chart(counts.set_index("Comportement"))

    st.subheader("Risk Evolution")
    chart_df = df[["sequence_id", "score_risque"]].set_index("sequence_id")
    st.line_chart(chart_df)

    st.subheader("General Statistics")
    st.write(df.describe())


# =========================
# PARAMETRES IA
# =========================
elif page == "🤖 AI Engine":
    header("🤖 AI Engine Configuration", "Configuration du modèle et des seuils de détection.")

    st.subheader("Model Configuration")
    model_name = st.selectbox("Modèle utilisé", ["YOLO + CNN + LSTM", "YOLO seulement", "CNN + LSTM"])
    threshold = st.slider("Seuil de détection suspecte", 0.0, 1.0, 0.5, 0.05)
    conf_yolo = st.slider("Confiance YOLO", 0.0, 1.0, 0.25, 0.05)
    mode = st.radio("Mode d'analyse", ["Vidéo importée", "Temps réel", "Dataset simulé"])

    if st.button("💾 Save AI Parameters"):
        st.success("Paramètres sauvegardés avec succès.")

    st.markdown(f"""
    <div class="info-box">
    Modèle sélectionné : {model_name}<br>
    Seuil suspect : {threshold}<br>
    Confiance YOLO : {conf_yolo}<br>
    Mode : {mode}
    </div>
    """, unsafe_allow_html=True)
