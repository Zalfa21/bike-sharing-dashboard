import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Bike Sharing Lucu", page_icon="🚲", layout="wide")

# Load dataset
@st.cache_data
def load_data():
    day = pd.read_csv('day.csv')
    hour = pd.read_csv('hour.csv')
    return day, hour

day, hour = load_data()

# Judul Dashboard dengan gambar
st.markdown("<h1 style='text-align: center; color: hotpink;'>🚲 Bike Sharing Dashboard Lucu 💖</h1>", unsafe_allow_html=True)
st.image("https://cdn-icons-png.flaticon.com/512/2972/2972185.png", width=100)

st.markdown("<p style='text-align: center;'>Selamat datang di dashboard peminjaman sepeda yang penuh warna dan semangat! 🎀</p>", unsafe_allow_html=True)

# Sidebar navigasi
menu = st.sidebar.radio(
    "🧭 Pilih Halaman:",
    ("🎒 Tentang Dataset", "📈 Statistik Umum", "📅 Visualisasi Harian", "🕒 Visualisasi Per Jam")
)

# Halaman: Tentang Dataset
if menu == "🎒 Tentang Dataset":
    st.header("📁 Tentang Dataset")
    st.write("""
    Dataset ini berasal dari proyek analisis sistem peminjaman sepeda di Washington DC. 💼
    
    Terdapat dua file utama:
    - `day.csv`: Data peminjaman sepeda per hari 📆
    - `hour.csv`: Data peminjaman sepeda per jam ⏰
    """)
    st.subheader("✨ Contoh Data Harian (`day.csv`):")
    st.dataframe(day.head())

    st.subheader("🌟 Contoh Data Per Jam (`hour.csv`):")
    st.dataframe(hour.head())

# Halaman: Statistik Umum
elif menu == "📈 Statistik Umum":
    st.header("📊 Statistik Umum")

    st.subheader("📚 Statistik Deskriptif Data Harian:")
    st.write(day.describe())

    st.subheader("💗 Total Keseluruhan Peminjaman Sepeda:")
    total = day['cnt'].sum()
    st.metric(label="Total Peminjaman 🚲", value=f"{total:,} sepeda")

# Halaman: Visualisasi Harian
elif menu == "📅 Visualisasi Harian":
    st.header("🌈 Visualisasi Peminjaman Sepeda Harian")

    st.subheader("📆 Tren Jumlah Peminjaman per Hari")
    plt.figure(figsize=(10, 4))
    plt.plot(pd.to_datetime(day['dteday']), day['cnt'], color='mediumvioletred', marker='o')
    plt.xticks(rotation=45)
    plt.title("📅 Jumlah Peminjaman Sepeda per Hari")
    plt.xlabel("Tanggal")
    plt.ylabel("Jumlah Peminjaman")
    st.pyplot(plt.gcf())

    st.subheader("🌤️ Distribusi Peminjaman berdasarkan Musim")
    plt.figure(figsize=(6, 4))
    sns.boxplot(x='season', y='cnt', data=day, palette='pastel')
    plt.title("Peminjaman Sepeda Berdasarkan Musim")
    st.pyplot(plt.gcf())

# Halaman: Visualisasi Per Jam
elif menu == "🕒 Visualisasi Per Jam":
    st.header("⏰ Visualisasi Peminjaman Sepeda per Jam")

    st.subheader("🧁 Rata-rata Peminjaman per Jam")
    avg_hour = hour.groupby('hr')['cnt'].mean()
    plt.figure(figsize=(10, 4))
    avg_hour.plot(kind='bar', color='plum')
    plt.title("💞 Rata-rata Peminjaman Sepeda per Jam")
    plt.xlabel("Jam (0-23)")
    plt.ylabel("Rata-rata Peminjaman")
    st.pyplot(plt.gcf())

    st.subheader("🍭 Heatmap Peminjaman per Jam dan Hari")
    pivot = hour.pivot_table(values='cnt', index='weekday', columns='hr', aggfunc='mean')
    plt.figure(figsize=(12, 6))
    sns.heatmap(pivot, cmap='pink', linewidths=0.3)
    plt.title("✨ Heatmap Peminjaman Sepeda")
    st.pyplot(plt.gcf())
