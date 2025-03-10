import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Mencoba Streamlit")

# Sidebar
st.sidebar.header("Jumlah Baris")
n_rows = st.sidebar.slider("Mau berapa Baris?", min_value=10, max_value=100, value=50)

data = pd.DataFrame({
    "Angka Random 1": np.random.randint(1, 100, n_rows),
    "Angka Random 2": np.random.randint(1, 100, n_rows),
    "Angka Desimal Random": np.random.rand(n_rows) * 100
})

st.subheader("Random Number Generator (TABEL)")
st.dataframe(data)

st.subheader("Data Visualization")
fig, ax = plt.subplots()
ax.hist(data["Angka Desimal Random"], bins=10, color='blue', alpha=0.7)
ax.set_xlabel("")
ax.set_ylabel("Frequency")
ax.set_title("Histogram")
st.pyplot(fig)

st.subheader("Summary Statistics")
st.metric(label="Mean 1", value=f"{data['Angka Random 1'].mean():.2f}")
st.metric(label="Mean 2", value=f"{data['Angka Random 2'].mean():.2f}")
st.metric(label="Mean Desimal", value=f"{data['Angka Desimal Random'].mean():.2f}")


