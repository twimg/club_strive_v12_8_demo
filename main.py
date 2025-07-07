import streamlit as st
import pandas as pd
import os

# タイトル
st.set_page_config(page_title="Club Strive Demo", layout="wide")
st.title("⚽ Club Strive - v12.8 Demo")

# データ読み込み
data_path = "data/players.csv"
if os.path.exists(data_path):
    df = pd.read_csv(data_path)
    st.subheader("選手一覧")
    st.dataframe(df)
else:
    st.warning("選手データが見つかりません。`data/players.csv` をアップロードしてください。")

# 簡易フィルター機能
if 'df' in locals():
    country = st.selectbox("国籍で絞り込む", ["すべて"] + sorted(df["国籍"].unique()))
    if country != "すべて":
        filtered_df = df[df["国籍"] == country]
        st.dataframe(filtered_df)
