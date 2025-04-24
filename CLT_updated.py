import pandas as pd
import numpy as np

file_path = 'CLT_Datasets.xlsx'
df = pd.read_excel(file_path)

jumlah_kelompok_list = [1, 3, 7, 40, 60, 100]
sample_sizes = [20, 100]
hasil = []

for kolom in df.columns:
    data = df[kolom].dropna().to_numpy()
    mean_populasi = np.mean(data)

    for k in jumlah_kelompok_list:
        rata_20, rata_100 = None, None
        formatted_means_20, formatted_means_100 = "", ""

        for sample_size in sample_sizes:
            sample_means = []
            for i in range(k):
                sampel = np.random.choice(data, size=sample_size, replace=False)
                sample_means.append(np.mean(sampel))

            rata_rataan = np.mean(sample_means)
            formatted_means = "\n".join([f"Rataan Sampel {i+1}: {round(mean, 4)}" for i, mean in enumerate(sample_means)])

            if sample_size == 20:
                rata_20 = rata_rataan
                formatted_means_20 = formatted_means
            elif sample_size == 100:
                rata_100 = rata_rataan
                formatted_means_100 = formatted_means

        hasil.append({
            "Dataset": kolom,
            "Jumlah Kelompok Sampel": k,
            "Rataan dari Rataan 20 Sampel": round(rata_20, 4),
            "Rataan Tiap Sampel (20)": formatted_means_20,
            "Rataan dari Rataan 100 Sampel": round(rata_100, 4),
            "Rataan Tiap Sampel (100)": formatted_means_100,
            "Rataan Populasi": round(mean_populasi, 4),
            "Selisih nilai kolom 3 dan 7": round(abs(rata_20 - mean_populasi), 4),
            "Selisih nilai kolom 5 dan 7": round(abs(rata_100 - mean_populasi), 4)
        })

# Simpan ke file Excel
df_hasil = pd.DataFrame(hasil)
df_hasil.to_excel("hasil_CLT_dengan_rataan_tiap_sampel.xlsx", index=False)
print(df_hasil)
