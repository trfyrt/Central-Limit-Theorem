import pandas as pd
import numpy as np

file_path = 'CLT_Datasets.xlsx'
df = pd.read_excel(file_path)

jumlah_kelompok = [1, 5, 10, 20, 40, 50]
sample_size = 20
hasil = []

for kolom in df.columns:
    data = df[kolom].dropna().to_numpy()
    mean_populasi = np.mean(data)

    for k in jumlah_kelompok:
        sample_means = []
        for _ in range(k):
            sampel = np.random.choice(data, size=sample_size, replace=False)
            sample_means.append(np.mean(sampel))

        formatted_means = "\n".join([f"Rataan Sampel {i+1}: {round(mean, 4)}" for i, mean in enumerate(sample_means)])
        rata2_sampel = np.mean(sample_means)

        hasil.append({
            "Dataset": kolom,
            "Jumlah Kelompok Sampel": k,
            "Rataan Tiap Sampel": formatted_means,
            "Rataan dari Rataan Sampel": round(rata2_sampel, 4),
            "Rataan Populasi": round(mean_populasi, 4),
            "Selisih": round(abs(rata2_sampel - mean_populasi), 4)
        })

df_hasil = pd.DataFrame(hasil)
df_hasil.to_excel("hasil_praktikum_CLT_label.xlsx", index=False)

print(df_hasil)