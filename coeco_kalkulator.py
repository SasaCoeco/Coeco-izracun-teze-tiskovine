import streamlit as st

# Nastavitev strani
st.set_page_config(page_title="Coeco Kalkulator", page_icon="📘")

# Prikaz logotipa podjetja
st.image("crn_logo_desno_banner.png", width=180)

# Omejeni formati
formati = {
    "A6": (105, 148),
    "A5": (148, 210),
    "A4": (210, 297)
}

# Glava aplikacije
st.markdown("""
<div style='background-color:#1f4e79; padding:16px; border-radius:8px; text-align:center'>
    <h2 style='color:white;'>📘 Kalkulator teže tiskovine</h2>
    <h4 style='color:white;'>Ovitek + jedro | po številu natisnjenih strani</h4>
</div>
""", unsafe_allow_html=True)

# Informacija za uporabnika
st.info("📌 Vnesi število **strani**, ne listov. Ena polo običajno vsebuje dve strani.")

# --- Ovitek ---
st.subheader("🟦 Ovitka")

col1, col2, col3 = st.columns(3)
with col1:
    format_ovitka = st.selectbox("Format ovitka", list(formati.keys()), index=1)
with col2:
    strani_ovitka = st.number_input("Število strani ovitka", min_value=1, value=4)
with col3:
    gramatura_ovitka = st.number_input("Gramatura ovitka (g/m²)", min_value=1.0, value=60.0)

sirina_o, visina_o = formati[format_ovitka]
teza_stran_ovitka = (sirina_o * visina_o * gramatura_ovitka) / 100000 / 2
teza_ovitka = round(teza_stran_ovitka * strani_ovitka, 4)

st.success(f"Teža ovitka: **{teza_ovitka} g**")

# --- Jedro ---
st.subheader("📗 Jedro")

col4, col5, col6 = st.columns(3)
with col4:
    format_jedra = st.selectbox("Format jedra", list(formati.keys()), index=1, key="format_j")
with col5:
    strani_jedra = st.number_input("Število strani jedra", min_value=1, value=200)
with col6:
    gramatura_jedra = st.number_input("Gramatura jedra (g/m²)", min_value=1.0, value=48.8)

sirina_j, visina_j = formati[format_jedra]
teza_stran_jedra = (sirina_j * visina_j * gramatura_jedra) / 100000 / 2
teza_jedra = round(teza_stran_jedra * strani_jedra, 4)

st.success(f"Teža jedra: **{teza_jedra} g**")

# --- Skupna teža ---
skupna_teza = round(teza_ovitka + teza_jedra, 4)
st.markdown("## 📦 Skupna teža tiskovine")
st.info(f"📘 Skupna teža: **{skupna_teza} g**")

# --- Podpis avtorja ---
st.markdown("""
<hr style='margin-top:40px;'>
<p style='font-size:13px; text-align:center; color:gray;'>
Aplikacijo je zasnoval <strong>Saša Rednak | Coeco d.o.o.</strong><br>
Za natančen izračun teže tiskarskih navodil in tehnične dokumentacije.
</p>
""", unsafe_allow_html=True)