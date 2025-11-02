import streamlit as st
import requests


st.set_page_config(page_title="mushafWEBAPP",page_icon="📖")
st.title("mushaf app 📖 ")
st.sidebar.title("controls")
st.sidebar.write("select an surah")
response_surah = requests.get("https://api.alquran.cloud/v1/surah")
data= response_surah.json()["data"]

surah_names_list=[f"{s["number"]}.{s["name"]}{s["englishName"]}" for s in data]

surah_name=st.sidebar.selectbox("select a surah ", surah_names_list)


surah_num= int(surah_name.split(".")[0])

st.write(surah_num)


response_surah = requests.get(f"https://api.alquran.cloud/v1/surah/{surah_num}/ar.abdurrahmaansudais")
data= response_surah.json()["data"]["ayahs"]


for ayah in data:
    st.write(f"{ayah["text"]}")
    st.audio(f"{ayah["audio"]}")
