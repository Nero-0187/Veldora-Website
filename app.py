import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

# ──────────────────────────────────────────────────────────────────────────────
# 1. PAGE CONFIGURATION
# ──────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Veldora Ventures — Helaian Kertas Jiwa",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ──────────────────────────────────────────────────────────────────────────────
# 2. IMAGE LIBRARY
# ──────────────────────────────────────────────────────────────────────────────
IMG = {
    "hero":     "https://images.unsplash.com/photo-1507842217343-583bb7270b66?auto=format&fit=crop&w=1920&q=80",
    "library":  "https://images.unsplash.com/photo-1521587760476-6c12a4b040da?auto=format&fit=crop&w=1600&q=80",
    "shelves":  "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?auto=format&fit=crop&w=1600&q=80",
    "lounge":   "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?auto=format&fit=crop&w=1600&q=80",
    "reading":  "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?auto=format&fit=crop&w=1600&q=80",
    "warm":     "https://images.unsplash.com/photo-1532012197267-da84d127e765?auto=format&fit=crop&w=1600&q=80",
    "novel":    "https://images.unsplash.com/photo-1474366521946-c3d4b507abf2?auto=format&fit=crop&w=1200&q=80",
    "horror":   "https://images.unsplash.com/photo-1509248961158-e54f6934749c?auto=format&fit=crop&w=1200&q=80",
    "majalah":  "https://images.unsplash.com/photo-1585241645927-c7a8e5840c42?auto=format&fit=crop&w=1200&q=80",
    "anime":    "https://images.unsplash.com/photo-1578632767115-351597cf2477?auto=format&fit=crop&w=1200&q=80",
    "religion": "https://images.unsplash.com/photo-1585036156171-384164a8c675?auto=format&fit=crop&w=1200&q=80",
    "english":  "https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=1200& retrospective=80",
    "contact":  "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?auto=format&fit=crop&w=1600&q=80",
}

# ──────────────────────────────────────────────────────────────────────────────
# 3. DATA STRUCTURES
# ──────────────────────────────────────────────────────────────────────────────
CATEGORIES = [
    ("Novel & Sastera", "Cerita-cerita yang menyentuh jiwa dan karya sastera pilihan.", IMG["novel"]),
    ("Horror",          "Kisah seram dan misteri yang mendebarkan untuk pembaca berani.", IMG["horror"]),
    ("Majalah",         "Majalah terkini penuh ilmu, gaya hidup dan inspirasi.",          IMG["majalah"]),
    ("Anime",           "Dunia anime dan manga yang penuh warna dan imaginasi.",          IMG["anime"]),
    ("Religion",        "Bacaan keagamaan untuk ketenangan dan pedoman hidup.",           IMG["religion"]),
    ("English",         "A curated selection of English reads for every reader.",          IMG["english"]),
]

NAV_CHANNELS = ["OVERVIEW", "COLLECTIONS", "ANALYTICS", "CREDENTIALS", "CONTACT & REVIEWS"]

