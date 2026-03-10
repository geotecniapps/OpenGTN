# apps/ensayo_triaxial.py
import streamlit as st
import numpy as np
import pandas as pd

def main():
    # Título y descripción de la app
    st.set_page_config(page_title="GTN | TRIAXIAL", page_icon=":material/sort:", layout="centered")
    st.title("GTN | TRIAXIAL TEST")

    st.divider()
    
    st.write("Enter the values of major principal stress (σ₁) and minor principal stress (σ₃) from **three specimens** to calculate the Mohr-Coulomb failure envelope.")
    st.caption("Note: σ₃ is the confining stress and σ₁ is the major stress (σ₃ plus deviator stress).")
    
    st.subheader("📝 Test data")
    st.info("Adjust the parameters and click **CALCULATE** to get the results.")
    
    data = {
        "Specimen" : [1,2,3],
        "σ₃ (kPa)": [],
        "σ₁ (kPa)": []}
    
    for i in range(1, 4):
        col1, col2 = st.columns(2)
    
        with col1:
            sigma3 = col1.number_input(f"Specimen {i} - σ₃ (kPa)", key=f"sigma3_{i}", value=100 + i*50.0)
        with col2:
            sigma1 = col2.number_input(f"Specimen {i} - σ₁ (kPa)", key=f"sigma1_{i}", value=300 + i*100.0)
        data["σ₃ (kPa)"].append(sigma3)
        data["σ₁ (kPa)"].append(sigma1)
        
    submit = st.button("CALCULATE", type="primary")
    
    if submit:
        mensaje = st.empty()
        mensaje.success("Generating diagram! Please wait...")
        df = pd.DataFrame(data)
        
        # Transformar a círculo de Mohr: c/φ mediante regresión lineal del plano de falla
        s3 = np.array(df["σ₃ (kPa)"])
        s1 = np.array(df["σ₁ (kPa)"])
        sigma_mean = (s1 + s3) / 2
        tau_max = (s1 - s3) / 2
    
        # Regresión lineal en el espacio st: tau = c + sigma * tan(φ)
        coeffs = np.polyfit(sigma_mean, tau_max, 1)
        m = coeffs[0] #m=sin(fi)
        b = coeffs[1] #b=c*cos(fi)
        phi_rad = np.arcsin(m)
        phi_deg = np.degrees(phi_rad)
        c = b / np.cos(phi_rad)
    
    
        ##### ----- Resultados
        st.divider()
        st.subheader("📊 Results:")
        col_res1, col_res2 = st.columns(2)
    
        # Los resultados se mostrarán en 2 columnas, en la columna 1 la tabla de datos y en la columna 2 la grafica
        with col_res1:
            # Mostrar tabla
            st.write("📋 Data table:")
            st.dataframe(df, hide_index=True)
    
                # Resultados
            st.write("Mohr-Coulomb envelope parameters:")
            st.success(f"Cohesion c = {c:.2f} kPa")
            st.success(f"Internal friction angle φ = {phi_deg:.2f}°")
    
        with col_res2:
            # Mostar gráfica
            import matplotlib.pyplot as plt
        
            # Para la envolvente de falla
            x0 = 0
            y0 = c
            pendiente = np.tan(phi_rad)
            x_recta = np.linspace(x0, max(sigma_mean) * 1.4, 100)
    
            # Calcular y graficar los círculos de Mohr para cada par (σ₁, σ₃)
            circles = []
            for i in range(3):
                center = (data["σ₁ (kPa)"][i] + data["σ₃ (kPa)"][i]) / 2
                radius = (data["σ₁ (kPa)"][i] - data["σ₃ (kPa)"][i]) / 2
                theta = np.linspace(0, 2 * np.pi, 200)
                x = center + radius * np.cos(theta)
                y = radius * np.sin(theta)
                circles.append((x, y))        
    
            # Graficar los círculos en el mismo gráfico
            fig, ax = plt.subplots()
            for x, y   in circles:
                ax.plot(x, y, label = "Mohr Circle ")
            # ax.plot(sigma_mean, tau_max, 'o', label="Puntos experimentales")
            ax.plot(x_recta, pendiente * (x_recta - x0) + y0, 'r--', label="Failure envelope")
            ax.set_title("Mohr Circles and Mohr-Coulomb Envelope")
            ax.legend()
    
            # Asignar valores mínimo y máximo de los ejes
            ax.set_xlim(0, max(s1) * 1.1)
            ax.set_ylim(0, max(s1) / 1.4)
    
            # Definir nombres de ejes
            ax.set_xlabel("Normal stress")
            ax.set_ylabel("Shear stress")
    
            st.pyplot(fig)
    
            # Actualizar mensaje a "generado"
            mensaje.success("✅ Diagram generated. Please scroll down")
            st.balloons()
    
    st.warning("⚠️ **Disclaimer:** This application is an educational tool and does not replace the evaluation of a qualified geotechnical engineer. Always consult a professional for the final design.")
    st.write("We appreciate user feedback to improve this tool. If you have suggestions or find errors, you can contact us through our social media or email geotecniapps@gmail.com.")
    st.markdown("<center><h5>Made by GeotecniApps.com</h5></center>", unsafe_allow_html=True)