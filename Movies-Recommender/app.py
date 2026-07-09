import pickle
import streamlit as st
import requests

# ─── Page Config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Premium CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&family=Outfit:wght@300;400;500;600;700;800;900&display=swap');

    /* ── Reset & Global ── */
    .stApp {
        background: #0b0c10;
        font-family: 'Poppins', sans-serif;
    }
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {
        padding: 1.5rem 2rem 2rem;
        max-width: 1300px;
    }

    /* ── Animated Gradient Background Orbs ── */
    .bg-effects {
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        pointer-events: none;
        z-index: 0;
        overflow: hidden;
    }
    .orb {
        position: absolute;
        border-radius: 50%;
        filter: blur(100px);
        opacity: 0.15;
        animation: floatOrb 20s ease-in-out infinite;
    }
    .orb-1 {
        width: 500px; height: 500px;
        background: #e50914;
        top: -10%; left: -5%;
        animation-delay: 0s;
    }
    .orb-2 {
        width: 400px; height: 400px;
        background: #6c3ce0;
        top: 50%; right: -5%;
        animation-delay: -7s;
    }
    .orb-3 {
        width: 350px; height: 350px;
        background: #0ea5e9;
        bottom: -10%; left: 30%;
        animation-delay: -14s;
    }
    @keyframes floatOrb {
        0%, 100% { transform: translate(0, 0) scale(1); }
        33% { transform: translate(40px, -30px) scale(1.1); }
        66% { transform: translate(-20px, 20px) scale(0.9); }
    }

    /* ── Hero Section ── */
    .hero {
        text-align: center;
        padding: 1.5rem 0 0.5rem;
        position: relative;
        z-index: 1;
    }
    .hero-badge {
        display: inline-block;
        background: rgba(229, 9, 20, 0.12);
        border: 1px solid rgba(229, 9, 20, 0.25);
        color: #ff4d5a;
        padding: 6px 18px;
        border-radius: 50px;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 1rem;
        animation: fadeInDown 0.8s ease;
    }
    .hero h1 {
        font-family: 'Outfit', sans-serif;
        font-size: 3.5rem;
        font-weight: 900;
        color: #ffffff;
        margin: 0;
        line-height: 1.1;
        letter-spacing: -2px;
        animation: fadeInUp 0.8s ease;
    }
    .hero h1 span {
        background: linear-gradient(135deg, #e50914 0%, #ff6b6b 50%, #ffd93d 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .hero-desc {
        color: #5a6577;
        font-size: 1rem;
        margin-top: 0.6rem;
        font-weight: 400;
        animation: fadeInUp 0.8s ease 0.2s both;
    }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* ── Glass Search Bar ── */
    .glass-search {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 20px;
        padding: 1.5rem 2rem;
        margin: 1.5rem auto;
        max-width: 900px;
        position: relative;
        z-index: 1;
        animation: fadeInUp 0.8s ease 0.3s both;
    }
    .search-row {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    .search-icon {
        font-size: 1.3rem;
        color: #5a6577;
    }
    .search-hint {
        color: #3d4856;
        font-size: 0.8rem;
        margin-top: 0.6rem;
        text-align: center;
    }
    .search-hint span {
        background: rgba(255,255,255,0.05);
        padding: 2px 10px;
        border-radius: 6px;
        font-family: monospace;
        color: #5a6577;
        font-size: 0.75rem;
    }

    /* Selectbox styling */
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.04) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 14px !important;
        color: #fff !important;
        font-size: 1rem !important;
        padding: 2px 4px !important;
    }
    .stSelectbox > div > div:focus-within {
        border-color: rgba(229, 9, 20, 0.5) !important;
        box-shadow: 0 0 0 3px rgba(229, 9, 20, 0.1) !important;
    }

    /* Button */
    .stButton > button {
        background: linear-gradient(135deg, #e50914, #c2070f) !important;
        color: white !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 0.65rem 2rem !important;
        font-family: 'Poppins', sans-serif !important;
        font-size: 0.95rem !important;
        font-weight: 600 !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 4px 20px rgba(229, 9, 20, 0.3) !important;
        width: 100% !important;
    }
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.02) !important;
        box-shadow: 0 8px 30px rgba(229, 9, 20, 0.45) !important;
        background: linear-gradient(135deg, #ff1a26, #e50914) !important;
    }
    .stButton > button:active {
        transform: translateY(0) scale(0.98) !important;
    }

    /* ── Selected Movie Spotlight ── */
    .spotlight {
        background: linear-gradient(135deg, rgba(229, 9, 20, 0.06), rgba(108, 60, 224, 0.04));
        border: 1px solid rgba(229, 9, 20, 0.12);
        border-radius: 24px;
        padding: 2rem;
        margin: 1.5rem 0;
        display: flex;
        gap: 2rem;
        align-items: flex-start;
        position: relative;
        z-index: 1;
        overflow: hidden;
        animation: fadeInUp 0.6s ease;
    }
    .spotlight::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -20%;
        width: 300px;
        height: 300px;
        background: radial-gradient(circle, rgba(229,9,20,0.08) 0%, transparent 70%);
        border-radius: 50%;
    }
    .spotlight-poster {
        width: 160px;
        min-width: 160px;
        border-radius: 16px;
        box-shadow: 0 12px 30px rgba(0,0,0,0.5);
        transition: transform 0.3s ease;
    }
    .spotlight-poster:hover {
        transform: scale(1.05) rotate(1deg);
    }
    .spotlight-content {
        flex: 1;
        position: relative;
        z-index: 1;
    }
    .spotlight-title {
        font-family: 'Outfit', sans-serif;
        font-size: 1.8rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 0.6rem;
        letter-spacing: -0.5px;
    }
    .spotlight-meta {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 1rem;
        flex-wrap: wrap;
    }
    .meta-chip {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        padding: 5px 14px;
        border-radius: 50px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    .chip-rating {
        background: linear-gradient(135deg, #ffd93d, #ff9500);
        color: #1a1a2e;
    }
    .chip-year {
        background: rgba(255,255,255,0.06);
        color: #8899aa;
        border: 1px solid rgba(255,255,255,0.08);
    }
    .chip-genre {
        background: rgba(108, 60, 224, 0.12);
        color: #a78bfa;
        border: 1px solid rgba(108, 60, 224, 0.2);
    }
    .spotlight-overview {
        color: #6b7b8d;
        font-size: 0.9rem;
        line-height: 1.7;
        max-width: 600px;
    }

    /* ── Section Title ── */
    .rec-title {
        position: relative;
        z-index: 1;
        margin: 2rem 0 1.2rem;
        animation: fadeInUp 0.6s ease;
    }
    .rec-title h2 {
        font-family: 'Outfit', sans-serif;
        font-size: 1.5rem;
        font-weight: 700;
        color: #ffffff;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .rec-title h2 .highlight {
        background: linear-gradient(135deg, #e50914, #ff6b6b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .rec-title .subtitle {
        color: #3d4856;
        font-size: 0.85rem;
        margin-top: 0.3rem;
    }

    /* ── Movie Cards ── */
    .m-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.04);
        border-radius: 18px;
        overflow: hidden;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        z-index: 1;
    }
    .m-card:hover {
        transform: translateY(-10px) scale(1.02);
        border-color: rgba(229, 9, 20, 0.3);
        box-shadow: 
            0 20px 50px rgba(0, 0, 0, 0.5),
            0 0 40px rgba(229, 9, 20, 0.08);
    }
    .m-card:hover .m-overlay {
        opacity: 1;
    }
    .m-poster-wrap {
        position: relative;
        overflow: hidden;
    }
    .m-poster {
        width: 100%;
        aspect-ratio: 2/3;
        object-fit: cover;
        display: block;
        transition: transform 0.5s ease;
    }
    .m-card:hover .m-poster {
        transform: scale(1.08);
    }
    .m-overlay {
        position: absolute;
        bottom: 0; left: 0; right: 0;
        height: 60%;
        background: linear-gradient(to top, rgba(11,12,16,0.95) 0%, transparent 100%);
        opacity: 0;
        transition: opacity 0.4s ease;
        display: flex;
        align-items: flex-end;
        padding: 1rem;
    }
    .m-overlay-text {
        color: #a0aec0;
        font-size: 0.7rem;
        line-height: 1.5;
    }
    .m-rank {
        position: absolute;
        top: 10px; left: 10px;
        background: rgba(0,0,0,0.6);
        backdrop-filter: blur(8px);
        color: #ffffff;
        width: 32px; height: 32px;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.8rem;
        font-weight: 800;
        border: 1px solid rgba(255,255,255,0.1);
    }
    .m-rating-badge {
        position: absolute;
        top: 10px; right: 10px;
        background: linear-gradient(135deg, #ffd93d, #ff9500);
        color: #1a1a2e;
        padding: 3px 10px;
        border-radius: 8px;
        font-size: 0.72rem;
        font-weight: 700;
        display: flex;
        align-items: center;
        gap: 3px;
        box-shadow: 0 4px 12px rgba(255, 217, 61, 0.3);
    }
    .m-body {
        padding: 0.9rem 1rem;
    }
    .m-title {
        color: #e2e8f0;
        font-family: 'Outfit', sans-serif;
        font-size: 0.9rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
        line-height: 1.3;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }
    .m-year {
        color: #4a5568;
        font-size: 0.75rem;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    .m-genres {
        display: flex;
        gap: 5px;
        flex-wrap: wrap;
    }
    .m-genre {
        background: rgba(229, 9, 20, 0.08);
        color: #ff6b6b;
        padding: 3px 10px;
        border-radius: 50px;
        font-size: 0.6rem;
        font-weight: 600;
        letter-spacing: 0.3px;
        border: 1px solid rgba(229, 9, 20, 0.12);
    }

    /* ── Row Spacing ── */
    .row-spacer {
        height: 1.5rem;
    }

    /* ── Footer ── */
    .app-footer {
        text-align: center;
        padding: 2.5rem 0 1rem;
        position: relative;
        z-index: 1;
        animation: fadeInUp 0.6s ease;
    }
    .footer-line {
        width: 60px;
        height: 2px;
        background: linear-gradient(90deg, #e50914, #6c3ce0);
        margin: 0 auto 1rem;
        border-radius: 2px;
    }
    .footer-text {
        color: #2d3748;
        font-size: 0.78rem;
    }
    .footer-text a {
        color: #e50914;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.3s ease;
    }
    .footer-text a:hover {
        color: #ff6b6b;
    }
    .footer-links {
        margin-top: 0.5rem;
        display: flex;
        justify-content: center;
        gap: 1.5rem;
    }
    .footer-link {
        color: #3d4856;
        font-size: 0.75rem;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    .footer-link:hover {
        color: #e50914;
    }
</style>
""", unsafe_allow_html=True)

# ─── Background Effects ──────────────────────────────────────────────────────
st.markdown("""
<div class="bg-effects">
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>
</div>
""", unsafe_allow_html=True)

# ─── TMDB API Helper ─────────────────────────────────────────────────────────
TMDB_API_KEY = "8265bd1679663a7ea12ac168da84d2e8"
TMDB_BASE = "https://api.themoviedb.org/3"
POSTER_BASE = "https://image.tmdb.org/t/p/w500"
PLACEHOLDER_IMG = "https://via.placeholder.com/500x750/1a1a2e/4a5568?text=No+Poster"


def fetch_movie_details(movie_id):
    """Fetch movie details from TMDB with graceful error handling."""
    try:
        url = f"{TMDB_BASE}/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
        resp = requests.get(url, timeout=5)
        d = resp.json()
        return {
            "poster": f"{POSTER_BASE}{d['poster_path']}" if d.get("poster_path") else PLACEHOLDER_IMG,
            "genres": [g["name"] for g in d.get("genres", [])][:3],
            "rating": round(d.get("vote_average", 0), 1),
            "year": d.get("release_date", "")[:4] or "N/A",
            "overview": d.get("overview", "No overview available."),
        }
    except Exception:
        return {"poster": PLACEHOLDER_IMG, "genres": [], "rating": 0, "year": "N/A", "overview": "Details unavailable."}


def recommend(movie, num=10):
    """Get top N content-based recommendations."""
    idx = movies[movies["title"] == movie].index[0]
    dists = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
    results = []
    for i in dists[1 : num + 1]:
        mid = movies.iloc[i[0]].movie_id
        title = movies.iloc[i[0]].title
        info = fetch_movie_details(mid)
        info["title"] = title
        results.append(info)
    return results


# ─── Load Data ───────────────────────────────────────────────────────────────
@st.cache_data
def load_movies():
    return pickle.load(open("movies.pkl", "rb"))


@st.cache_resource
def load_similarity():
    import os
    if os.path.exists("similarity.pkl"):
        return pickle.load(open("similarity.pkl", "rb"))
    else:
        # Fallback: Compute similarity matrix on the fly
        from sklearn.feature_extraction.text import CountVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
        
        cv = CountVectorizer(max_features=5000, stop_words='english')
        # Ensure tags column is filled
        movies['tags'] = movies['tags'].fillna('')
        vector = cv.fit_transform(movies['tags']).toarray()
        sim = cosine_similarity(vector)
        return sim


movies = load_movies()
similarity = load_similarity()

# ─── Hero ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-badge">✨ AI-Powered Engine</div>
    <h1>Movie <span>Recommendation</span> System</h1>
    <p class="hero-desc">Discover your next favorite movie — powered by machine learning</p>
</div>
""", unsafe_allow_html=True)

# ─── Search ──────────────────────────────────────────────────────────────────
col1, col2 = st.columns([5, 1])

with col1:
    selected_movie = st.selectbox(
        "Search",
        movies["title"].values,
        index=None,
        placeholder="🔍  Search for a movie you love...",
        label_visibility="collapsed",
    )

with col2:
    show = st.button("🎯 Recommend", use_container_width=True)


# ─── Recommendations ─────────────────────────────────────────────────────────
if show and selected_movie:
    # Spotlight — selected movie
    sel_id = movies[movies["title"] == selected_movie].iloc[0].movie_id
    sel = fetch_movie_details(sel_id)

    genres_chips = " ".join([f'<span class="meta-chip chip-genre">{g}</span>' for g in sel["genres"]])

    st.markdown(f"""
    <div class="spotlight">
        <img src="{sel['poster']}" class="spotlight-poster" alt="{selected_movie}">
        <div class="spotlight-content">
            <div class="spotlight-title">{selected_movie}</div>
            <div class="spotlight-meta">
                <span class="meta-chip chip-rating">⭐ {sel['rating']}</span>
                <span class="meta-chip chip-year">📅 {sel['year']}</span>
                {genres_chips}
            </div>
            <p class="spotlight-overview">{sel['overview'][:280]}{'...' if len(sel['overview']) > 280 else ''}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Fetch recommendations
    with st.spinner("🔮 Finding perfect matches..."):
        recs = recommend(selected_movie, num=10)

    st.markdown(f"""
    <div class="rec-title">
        <h2>🍿 Because you liked <span class="highlight">{selected_movie}</span></h2>
        <p class="subtitle">Top 10 movies you'll love, ranked by similarity</p>
    </div>
    """, unsafe_allow_html=True)

    # Render 2 rows × 5 cols
    for row in range(2):
        cols = st.columns(5, gap="medium")
        for c_idx, col in enumerate(cols):
            m_idx = row * 5 + c_idx
            if m_idx < len(recs):
                m = recs[m_idx]
                with col:
                    genres_html = "".join([f'<span class="m-genre">{g}</span>' for g in m["genres"]])
                    st.markdown(f"""
                    <div class="m-card">
                        <div class="m-poster-wrap">
                            <img src="{m['poster']}" class="m-poster" alt="{m['title']}">
                            <div class="m-rank">#{m_idx + 1}</div>
                            <div class="m-rating-badge">⭐ {m['rating']}</div>
                            <div class="m-overlay">
                                <div class="m-overlay-text">{m['overview'][:120]}...</div>
                            </div>
                        </div>
                        <div class="m-body">
                            <div class="m-title">{m['title']}</div>
                            <div class="m-year">📅 {m['year']}</div>
                            <div class="m-genres">{genres_html}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
        if row == 0:
            st.markdown('<div class="row-spacer"></div>', unsafe_allow_html=True)

elif show and not selected_movie:
    st.warning("⚠️ Please select a movie first!")

# ─── Footer ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="app-footer">
    <div class="footer-line"></div>
    <p class="footer-text">
        Built with ❤️ using <a href="https://streamlit.io" target="_blank">Streamlit</a>
        &nbsp;·&nbsp; Data from <a href="https://www.themoviedb.org" target="_blank">TMDB</a>
    </p>
    <div class="footer-links">
        <a href="https://github.com/AdityaTawhare/Movie-Recommendation-System" target="_blank" class="footer-link">⭐ GitHub</a>
        <a href="https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata" target="_blank" class="footer-link">📊 Dataset</a>
    </div>
</div>
""", unsafe_allow_html=True)
