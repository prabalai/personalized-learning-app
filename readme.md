# 🧠 Personalized Learning App

An AI-powered Streamlit-based learning system that classifies students by learning type and recommends their next best activity (quiz, video, or tutorial).

---

## ✅ Phase 1 Features (Completed)

- 🎯 **Student Profiling**: KMeans clustering based on quiz performance (score, time, hints used)
- 📊 **Personalized Recommendations**: Decision Tree model recommends next step — quiz, tutorial, or challenge
- 📁 **Simulated Dataset**: Includes 1000 students with realistic learning behavior
- 💻 **Interactive UI**: Real-time personalized suggestions after taking quizzes

---

## 🚧 Phase 2 Features (In Progress)

- 📂 **Real-World Dataset Integration** (EdNet)
- 📦 **MLOps with MLflow**: Logging, tracking, and managing model versions
- 🔐 **Login & Session Tracking**: Using CSV/SQLite
- 🧠 **AI Notes Generator**: Hugging Face transformers to generate short notes
- 📈 **Progress Dashboard**: Visualizations for score trends, time analysis, and learning gaps

---

## 🧰 Tech Stack

- **Frontend/UI**: Streamlit
- **ML Models**: Scikit-learn (KMeans, DecisionTree)
- **AI Text Generation**: Hugging Face Transformers (planned)
- **Data**: Simulated CSV (EdNet planned)
- **Storage**: CSV (now), SQLite (planned)
- **MLOps**: MLflow (coming soon)

---

## 🚀 How to Run the App

```bash
# Clone the repository
git clone https://github.com/prabalai/personalized-learning-app.git
cd personalized-learning-app

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py

📁 Project Structure
personalized_learning_app/
├── app.py                # Main Streamlit app
├── requirements.txt      # Dependencies
├── README.md             # Project overview
├── data/
│   └── quiz_data.csv     # Sample quiz questions
├── models/
│   └── decision_tree_model.pkl
├── utils/
│   ├── ml_utils.py
│   ├── session_handler.py
│   └── note_generator.py

👤 Author
Prabal Singh
BTech in Artificial Intelligence and Data Science
Aspiring Data Scientist | Building GenAI + MLOps Projects

📄 License
This project is licensed under the MIT License — free to use, just give credit! 🙌
