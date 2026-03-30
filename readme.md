# Personalized Learning App

An AI-driven learning system that profiles students using KMeans clustering and delivers personalized recommendations — quiz, tutorial, or challenge — via a real-time Streamlit interface.

![Python](https://img.shields.io/badge/Python-3.10+-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-UI-red) ![License](https://img.shields.io/badge/License-MIT-green)

---

## What it does

**Student profiling** — KMeans clustering segments students by quiz score, time-on-task, and hints used, assigning each to a learning archetype.

**Personalized recommendations** — A Decision Tree classifier maps each cluster to an optimal next step: quiz, tutorial, or challenge. Recommendations update in real time after every quiz submission.

**Simulated dataset** — 1,000 students with realistic behavioral patterns, ready to swap for EdNet in Phase 2.

---

## Roadmap

| Feature | Status |
|---|---|
| KMeans student clustering | ✅ Done |
| Decision Tree recommendations | ✅ Done |
| Streamlit interactive UI | ✅ Done |
| MLflow experiment tracking | 🔨 In progress |
| HuggingFace notes generator | 🔨 In progress |
| Progress dashboard (score trends, learning gaps) | 🔨 In progress |
| EdNet real-world dataset integration | 🔨 In progress |
| Login & session tracking (SQLite) | 🔨 In progress |

---

## Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| ML Models | Scikit-learn (KMeans, Decision Tree) |
| NLP / GenAI | HuggingFace Transformers (planned) |
| MLOps | MLflow (planned) |
| Storage | CSV → SQLite |
| Dataset | Simulated CSV → EdNet |

---

## Run locally
```bash
# Clone and install
git clone https://github.com/prabalai/personalized-learning-app.git
cd personalized-learning-app
pip install -r requirements.txt

# Launch
streamlit run app.py
```

---

## Project structure
```
personalized_learning_app/
├── app.py                    # Streamlit entry point
├── requirements.txt
├── data/
│   └── quiz_data.csv         # 1,000-student simulated dataset
├── models/
│   └── decision_tree_model.pkl
└── utils/
    ├── ml_utils.py
    ├── session_handler.py
    └── note_generator.py
```

---

## About

Built by **Prabal Singh** — BTech in Artificial Intelligence and Data Science, focused on applied GenAI and MLOps projects.

Licensed under MIT.
