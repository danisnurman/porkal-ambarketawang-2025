import streamlit
import pandas as pd
# ---
streamlit.title("Porkal Ambarketawang 2025")
streamlit.write("Klasemen Porkal Cabang Olahraga Voli Kalurahan Ambarketawang Tahun 2025")
# ---
url_rekap = "https://s.id/m4s27"
streamlit.markdown("**Link Rekap Skor**: [s.id/m4s27](%s)" % url_rekap)
streamlit.divider()
streamlit.write("\n\n")
# ---
# Daftar tim
teamsA = ["Mancasan A", "Gamping Kidul", "Mejing Wetan A", "Kalimanjung", "Mejing Kidul"]
teamsB = ["Mancasan B", "Tlogo", "Mejing Wetan B", "Mejing Lor", "Watulangkah"]
# ---
# Inisialisasi klasemen
klasemenA = pd.DataFrame({
    "Tim": teamsA,
    "P": 0,
    "W": 0,
    "L": 0,
    "Skor +": 0,
    "Skor -": 0,
    "Set +": 0,
    "Set -": 0,
    "Poin": 0
})
klasemenB = pd.DataFrame({
    "Tim": teamsB,
    "P": 0,
    "W": 0,
    "L": 0,
    "Skor +": 0,
    "Skor -": 0,
    "Set +": 0,
    "Set -": 0,
    "Poin": 0
})
# ---
# Klasemen Grup A
def update_klasemen_A(timA, timB, skorA, skorB, setA, setB):
    global klasemen

    # Update jumlah main
    klasemenA.loc[klasemenA["Tim"] == timA, "P"] += 1
    klasemenA.loc[klasemenA["Tim"] == timB, "P"] += 1

    # Update skor
    klasemenA.loc[klasemenA["Tim"] == timA, "Skor +"] += skorA
    klasemenA.loc[klasemenA["Tim"] == timA, "Skor -"] += skorB
    klasemenA.loc[klasemenA["Tim"] == timB, "Skor +"] += skorB
    klasemenA.loc[klasemenA["Tim"] == timB, "Skor -"] += skorA

    # Update set
    klasemenA.loc[klasemenA["Tim"] == timA, "Set +"] += setA
    klasemenA.loc[klasemenA["Tim"] == timA, "Set -"] += setB
    klasemenA.loc[klasemenA["Tim"] == timB, "Set +"] += setB
    klasemenA.loc[klasemenA["Tim"] == timB, "Set -"] += setA

    # Tentukan menang/kalah
    if setA > setB:
        klasemenA.loc[klasemenA["Tim"] == timA, "W"] += 1
        klasemenA.loc[klasemenA["Tim"] == timB, "L"] += 1
        # Poin
        if setA == 3 and setB <= 1:
            klasemenA.loc[klasemenA["Tim"] == timA, "Poin"] += 3
        elif setA == 3 and setB == 2:
            klasemenA.loc[klasemenA["Tim"] == timA, "Poin"] += 2
            klasemenA.loc[klasemenA["Tim"] == timB, "Poin"] += 1
    else:
        klasemenA.loc[klasemenA["Tim"] == timB, "W"] += 1
        klasemenA.loc[klasemenA["Tim"] == timA, "L"] += 1
        # Poin
        if setB == 3 and setA <= 1:
            klasemenA.loc[klasemenA["Tim"] == timB, "Poin"] += 3
        elif setB == 3 and setA == 2:
            klasemenA.loc[klasemenA["Tim"] == timB, "Poin"] += 2
            klasemenA.loc[klasemenA["Tim"] == timA, "Poin"] += 1

# Klasemen Grup B
def update_klasemen_B(timA, timB, skorA, skorB, setA, setB):
    global klasemenB

    # Update jumlah main
    klasemenB.loc[klasemenB["Tim"] == timA, "P"] += 1
    klasemenB.loc[klasemenB["Tim"] == timB, "P"] += 1

    # Update skor
    klasemenB.loc[klasemenB["Tim"] == timA, "Skor +"] += skorA
    klasemenB.loc[klasemenB["Tim"] == timA, "Skor -"] += skorB
    klasemenB.loc[klasemenB["Tim"] == timB, "Skor +"] += skorB
    klasemenB.loc[klasemenB["Tim"] == timB, "Skor -"] += skorA

    # Update set
    klasemenB.loc[klasemenB["Tim"] == timA, "Set +"] += setA
    klasemenB.loc[klasemenB["Tim"] == timA, "Set -"] += setB
    klasemenB.loc[klasemenB["Tim"] == timB, "Set +"] += setB
    klasemenB.loc[klasemenB["Tim"] == timB, "Set -"] += setA

    # Tentukan menang/kalah
    if setA > setB:
        klasemenB.loc[klasemenB["Tim"] == timA, "W"] += 1
        klasemenB.loc[klasemenB["Tim"] == timB, "L"] += 1
        # Poin
        if setA == 3 and setB <= 1:
            klasemenB.loc[klasemenB["Tim"] == timA, "Poin"] += 3
        elif setA == 3 and setB == 2:
            klasemenB.loc[klasemenB["Tim"] == timA, "Poin"] += 2
            klasemenB.loc[klasemenB["Tim"] == timB, "Poin"] += 1
    else:
        klasemenB.loc[klasemenB["Tim"] == timB, "W"] += 1
        klasemenB.loc[klasemenB["Tim"] == timA, "L"] += 1
        # Poin
        if setB == 3 and setA <= 1:
            klasemenB.loc[klasemenB["Tim"] == timB, "Poin"] += 3
        elif setB == 3 and setA == 2:
            klasemenB.loc[klasemenB["Tim"] == timB, "Poin"] += 2
            klasemenB.loc[klasemenB["Tim"] == timA, "Poin"] += 1
