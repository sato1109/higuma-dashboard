import streamlit as st
import folium
from streamlit_folium import folium_static
import matplotlib.pyplot as plt
import numpy as np


# Streamlitのタイトル
st.title("Folium Map in Streamlit - Hakodate")

# 地図の中心座標とズームレベルを設定
map_center = [41.768793, 140.728810]  # 函館の座標
zoom_level = 10

# Foliumで地図を作成
m = folium.Map(location=map_center, zoom_start=zoom_level)

# Imgurにアップロードした画像のURL
image_url = "https://i.imgur.com/U78yYF5.png"

# ポップアップに表示するHTMLを作成
popup_html = f"""
    <b>Hakodate Station</b><br>
    <i>Location:</i> Hakodate, Hokkaido, Japan<br>
    <i>Opened:</i> 1902<br>
    <i>Operator:</i> JR Hokkaido<br>
    <i>Lines:</i> Hakodate Main Line<br>
    <img src="{image_url}" alt="Hakodate Station" width="200">
"""

# カスタムアイコンを作成
custom_icon = folium.Icon(color='red', icon='info-sign')

# 地図上にマーカーを追加
folium.Marker(
    [41.768793, 140.728810], 
    tooltip='Hakodate Station', 
    popup=folium.Popup(popup_html, max_width=300),
    icon=custom_icon
).add_to(m)

# カラーバーを作成する関数
def create_color_bar():
    # 色の範囲を定義
    colors = ["#ffa07a", "#ff6347", "#ff0000"]
    labels = ["1 - 5", "6 - 10", "11 -"]

    # カラーバーを作成
    fig, ax = plt.subplots(figsize=(0.1, 0.5))  # サイズを小さくする
    cmap = plt.cm.colors.ListedColormap(colors)  # カラーマップをリストから作成
    norm = plt.Normalize(vmin=0, vmax=len(colors))
    cb = plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), cax=ax)
    cb.set_ticks(np.arange(len(colors)) + 0.5)
    cb.set_ticklabels(labels)
    cb.ax.invert_yaxis()
    cb.ax.tick_params(labelsize=5)  # フォントサイズを小さくする

    return fig

# レイアウトを調整
col1, col2 = st.columns([6, 1])  # カラムの比率を調整

with col1:
    folium_static(m)
with col2:
    fig = create_color_bar()
    st.pyplot(fig)

