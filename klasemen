import streamlit
import pandas as pd
# ---
streamlit.title("Porkal Voli Ambarketawang 2025")
# ---
url = "https://s.id/iF2N1"
#streamlit.markdown("**Link Rekap Skor**: [s.id/iF2N1](%s)" % url)
streamlit.divider()
streamlit.write("\n\n")
# ---
# Daftar tim
teams = ["RT 01", "RT 02", "RT 03", "RT 04", "RT 05", "RT 06"]
# ---
# Inisialisasi klasemen
klasemen = pd.DataFrame({
    "Tim": teams,
    "Main": 0,
    "Menang": 0,
    "Kalah": 0,
    "Skor +": 0,
    "Skor -": 0,
    "Set +": 0,
    "Set -": 0,
    "Poin": 0
})
# ---
# Klasemen
def update_klasemen(timA, timB, skorA, skorB, setA, setB):
    global klasemen

    # Update jumlah main
    klasemen.loc[klasemen["Tim"] == timA, "Main"] += 1
    klasemen.loc[klasemen["Tim"] == timB, "Main"] += 1

    # Update skor
    klasemen.loc[klasemen["Tim"] == timA, "Skor +"] += skorA
    klasemen.loc[klasemen["Tim"] == timA, "Skor -"] += skorB
    klasemen.loc[klasemen["Tim"] == timB, "Skor +"] += skorB
    klasemen.loc[klasemen["Tim"] == timB, "Skor -"] += skorA

    # Update set
    klasemen.loc[klasemen["Tim"] == timA, "Set +"] += setA
    klasemen.loc[klasemen["Tim"] == timA, "Set -"] += setB
    klasemen.loc[klasemen["Tim"] == timB, "Set +"] += setB
    klasemen.loc[klasemen["Tim"] == timB, "Set -"] += setA

    # Tentukan menang/kalah
    if setA > setB:
        klasemen.loc[klasemen["Tim"] == timA, "Menang"] += 1
        klasemen.loc[klasemen["Tim"] == timB, "Kalah"] += 1
        # Poin
        if setA == 3 and setB <= 1:
            klasemen.loc[klasemen["Tim"] == timA, "Poin"] += 3
        elif setA == 3 and setB == 2:
            klasemen.loc[klasemen["Tim"] == timA, "Poin"] += 2
            klasemen.loc[klasemen["Tim"] == timB, "Poin"] += 1
    else:
        klasemen.loc[klasemen["Tim"] == timB, "Menang"] += 1
        klasemen.loc[klasemen["Tim"] == timA, "Kalah"] += 1
        # Poin
        if setB == 3 and setA <= 1:
            klasemen.loc[klasemen["Tim"] == timB, "Poin"] += 3
        elif setB == 3 and setA == 2:
            klasemen.loc[klasemen["Tim"] == timB, "Poin"] += 2
            klasemen.loc[klasemen["Tim"] == timA, "Poin"] += 1
# ---
# Print Klasemen
def show_klasemen():
    global klasemen

    # Hitung selisih
    klasemen["Selisih Set"] = klasemen["Set +"] - klasemen["Set -"]
    klasemen["Selisih Skor"] = klasemen["Skor +"] - klasemen["Skor -"]

    # Urutkan
    df_sorted = klasemen.sort_values(
        by=["Poin", "Selisih Set", "Selisih Skor"],
        ascending=[False, False, False]
    ).reset_index(drop=True)

    # Tambahkan nomor urut
    df_sorted.index = df_sorted.index + 1
    df_sorted.rename_axis("No", inplace=True)

    # ---------- STYLING ----------
    styled = (
        df_sorted.style
        # Gradient hijau utk Poin (semakin tinggi semakin gelap)
        .background_gradient(cmap="Greens", subset=["Poin"])
        # Gradient biru utk Selisih Set
        .background_gradient(cmap="Blues", subset=["Selisih Set"])
        # Gradient oranye utk Selisih Skor
        .background_gradient(cmap="Oranges", subset=["Selisih Skor"])
        .format({"Selisih Set": "{:+d}", "Selisih Skor": "{:+d}"})
    )

    return styled

# ==========================================
# ---
# Input hasil pertandingan (contoh data sesuai tabel Anda)
update_klasemen("RT 02", "RT 05", 51, 75, 0, 3)     #1.1_20-09-2025
update_klasemen("RT 03", "RT 04", 54, 75, 0, 3)     #1.2_20-09-2025

# ---
# Tampilkan klasemen
streamlit.subheader(":blue-background[**Klasemen Tim**]")

#Urutan untuk klasemen: berdasarkan Menang, Set Menang, dan Selisih Skor
streamlit.dataframe(show_klasemen(), use_container_width=True)
streamlit.badge("Last update: 26 Agustus 2025 22:09:54", icon=":material/check:", color="green")
# ---
streamlit.divider()
streamlit.write("\n\n")
streamlit.markdown("*Sekretariat Bola Voli Porkal Ambarketawang 2025*")
streamlit.markdown("*Made using Python and Streamlit Framework by Danis Nurmansyah*")
