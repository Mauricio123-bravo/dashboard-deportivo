import streamlit as st
import pandas as pd


st.set_page_config(page_title="Dasboard Deportivo", layout="centered")


st.title("Panel de Rendimiento: Equipo Datos e IA santoto Tunja")
st.write("Estadisticas clave de los jugadores en el semestre actual")

datos = {
    "Jugador" : ["sebastian", "manuel", "cristian", "gabriela"],
    "Goles" : [18,14,20,1],
    "Asistencias" : [5,7,10,3]
}

df = pd.DataFrame(datos)

col1,col2,col3,col4 = st.columns(4)

col1.metric("Goles totales", df["Goles"].sum(), delta="+3 vs partido anterior")
col2.metric("Asistencias totales", df["Asistencias"].sum())
col3.metric("Goleador del equipo", df.loc[df["Goles"].idxmax(), "Jugador"])
col4.metric("Posicion de liga del Equipo", value="3er Lugar", delta="-1 puesto")



st.subheader("Estadiísticas al detalle")
st.dataframe(df)


st.subheader("Comparativa de Rendiemiento")
st.bar_chart(df.set_index("Jugador"))