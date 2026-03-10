import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def main():


    st.set_page_config(page_title="GTN | EARTH PRESSURE RANKINE", page_icon=":material/sort:", layout="centered")
    st.title("GTN | EARTH PRESSURE RANKINE")


    #st.markdown("<center><h2>🧱 Presiones de Tierras - Rankine</h2></center>", unsafe_allow_html=True)

    st.write("Calcula las presiones de tierras de Rankine para suelos, muro vertical con relleno horizontal.")

    st.info("Ajusta los parámetros y el cálculo se realizará de forma automática.")

    #with st.form("rankine_form"):
    col1, col2 = st.columns([1,2])

    with col1:
        st.subheader("📊 Datos:")
        H = st.slider("Altura del muro H (m)", min_value=0.1, max_value=10.0, value=3.0, step=0.1)
        gamma = st.slider("Peso volumétrico del suelo γ (kN/m³)", min_value=10.0, max_value=25.0, value=18.0, step=0.1)
        phi = st.slider("Ángulo de fricción interna φ (°)", min_value=0.0, max_value=45.0, value=30.0, step=1.0)
        c = st.slider("Cohesión del suelo c (kPa)", min_value=0.0, max_value=100.0, value=0.0, step=1.0)


        #   submit = st.form_submit_button("CALCULAR", type="primary")

        #if submit:
        phi_rad = np.radians(phi)

        # Coeficientes de Rankine
        Ka = np.tan(np.radians(45 - phi / 2)) ** 2
        K0 = 1 - np.sin(phi_rad)
        Kp = np.tan(np.radians(45 + phi / 2)) ** 2

        # Presiones en la corona del muro
        pac = Ka * gamma * 0 - 2 * c * np.sqrt(Ka)
        p0c = K0 * gamma * 0
        ppc = Kp * gamma * 0 + 2 * c * np.sqrt(Kp)

        # Presiones en la base del muro
        pa = Ka * gamma * H - 2 * c * np.sqrt(Ka)
        p0 = K0 * gamma * H
        pp = Kp * gamma * H + 2 * c * np.sqrt(Kp)

        # Fuerza total (triángulo): P = 0.5 * Ka * γ * H²
        Pa = 1 / 2 * (pa + pac) * H
        P0 = 1 / 2 * (p0 + p0c) * H
        Pp = 1 / 2 * (pp + ppc) * H

        # Ubicacion de la resultante desede la base del muro 
        Za = (H * (pa + 2* pac)) / (3 * (pa +pac))
        Z0 = (H * (p0 + 2* p0c)) / (3 * (p0 +p0c))
        Zp = (H * (pp + 2* ppc)) / (3 * (pp +ppc))


    with st.expander("Ver Cálculos"):
        st.subheader("💻 Cálculos:")
        st.markdown("**Coeficientes de Rankine:**")
        st.write(f"Coeficiente activo (Ka): **{Ka:.3f}**")
        st.write(f"Coeficiente en reposo (K0): **{K0:.3f}**")
        st.write(f"Coeficiente pasivo (Kp): **{Kp:.3f}**")

        st.divider()
        st.markdown("**Presiones resultantes en la corona:**")
        st.write(f"Esfuerzo activo: **{pac:.2f} kPa**")
        st.write(f"Esfuerzo en reposo: **{p0c:.2f} kPa**")
        st.write(f"Esfuerzo pasivo: **{ppc:.2f} kPa**")

        st.divider()
        st.markdown("**Presiones resultantes en la base:**")
        st.write(f"Esfuerzo activo: **{pa:.2f} kPa**")
        st.write(f"Esfuerzo en reposo: **{p0:.2f} kPa**")
        st.write(f"Esfuerzo pasivo: **{pp:.2f} kPa**")

        st.divider()
        st.markdown("**Fuerzas resultantes por metro:**")
        st.write(f"Fuerza activa total (Pa): **{Pa:.2f} kN/m**")
        st.write(f"Fuerza en reposo total (P0): **{P0:.2f} kN/m**")
        st.write(f"Fuerza pasiva total (Pp): **{Pp:.2f} kN/m**")

        st.divider()
        st.markdown("**Ubicación de las fuerzas resultantes desde la base del muro:**")
        if Za < 0:
            st.write(f"Fuerza activa (Za): **<0 m**")
        if Za >= 0:
            st.write(f"Fuerza activa (Za): **{Za:.2f} m**")
        
        st.write(f"Fuerza en reposo (Z0): **{Z0:.2f} m**")
        st.write(f"Fuerza pasiva (Zp): **{Zp:.2f} m**")



    with col2:
        # Gráfico
        st.subheader("📈 Gráfico:")
        z = np.linspace(0, H, 100)
        sigma_a = Ka * gamma * z - 2 * c * np.sqrt(Ka)
        sigma_h0 = K0 * gamma * z
        sigma_p = Kp * gamma * z + 2 * c * np.sqrt(Kp)

        fig, ax = plt.subplots()
        ax.plot(sigma_a, z, label="Presión Activa", color='red')
        ax.plot(sigma_h0, z, label="Presión en Reposo", color='green')
        ax.plot(sigma_p, z, label="Presión Pasiva", color='blue')
        ax.set_xlabel("Presión (kPa)")
        ax.set_ylabel("Altura del muro (m)")
        ax.invert_yaxis()
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

    st.markdown("⚠️ **Descarga de responsabilidad:** Esta aplicación es una herramienta educativa y no sustituye la evaluación de un ingeniero geotécnico calificado. Consulta siempre a un profesional para el diseño final.")
    st.write("Agradecemos a los usuarios su retroalimentación para mejorar esta herramienta. Si tiene sugerencias o detecta errores, puede contactarnos a través de nuestras redes sociales o al correo electrónico geotecniapps@gmail.com.")
    st.markdown("<center><h5>Made by GeotecniApps.com</h5></center>", unsafe_allow_html=True)