import streamlit as st
import folium
from streamlit_folium import folium_static

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

# Streamlit上に地図を表示
folium_static(m)