# ──────────────────────────────────────────────────────────────────────────────
# 4. ULTRA-TARGETED CSS (FORMULA ANTI-OVERRIDE STREAMLIT)
# ──────────────────────────────────────────────────────────────────────────────
def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Jost:wght@300;400;500;600;700&display=swap');

    :root {
        --primary: #4A3428; --secondary: #5C4033; --accent: #A67C52;
        --beige: #DCC7AA; --paper: #EADFCF; --gold: #C8A165;
        --h: #2E2118; --body: #4B3A2D; --cream: #F5ECDD;
    }

    #MainMenu {visibility:hidden;}
    footer {visibility:hidden;}
    header[data-testid="stHeader"] {background:transparent; height:0;}

    .stApp {
        background: linear-gradient(135deg, rgba(74,52,40,0.04), rgba(92,64,51,0.06)), #EADFCF;
        color: var(--body);
        font-family: 'Jost', sans-serif;
    }
    
    .block-container {padding-top:1.2rem; max-width:1200px;}
    h1, h2, h3, h4 {font-family:'Cormorant Garamond',serif; color:var(--h) !important; font-weight:600;}
    h1 {font-size:3rem; letter-spacing:.5px;}
    p, li {font-size:1.05rem; line-height:1.65; color:var(--body);}

    /* ── BRAND TOP BAR ── */
    .topbar {
        background: #4A3525;
        box-shadow: 0 8px 24px rgba(46,33,24,.30);
        border-bottom: 3px solid var(--gold);
        border-radius: 12px 12px 0 0;
        padding: 1.2rem 1.5rem 1rem;
        margin-bottom: 0;
    }
    .brand {display:flex; align-items:baseline; gap:.8rem;}
    .brand .name {
        font-family: 'Cormorant Garamond', serif; font-size: 1.8rem; font-weight: 700;
        color: #FFFFFF !important; letter-spacing: 2px;
    }
    .brand .tag {font-size: .78rem; letter-spacing: 2.5px; text-transform: uppercase; color: var(--gold) !important;}

    /* ── NAVIGATION CONTAINER STRIP ── */
    .nav-row {
        background: #4A3525; 
        border-radius: 0 0 12px 12px;
        padding: .8rem .8rem;
        margin-bottom: 2rem;
        box-shadow: 0 8px 22px rgba(46,33,24,.16);
    }

    /* SEMAKAN LINE-BY-LINE MACAM PRO:
       Streamlit versi baru membungkus teks butang di dalam tag <p> atau <span>.
       Sebab itu warna latar belakang berubah, tapi tulisan kekal 'halimunan'.
       Kita akan sasarkan terus ke akar umbi elemen tersebut mengikut attribute `data-testid`.
    */

    /* ==========================================================================
       A) BUTANG TIDAK AKTIF / INACTIVE (Streamlit Secondary Button)
       ========================================================================== */
    /* Target Latar Belakang Butang Inactive */
    div.nav-row div[data-testid="stButton"] button[data-testid="stBaseButton-secondary"],
    div.subnav-panel div[data-testid="stButton"] button[data-testid="stBaseButton-secondary"] {
        background-color: #F5E6D3 !important; 
        border: 1px solid #DCC7AA !important;
        border-radius: 4px !important;
        height: 48px !important;
        width: 100% !important;
        transition: all 0.2s ease-in-out !important;
    }

    /* Paksa Tulisan Butang Inactive Menjadi Coklat Gelap Pekat (Contrast Tinggi) */
    div.nav-row div[data-testid="stButton"] button[data-testid="stBaseButton-secondary"] p,
    div.nav-row div[data-testid="stButton"] button[data-testid="stBaseButton-secondary"] span,
    div.subnav-panel div[data-testid="stButton"] button[data-testid="stBaseButton-secondary"] p,
    div.subnav-panel div[data-testid="stButton"] button[data-testid="stBaseButton-secondary"] span {
        color: #4A3525 !important;
        font-weight: 700 !important;
        font-family: 'Jost', sans-serif !important;
        font-size: .88rem !important;
        letter-spacing: 1px !important;
        text-transform: uppercase !important;
    }

    /* Efek Hover untuk Butang Inactive */
    div.nav-row div[data-testid="stButton"] button[data-testid="stBaseButton-secondary"]:hover,
    div.subnav-panel div[data-testid="stButton"] button[data-testid="stBaseButton-secondary"]:hover {
        background-color: #EAD8C1 !important;
    }
    div.nav-row div[data-testid="stButton"] button[data-testid="stBaseButton-secondary"]:hover p,
    div.subnav-panel div[data-testid="stButton"] button[data-testid="stBaseButton-secondary"]:hover p {
        color: #2E2118 !important;
    }

    /* ==========================================================================
       B) BUTANG AKTIF / DITEKAN / ACTIVE (Streamlit Primary Button)
       ========================================================================== */
    /* Target Latar Belakang Butang Active (Gold Mewah) */
    div.nav-row div[data-testid="stButton"] button[data-testid="stBaseButton-primary"],
    div.subnav-panel div[data-testid="stButton"] button[data-testid="stBaseButton-primary"] {
        background-color: #C8A165 !important; 
        border: 1px solid #C8A165 !important;
        border-radius: 4px !important;
        height: 48px !important;
        width: 100% !important;
    }

    /* Paksa Tulisan Butang Active Menjadi Hitam/Coklat Gelap Pekat Kontras */
    div.nav-row div[data-testid="stButton"] button[data-testid="stBaseButton-primary"] p,
    div.nav-row div[data-testid="stButton"] button[data-testid="stBaseButton-primary"] span,
    div.subnav-panel div[data-testid="stButton"] button[data-testid="stBaseButton-primary"] p,
    div.subnav-panel div[data-testid="stButton"] button[data-testid="stBaseButton-primary"] span {
        color: #1A100A !important;
        font-weight: 800 !important;
        font-family: 'Jost', sans-serif !important;
        font-size: .88rem !important;
        letter-spacing: 1px !important;
        text-transform: uppercase !important;
    }

    /* Efek Hover untuk Butang Active */
    div.nav-row div[data-testid="stButton"] button[data-testid="stBaseButton-primary"]:hover,
    div.subnav-panel div[data-testid="stButton"] button[data-testid="stBaseButton-primary"]:hover {
        background-color: #B58F54 !important;
    }

    /* ── SUB NAV STRIP PANEL ── */
    .subnav-panel {
        background: rgba(74, 53, 37, 0.08);
        border: 1px solid rgba(166, 124, 82, 0.3);
        border-radius: 8px;
        padding: .5rem;
        margin-bottom: 2rem;
    }
    div.subnav-panel div[data-testid="stButton"] button {
        height: 40px !important;
    }

    /* PREMIUM LAYOUT COMPONENTS */
    .hero {
        position: relative; border-radius: 18px; overflow: hidden;
        height: 440px; display: flex; align-items: center; justify-content: center;
        text-align: center; margin-bottom: 2.5rem;
        box-shadow: 0 20px 50px rgba(46,33,24,.35);
    }
    .hero::before {
        content: ""; position: absolute; inset: 0;
        background: linear-gradient(180deg, rgba(46,33,24,.60), rgba(74,52,40,.85));
    }
    .hero-inner {position: relative; z-index: 2; padding: 0 1.5rem; max-width: 820px;}
    .hero-inner h1 {color: var(--cream) !important; text-shadow: 0 4px 18px rgba(0,0,0,.6); font-size: 3.2rem;}
    .hero-inner p {color: #F0E6D6 !important; font-size: 1.2rem;}
    .eyebrow {
        display: inline-block; letter-spacing: 4px; text-transform: uppercase;
        font-size: .8rem; color: var(--gold) !important; margin-bottom: .6rem; font-weight: 600;
    }

    .card {
        background: rgba(255,255,255,.65); backdrop-filter: blur(8px);
        border: 1px solid rgba(166,124,82,.30); border-radius: 14px; padding: 1.8rem;
        box-shadow: 0 10px 30px rgba(46,33,24,.10); height: 100%;
    }
    .media {
        border-radius: 14px; overflow: hidden; box-shadow: 0 12px 30px rgba(46,33,24,.15); background: #fff; height: 100%;
    }
    .media img {width: 100%; height: 220px; object-fit: cover;}
    .media .body {padding: 1.2rem 1.3rem 1.5rem; background: #FBF6EC;}
    
    .badge {
        display: inline-block; background: var(--gold); color: #2E2118 !important;
        font-weight: 600; font-size: .70rem; letter-spacing: 1px; text-transform: uppercase;
        padding: .25rem .65rem; border-radius: 4px; margin-bottom: .5rem;
    }
    .price {font-family: 'Cormorant Garamond',serif; font-size: 1.6rem; color: var(--secondary) !important; font-weight: 700;}
    .stars {color: var(--gold) !important; letter-spacing: 2px;}

    .metric {
        background: linear-gradient(160deg, var(--primary), var(--secondary));
        border-radius: 14px; padding: 1.6rem 1.4rem; text-align: center; height: 100%;
    }
    .metric .num {font-family: 'Cormorant Garamond',serif; font-size: 2.8rem; color: #F4E7CF !important; font-weight: 700;}
    .metric .lbl {color: #E3D2B8 !important; letter-spacing: 1px; text-transform: uppercase; font-size: .78rem;}
    .rule {height: 2px; width: 70px; background: var(--gold); border: none; margin: .4rem 0 1.6rem;}
    
    /* Form Buttons Override */
    div[data-testid="stForm"] button {
        background: var(--primary) !important; color: var(--cream) !important;
    }
    .stTextInput input, .stTextArea textarea {color: var(--body) !important; background: #FBF6EC !important;}
    </style>
    """, unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────────────
# 5. CORE HELPER FUNCTIONS
# ──────────────────────────────────────────────────────────────────────────────
def scroll_to_top(page_key: str):
    components.html(
        f"""
        <script>
            const tick = "{page_key}";
            function toTop() {{
                try {{
                    const doc = window.parent.document;
                    const targets = [
                        doc.querySelector('section[data-testid="stMain"]'),
                        doc.querySelector('section.main'), doc.querySelector('.main'),
                        doc.scrollingElement, doc.documentElement, doc.body
                    ];
                    targets.forEach(t => {{ if (t) {{ t.scrollTo ? t.scrollTo(0,0) : (t.scrollTop = 0); }} }});
                    window.parent.scrollTo(0, 0);
                }} catch (e) {{}}
            }}
            toTop(); setTimeout(toTop, 60); setTimeout(toTop, 200);
        </script>
        """, height=0,
    )

def hero(title, subtitle, image, eyebrow="Veldora Ventures"):
    st.markdown(f"""
    <div class="hero" style="background:url('{image}') center/cover no-repeat;">
        <div class="hero-inner">
            <span class="eyebrow">{eyebrow}</span>
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def stars(n):
    return "★" * int(n) + "☆" * (5 - int(n))

# ──────────────────────────────────────────────────────────────────────────────
# 6. MANAGEMENT FOR TASKS / CHANNELS (ROUTING INTERFACE)
# ──────────────────────────────────────────────────────────────────────────────
def top_nav():
    st.markdown("""
    <div class="topbar">
        <div class="brand">
            <span class="name">VELDORA VENTURES</span>
            <span class="tag">Helaian Kertas Jiwa</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="nav-row">', unsafe_allow_html=True)
    cols = st.columns(len(NAV_CHANNELS))
    for col, channel in zip(cols, NAV_CHANNELS):
        with col:
            current_p = st.session_state.page
            
            is_active = False
            if channel == "OVERVIEW" and current_p in ["Home", "About Us", "Vision & Mission"]:
                is_active = True
            elif channel == "COLLECTIONS" and current_p in ["Categories", "Featured", "Best Sellers"]:
                is_active = True
            elif channel == "ANALYTICS" and current_p == "Market":
                is_active = True
            elif channel == "CREDENTIALS" and current_p == "SSM":
                is_active = True
            elif channel == "CONTACT & REVIEWS" and current_p == "Contact":
                is_active = True

            if st.button(
                channel,
                key=f"nav_{channel}",
                use_container_width=True,
                type="primary" if is_active else "secondary",
            ):
                if channel == "OVERVIEW": st.session_state.page = "Home"
                elif channel == "COLLECTIONS": st.session_state.page = "Categories"
                elif channel == "ANALYTICS": st.session_state.page = "Market"
                elif channel == "CREDENTIALS": st.session_state.page = "SSM"
                elif channel == "CONTACT & REVIEWS": st.session_state.page = "Contact"
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # Submenus Navigation Strip Row
    if st.session_state.page in ["Home", "About Us", "Vision & Mission"]:
        st.markdown('<div class="subnav-panel">', unsafe_allow_html=True)
        sub_cols = st.columns([1.2, 1.2, 1.5, 4.1])
        with sub_cols[0]:
            if st.button("OVERVIEW", type="primary" if st.session_state.page == "Home" else "secondary", key="sub_h", use_container_width=True):
                st.session_state.page = "Home"; st.rerun()
        with sub_cols[1]:
            if st.button("OUR STORY", type="primary" if st.session_state.page == "About Us" else "secondary", key="sub_a", use_container_width=True):
                st.session_state.page = "About Us"; st.rerun()
        with sub_cols[2]:
            if st.button("VISION & MISSION", type="primary" if st.session_state.page == "Vision & Mission" else "secondary", key="sub_v", use_container_width=True):
                st.session_state.page = "Vision & Mission"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
                
    elif st.session_state.page in ["Categories", "Featured", "Best Sellers"]:
        st.markdown('<div class="subnav-panel">', unsafe_allow_html=True)
        sub_cols = st.columns([1.5, 1.5, 1.5, 3.5])
        with sub_cols[0]:
            if st.button("MAIN CATEGORIES", type="primary" if st.session_state.page == "Categories" else "secondary", key="sub_c", use_container_width=True):
                st.session_state.page = "Categories"; st.rerun()
        with sub_cols[1]:
            if st.button("FEATURED BOOKS", type="primary" if st.session_state.page == "Featured" else "secondary", key="sub_f", use_container_width=True):
                st.session_state.page = "Featured"; st.rerun()
        with sub_cols[2]:
            if st.button("BEST SELLERS", type="primary" if st.session_state.page == "Best Sellers" else "secondary", key="sub_b", use_container_width=True):
                st.session_state.page = "Best Sellers"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────────────
# 7. VIEWS DEFINITIONS
# ──────────────────────────────────────────────────────────────────────────────
def page_home():
    hero("Tempat Cerita Hidup dan Jiwa Berlabuh", 
         "Discover stories that bring comfort, thrill, and reflection in a sanctuary built for readers.", 
         IMG["hero"], eyebrow="Helaian Kertas Jiwa")

    st.markdown("## A Harbor of Stories")
    st.markdown('<hr class="rule">', unsafe_allow_html=True)

    a, b = st.columns([1.1, 1])
    with a:
        st.markdown("""
        <div class="card">
        <p>True to our tagline, <em>"Tempat Cerita Hidup dan Jiwa Berlabuh"</em>, we believe a good
        book is a sanctuary. In a world that rarely slows down, Veldora Ventures is your quiet,
        classic, and cozy online corner — a place to pause, pick up a book, and let your mind wander.</p>
        <p>We are not just selling pages, we are building a peaceful haven for your imagination
        to rest and grow. Welcome to our harbor of stories.</p>
        </div>
        """, unsafe_allow_html=True)
    with b:
        st.image(IMG["lounge"], use_container_width=True)

def page_about():
    hero("About Us", "Where a shared love of reading became a sanctuary for stories.", IMG["library"])
    a, b = st.columns([1, 1.1])
    with a:
        st.image(IMG["reading"], use_container_width=True)
    with b:
        st.markdown("""
        <div class="card">
        <p>It all began five years ago with a simple, shared passion — a profound love for reading.
        For us, diving into the pages of a novel or a magazine wasn’t just a pastime, it was a way to
        discover new worlds, gain knowledge, and find moments of quiet reflection.</p>
        </div>
        """, unsafe_allow_html=True)

def page_vision():
    hero("Vision & Mission", "The guiding light behind every story we share.", IMG["shelves"])
    a, b = st.columns(2)
    with a:
        st.markdown('<div class="card"><span class="badge">Our Vision</span><h3>A Peaceful Escape</h3><p>To be the favorite online bookstore where people everywhere can find a peaceful escape through reading.</p></div>', unsafe_allow_html=True)
    with b:
        st.markdown('<div class="card"><span class="badge">Our Mission</span><h3>Reading Made Easy</h3><p>To make reading fun and easy by delivering the best romance and horror stories straight to your screen.</p></div>', unsafe_allow_html=True)

def page_collections():
    hero("Our Categories", "Browse the official Veldora Ventures reading categories.", IMG["shelves"])
    rows = [CATEGORIES[i:i + 3] for i in range(0, len(CATEGORIES), 3)]
    for row in rows:
        cols = st.columns(3)
        for col, (title, desc, img) in zip(cols, row):
            with col:
                st.markdown(f'<div class="media"><img src="{img}"><div class="body"><h3>{title}</h3><p>{desc}</p></div></div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

def page_books():
    hero("Featured Products", "Live storefront selections synchronized with Helaian Kertas Jiwa.", IMG["english"])
    books = [
        ("Atas Pelamin Bertemu Jua", "Novel & Sastera", 5, "RM 7.80", IMG["novel"]),
        ("Novel Melayu Fixi Series",  "Horror",          5, "RM 10.00", IMG["horror"]),
        ("Majalah Humor Gila-Gila",    "Majalah",         4, "RM 7.99", IMG["majalah"]),
    ]
    cols = st.columns(3)
    for col, (title, genre, rate, price, img) in zip(cols, books):
        with col:
            st.markdown(f'<div class="media"><img src="{img}"><div class="body"><span class="badge">{genre}</span><h3>{title}</h3><div class="stars">{stars(rate)}</div><p class="price">{price}</p></div></div>', unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────────────
# FIXED: MEMASUKKAN BUKU SEBENAR DENGAN REKA BENTUK CARD ASAL (TIADA PERUBAHAN GAYA)
# ──────────────────────────────────────────────────────────────────────────────
def page_bestsellers():
    hero("Best Sellers", "The categories our readers love most.", IMG["novel"])
    
    # Memetakan buku terlaris syarikat menggunakan template seni reka asal .media & .card anda
    bestsellers = [
        ("Atas Pelamin Bertemu Jua", "Novel & Sastera", 5, "RM 7.80", IMG["novel"]),
        ("Novel Melayu Fixi Series",  "Horror",          5, "RM 10.00", IMG["horror"]),
        ("Majalah Humor Gila-Gila",    "Majalah",         4, "RM 7.99", IMG["majalah"]),
    ]
    cols = st.columns(3)
    for col, (title, genre, rate, price, img) in zip(cols, bestsellers):
        with col:
            st.markdown(f'<div class="media"><img src="{img}"><div class="body"><span class="badge">🔥 Best Seller · {genre}</span><h3>{title}</h3><div class="stars">{stars(rate)}</div><p class="price">{price}</p></div></div>', unsafe_allow_html=True)

def page_market():
    hero("Market Performance", "Our analytical growth as a digital literary brand.", IMG["library"])
    m = st.columns(4)
    metrics = [("RM 609.83", "Monthly Revenue"), ("23", "Successful Orders"), ("1.52%", "Conversion Rate"), ("4.9", "Avg. Shop Rating")]
    for col, (num, lbl) in zip(m, metrics):
        with col:
            st.markdown(f'<div class="metric"><div class="num">{num}</div><div class="lbl">{lbl}</div></div>', unsafe_allow_html=True)

def page_ssm():
    hero("Corporate Legitimacy", "Official registration and legal statutory data.", IMG["warm"])
    st.markdown('<div class="card"><h3>SSM Registered: Veldora Ventures</h3><p>Registration No: 202603094530 (003840271-D). Verified Active.</p></div>', unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────────────
# FIXED: MENAMBAH SOSIAL MEDIA RASMI & MEDAN BORANG (EMAIL & PHONE) TANPA USIK CODE GAYA
# ──────────────────────────────────────────────────────────────────────────────
def page_contact():
    hero("Contact Us", "Every great story starts with a conversation.", IMG["contact"])
    a, b = st.columns(2)
    with a:
        st.markdown("""
        <div class="card">
        <h3>Get in Touch</h3>
        <p>
        <b>Email:</b> VeldoraVent@gmail.com<br>
        <b>Phone:</b> 013-851-8815<br>
        <b>Instagram:</b> @helaian_kertas_jiwa<br>
        <b>Shopee Store:</b> Helaian_Kertas_Jiwa<br><br>
        <b>HQ Address:</b><br>
        No. 27, Jalan Alam Suria 15/3/1,<br>
        42300 Bandar Puncak Alam,<br>
        Selangor Darul Ehsan, Malaysia.
        </p>
        </div>
        """, unsafe_allow_html=True)
    with b:
        with st.form("contact_form"):
            st.text_input("Your Name")
            st.text_input("Your Email Address")
            st.text_input("Your Phone Number")
            st.text_area("Your Message")
            st.form_submit_button("SUBMIT MESSAGE")

# ──────────────────────────────────────────────────────────────────────────────
# 8. CORE APPLICATION ROUTER
# ──────────────────────────────────────────────────────────────────────────────
VIEW_ROUTER = {
    "Home": page_home, "About Us": page_about, "Vision & Mission": page_vision,
    "Categories": page_collections, "Featured": page_books, "Best Sellers": page_bestsellers,
    "Market": page_market, "SSM": page_ssm, "Contact": page_contact,
}

inject_css()

if "page" not in st.session_state:
    st.session_state.page = "Home"

top_nav()
scroll_to_top(st.session_state.page)
VIEW_ROUTER[st.session_state.page]()