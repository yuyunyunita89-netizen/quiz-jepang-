import streamlit as st
import random

# -----------------------------
# Daftar kosakata Jepang
kosakata = {
    "こんにちは (Konnichiwa)": "Halo / Selamat siang",
    "おはよう (Ohayou)": "Selamat pagi",
    "こんばんは (Konbanwa)": "Selamat malam",
    "さようなら (Sayounara)": "Selamat tinggal",
    "ありがとう (Arigatou)": "Terima kasih",
    "すみません (Sumimasen)": "Permisi / Maaf",
    "はい (Hai)": "Ya",
    "いいえ (Iie)": "Tidak",
    "ねこ (Neko)": "Kucing",
    "いぬ (Inu)": "Anjing",
    "みず (Mizu)": "Air",
    "たべもの (Tabemono)": "Makanan",
    "のみもの (Nomimono)": "Minuman"
}

# -----------------------------
st.title("🇯🇵 Belajar Bahasa Jepang")
st.write("Selamat datang! Pilih menu di bawah ini untuk belajar kosakata atau mencoba kuis 😊")

menu = st.sidebar.selectbox("Pilih Menu", ["📚 Lihat Kosakata", "📝 Quiz Tebak Arti"])

# -----------------------------
if menu == "📚 Lihat Kosakata":
    st.header("📚 Daftar Kosakata Jepang - Indonesia")
    for jepang, indo in kosakata.items():
        st.markdown(f"**{jepang}** ➜ {indo}")

# -----------------------------
elif menu == "📝 Quiz Tebak Arti":
    st.header("📝 Quiz Kosakata Jepang")

    if "soal" not in st.session_state:
        # acak urutan soal
        st.session_state.soal = list(kosakata.items())
        random.shuffle(st.session_state.soal)
        st.session_state.index = 0
        st.session_state.skor = 0
        st.session_state.selesai = False

    # Jika belum selesai
    if not st.session_state.selesai:
        jepang, arti_benar = st.session_state.soal[st.session_state.index]

        st.subheader(f"Arti dari kata: **{jepang}**")

        jawaban = st.text_input("Jawaban kamu (dalam bahasa Indonesia):", key=f"jawaban_{st.session_state.index}")

        if st.button("Periksa Jawaban"):
            if jawaban.strip().lower() in arti_benar.lower():
                st.success("✅ Benar!")
                st.session_state.skor += 1
            else:
                st.error(f"❌ Salah. Jawaban benar: {arti_benar}")

            st.session_state.index += 1

            if st.session_state.index >= len(st.session_state.soal):
                st.session_state.selesai = True
            else:
                st.rerun()

    # Jika sudah selesai
    else:
        st.success(f"🎉 Kuis selesai! Skor kamu: {st.session_state.skor}/{len(st.session_state.soal)}")
        if st.button("Ulangi Kuis"):
            del st.session_state["soal"]
            del st.session_state["index"]
            del st.session_state["skor"]
            del st.session_state["selesai"]
            st.rerun()
