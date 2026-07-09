# 🎬 Movie Recommendation System

A content-based movie recommendation system that suggests similar movies based on your selection. Built with Python, Machine Learning, and a premium dark cinematic Streamlit UI.

![Python](https://img.shields.io/badge/Python-3.7+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.24+-red?style=flat-square&logo=streamlit)
![TMDB](https://img.shields.io/badge/TMDB-API-01b4e4?style=flat-square)
![License](https://img.shields.io/badge/License-Open%20Source-green?style=flat-square)

---

## ✨ Features

- 🤖 **Content-Based Filtering** — Recommends movies based on genres, keywords, cast & crew
- 🎨 **Premium Dark UI** — Cinematic dark theme with animated gradient orbs & glassmorphism
- 🍿 **Top 10 Recommendations** — Ranked movie cards with posters, ratings, genres & overviews
- 🎬 **Movie Spotlight** — Full details of your selected movie (poster, rating, year, overview)
- ✨ **Hover Animations** — Cards lift & reveal movie overview on hover
- 🛡️ **Error Handling** — Graceful fallbacks if TMDB API is unavailable
- ⚡ **Fast Reloads** — Data cached with `@st.cache_data` for instant responses

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core language |
| Pandas & NumPy | Data processing |
| Scikit-learn | Cosine similarity & vectorization |
| Streamlit | Web application framework |
| TMDB API | Real-time movie posters & metadata |
| Jupyter Notebook | Data analysis & model building |

## 📂 Project Structure

```
Movie-Recommendation-System/
├── movie-recommender-system.ipynb   # Data analysis & model building
├── movie_dict.pkl                   # Processed movie data
├── movies.pkl                       # Movie DataFrame
├── Movies-Recommender/              # Streamlit web app
│   ├── app.py                       # Main application (premium UI)
│   ├── requirements.txt             # Python dependencies
│   └── similarity.pkl               # Cosine similarity matrix (generated locally)
└── README.md
```

> **Note:** `similarity.pkl` is not tracked in git (too large). Generate it by running the Jupyter notebook.

## 📥 Dataset

This project uses the **TMDB 5000 Movie Dataset** from Kaggle. Download and place in the root directory before running the notebook:

👉 [tmdb-movie-metadata on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

Files needed:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/AdityaTawhare/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

### 2. Download the dataset
Get both CSV files from [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) and place them in the root directory.

### 3. Generate the similarity model
Run the Jupyter notebook to generate `similarity.pkl`:
```bash
jupyter notebook movie-recommender-system.ipynb
```
Then copy `similarity.pkl` into `Movies-Recommender/`.

### 4. Install dependencies
```bash
cd Movies-Recommender
pip install -r requirements.txt
```

### 5. Run the app
```bash
streamlit run app.py
```

Open your browser at **http://localhost:8501** 🎉

## 🧠 How It Works

```
Raw Data → Preprocessing → Feature Engineering → Vectorization → Cosine Similarity → Recommendations
```

1. **Preprocessing** — Merges movies & credits datasets, extracts genres, keywords, cast, crew
2. **Feature Engineering** — Combines metadata into a single "tags" field per movie
3. **Vectorization** — Converts tags to numerical vectors using `CountVectorizer` (5000 features)
4. **Cosine Similarity** — Calculates pairwise similarity scores across all ~4800 movies
5. **Recommendation** — Returns top 10 most similar movies for any selection

## 📸 App Preview

| Feature | Description |
|---------|-------------|
| 🌌 Animated background orbs | Floating red, purple & blue blurred orbs |
| 🎬 Movie Spotlight | Selected movie shown with full details |
| 🃏 Ranked cards | `#1`–`#10` badges + golden rating chips |
| 🎭 Genre tags | Pill-style genre labels per movie |
| 🔍 Smart hover | Overview text revealed on card hover |

## 📄 License

This project is open source and available for learning and educational purposes.

---

⭐ **If you found this helpful, give it a star on GitHub!**