# ---
# Fungsi highlight untuk juara grup
def highlight_top2(row):
    if row.name == 1 or row.name == 2:
        return ['background-color: green'] * len(row)
    else:
        return [''] * len(row)

# Print Klasemen
def show_klasemenA():
    global klasemenA

    # Hitung selisih
    klasemenA["Selisih Set"] = klasemenA["Set +"] - klasemenA["Set -"]
    klasemenA["Selisih Skor"] = klasemenA["Skor +"] - klasemenA["Skor -"]

    # Urutkan
    df_sorted = klasemenA.sort_values(
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
        .apply(highlight_top2, subset=["Tim", "P", "W", "L"], axis=1)
    )

    return styled
    
def show_klasemenB():
    global klasemenB

    # Hitung selisih
    klasemenB["Selisih Set"] = klasemenB["Set +"] - klasemenB["Set -"]
    klasemenB["Selisih Skor"] = klasemenB["Skor +"] - klasemenB["Skor -"]

    # Urutkan
    df_sorted = klasemenB.sort_values(
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
        .apply(highlight_top2, subset=["Tim", "P", "W", "L"], axis=1)
    )

    return styled

# ==========================================
# ---
# Input hasil pertandingan (contoh data sesuai tabel Anda)
update_klasemen_B("Mejing Wetan B", "Mejing Lor", 114, 103, 3, 2)     #1.1_20-09-2025
update_klasemen_B("Mancasan B", "Watulangkah", 102, 109, 2, 3)        #1.2_20-09-2025
update_klasemen_A("Mejing Wetan A", "Kalimanjung", 75, 57, 3, 0)      #2.1_21-09-2025
update_klasemen_A("Mejing Kidul", "Gamping Kidul", 78, 66, 3, 0)      #2.1_21-09-2025
update_klasemen_B("Mancasan B", "Mejing Wetan B", 109, 108, 2, 3)     #3.1_22-09-2025
update_klasemen_B("Tlogo", "Watulangkah", 64, 77, 0, 3)               #3.2_22-09-2025
update_klasemen_A("Mancasan A", "Kalimanjung", 75, 49, 3, 0)          #4.1_23-09-2025
update_klasemen_A("Mejing Kidul", "Mejing Wetan A", 75, 45, 3, 0)     #4.2_23-09-2025
update_klasemen_B("Watulangkah", "Mejing Wetan B", 112, 99, 3, 2)     #5.1_24-09-2025
update_klasemen_B("Tlogo", "Mejing Lor", 75, 64, 3, 0)                #5.2_24-09-2025
update_klasemen_A("Kalimanjung", "Gamping Kidul", 80, 102, 1, 3)      #6.1_25-09-2025
update_klasemen_A("Mancasan A", "Mejing Wetan A", 75, 37, 3, 0)       #6.2_25-09-2025
update_klasemen_B("Tlogo", "Mejing Wetan B", 75, 68, 3, 0)            #7.1_26-09-2025
update_klasemen_B("Mejing Lor", "Mancasan B", 58, 75, 0, 3)           #7.2_26-09-2025
update_klasemen_A("Mancasan A", "Gamping Kidul", 75, 55, 3, 0)        #8.1_27-09-2025
update_klasemen_A("Kalimanjung", "Mejing Kidul", 0, 75, 0, 3)         #8.2_27-09-2025
update_klasemen_B("Watulangkah", "Mejing Lor", 77, 65, 3, 0)          #9.1_28-09-2025
update_klasemen_B("Tlogo", "Mancasan B", 98, 80, 3, 1)                #9.2_28-09-2025
update_klasemen_A("Mejing Wetan A", "Gamping Kidul", 0, 75, 0, 3)        #10.1_29-09-2025
update_klasemen_A("Mancasan A", "Mejing Kidul", 95, 94, 1, 3)         #10.2_29-09-2025

# ---
# Urutan untuk klasemen: berdasarkan Menang, Set Menang, dan Selisih Skor
# Tampilkan klasemen A
streamlit.subheader(":red-background[**Klasemen Grup A**]")
streamlit.dataframe(show_klasemenA(), use_container_width=False)
streamlit.badge("Last update: 29 September 2025 23:33:46", icon=":material/check:", color="green")
# new line
streamlit.divider()
streamlit.write("\n\n")
# Tampilkan klasemen B
streamlit.subheader(":blue-background[**Klasemen Grup B**]")
streamlit.dataframe(show_klasemenB(), use_container_width=False)
streamlit.badge("Last update: 29 September 2025 01:02:21", icon=":material/check:", color="green")
# ---
streamlit.divider()
streamlit.write("\n\n")
streamlit.markdown("*Panitia Porkal Cabang Olahraga Voli Kalurahan Ambarketawang 2025*")

# Copyright
url_linkedin = "https://www.linkedin.com/in/dnnurman/"
streamlit.markdown("*Made using Python and Streamlit Framework by [Danis Nurmansyah](%s)*" % url_linkedin)
