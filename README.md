# 🎬 Movie Recommendation System

A content-based movie recommendation system that suggests similar movies based on your selection. Built with Python, Machine Learning, and Streamlit.

## ✨ Features

- **Content-Based Filtering** — Recommends movies based on metadata like genres, keywords, cast, and crew
- **Interactive Web App** — Clean Streamlit interface with a searchable movie dropdown
- **Movie Posters** — Fetches real-time poster images from the TMDB API
- **Top 5 Recommendations** — Displays the 5 most similar movies with their posters

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core language |
| Pandas & NumPy | Data processing |
| Scikit-learn | Cosine similarity & vectorization |
| Streamlit | Web application framework |
| TMDB API | Movie posters & metadata |
| Jupyter Notebook | Data analysis & model building |

## 📂 Project Structure

```
Movie-Recommendation-System/
├── movie-recommender-system.ipynb   # Data analysis & model building notebook
├── movie_dict.pkl                   # Processed movie data (pickle)
├── movies.pkl                       # Movie DataFrame (pickle)
├── Movies-Recommender/              # Streamlit web app
│   ├── app.py                       # Main application
│   ├── requirements.txt             # Python dependencies
│   ├── setup.sh                     # Streamlit config for deployment
│   └── Procfile                     # Heroku deployment config
└── README.md
```

## 📥 Dataset

This project uses the **TMDB 5000 Movie Dataset** from Kaggle. Download the following files and place them in the root directory:

1. [tmdb_5000_movies.csv](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
2. [tmdb_5000_credits.csv](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AdityaTawhare/Movie-Recommendation-System.git
   cd Movie-Recommendation-System
   ```

2. **Download the dataset** from [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) and place the CSV files in the root directory.

3. **Generate the similarity model** by running the Jupyter notebook:
   ```bash
   jupyter notebook movie-recommender-system.ipynb
   ```
   This will generate `similarity.pkl` needed by the web app.

4. **Install dependencies**
   ```bash
   cd Movies-Recommender
   pip install -r requirements.txt
   ```

5. **Run the app**
   ```bash
   streamlit run app.py
   ```

6. Open your browser at `http://localhost:8501`

## 📸 How It Works

1. Select a movie from the dropdown menu
2. Click **"Show Recommendation"**
3. View 5 similar movie recommendations with their posters

## 🧠 Algorithm

The recommendation engine uses **content-based filtering**:

1. **Data Preprocessing** — Merges movie and credits datasets, extracts genres, keywords, cast, and crew
2. **Feature Engineering** — Combines metadata into a single text feature ("tags")
3. **Vectorization** — Converts tags into numerical vectors using `CountVectorizer`
4. **Cosine Similarity** — Calculates similarity scores between all movie pairs
5. **Recommendation** — Returns the top 5 most similar movies for any given selection

## 📄 License

This project is open source and available for learning and educational purposes.

---

⭐ If you found this project helpful, give it a star on GitHub!
