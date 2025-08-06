📚 Personalized Learning System
An AI-powered Streamlit-based learning app that classifies students by learning type and recommends the next best learning activity (quiz, video, tutorial).

✅ Current Features (Phase 1 - Complete)
🧠 Student Profiling using KMeans
Cluster students based on quiz performance (score, time, hints used).

🔍 Personalized Recommendations
A Decision Tree model predicts what the student should do next — quiz, tutorial, or challenge.

📊 Simulated Dataset (1000 students)
Created with realistic student behavior to test the pipeline.

🧪 Interactive Streamlit UI
Students take a quiz and receive real-time personalized suggestions.

🚧 In Progress (Phase 2 - Ongoing)
📂 Dataset Integration (EdNet)
Adding real-world student learning data to improve personalization.

⚙️ MLOps with MLflow
Logging experiments, tracking metrics, and managing model versions.

🔐 Login & Session Storage
Student session data saved using CSV/SQLite for persistent progress tracking.

📝 AI Notes Generator
Automatically generate short notes using Hugging Face Transformers.

📈 Progress Dashboard
Charts for score trends, time analysis, and learning gaps.

🧰 Tech Stack
Layer	Tools Used
UI & Frontend	Streamlit
ML Models	scikit-learn (KMeans, DecisionTree)
AI Text Gen	HuggingFace Transformers (optional)
Dataset	Simulated CSV, EdNet (coming soon)
Logging & MLOps	MLflow (coming soon)
Storage	CSV (now), SQLite (planned)

🚀 Run the App
Clone the repo

bash
Copy
Edit
git clone https://github.com/yourusername/personalized-learning-app.git
cd personalized-learning-app
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app

bash
Copy
Edit
streamlit run app.py
📁 Project Structure
bash
Copy
Edit
personalized_learning_app/
├── app.py                  # Streamlit app
├── requirements.txt        # All dependencies
├── README.md               # Project overview
│
├── data/
│   └── quiz_data.csv       # Sample quiz questions
│
├── models/
│   └── decision_tree_model.pkl
│
└── utils/
    ├── ml_utils.py
    ├── session_handler.py
    └── note_generator.py
🙌 Author
Prabal Singh
BTech in Artificial Intelligence and Data Science
Aspiring Data Scientist | Building GenAI + MLOps Projects

📜 License
MIT License – free to use, just give credit 🙌