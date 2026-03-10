# apps/capacidad_carga.py
import streamlit as st
import numpy as np

def main():
    st.set_page_config(page_title="GTN | Qa TERZAGHI", page_icon=":material/sort:", layout="centered")
    st.title("GTN | CAP CARGA TERZAGHI")
    st.write("This application allows you to calculate **square**, **rectangular** and **circular** footings under drained conditions (φ > 0), without shape, inclination or depth factors.")
    st.write("Choose the foundation type and adjust the parameters for calculation:")

    tipo_cimentacion = st.selectbox(
        "Select foundation type:",
        ["Square", "Rectangular", "Circular"]
    )

    col1, col2 = st.columns(2)
    with col1:
        st.write("**Foundation geometry**")
        if tipo_cimentacion == "Circular":
            B = st.number_input("Foundation diameter **B** (m)", min_value=0.1, value=1.0, step=0.1)
        elif tipo_cimentacion == "Rectangular":
            B = st.number_input("Foundation width **B** (m)", min_value=0.1, value=1.0, step=0.1)
            L = st.number_input("Foundation length **L** (m)", min_value=0.1, value=1.0, step=0.1)
        else:
            B = st.number_input("Foundation width **B** and length **L** (m)", min_value=0.1, value=1.0, step=0.1)
        Df = st.number_input("Foundation depth **Df** (m)", min_value=0.1, value=1.0, step=0.1)

        st.divider()

        st.write("**Soil data**")
        gamma = st.number_input("Soil unit weight **γ** (kN/m³)", min_value=10.0, value=18.0, step=0.1)
        c = st.number_input("Soil cohesion **c** (kPa)", min_value=0.0, value=0.0, step=1.0)
        phi = st.number_input("Internal friction angle **φ** (°)", min_value=0.0, max_value=45.0, value=30.0, step=1.0)

        st.divider()

        st.write("**Factor of Safety**")
        FS = st.number_input("Factor of Safety **FS**", min_value=1.0, value=3.0, step=0.1)

    with col2:
        st.image("capcarga1.png")

        # Cambiar ecuación según tipo de cimentación
        if tipo_cimentacion == "Square":
            st.latex(r"q_u = 1.3cN_c + qN_q + 0.4\gamma B N_\gamma")
            st.caption("Equation for **square** foundation.")
        elif tipo_cimentacion == "Rectangular":
            st.latex(r"q_u = cN_c + qN_q + \frac{1}{2}\gamma B N_\gamma")
            st.caption("Equation for **rectangular** foundation.")
        else:
            st.latex(r"q_u = 1.3cN_c + qN_q + 0.3\gamma B N_\gamma")
            st.caption("Equation for **circular** foundation.")

        #Mostrar los factores de capacidad de carga (N) de Terzaghi
        st.latex(r"""
        \begin{align*}
            
        N_{q} &=\frac{e^{2\left ( 3\pi /4-\phi /2 \right )tan\left ( \phi  \right )}}{2 cos ^{2} \left ( 45 + \frac{\phi }{2} \right )}\\
                \\
                    
        N_c &= \frac{N_q - 1}{\tan \phi} \\
                \\
                    
        N_{\gamma} &=\frac{1}{2}\left ( \frac{K_{p\gamma }}{cos^{2}(\phi' )}-1 \right )*tan(\phi' )\\
            
        \end{align*}""")
        st.caption("Source: Terzaghi, K. (1943). *Theoretical Soil Mechanics*, Wiley, New York.")

        st.divider()

        st.info("Adjust the parameters and click **CALCULATE** to get the results.")
        submit = st.button("CALCULATE", type="primary")

    # 🔹 Cálculos (al hacer clic en Calcular)
    if submit:
        # Convertir a radianes
        phi_rad = np.radians(phi)

        # Coeficientes de Terzaghi
        Nq = np.exp(2*(3*np.pi/4-phi_rad/2)*np.tan(phi_rad))/(2*np.cos(np.pi/4+phi_rad/2)**2)
        Nc = (Nq - 1) / np.tan(phi_rad) if phi != 0 else 5.7  # Nc ≈ 5.7 para φ = 0
        
        # Diccionario de valores Ny (Nγ) según phi, calculados por De Kumbhojkar 1993 (para zapata cuadrada)
        ny_dict = {
            0: 0.0,
            1: 0.01,
            2: 0.04,
            3: 0.06,
            4: 0.10,
            5: 0.14,
            6: 0.20,
            7: 0.27,
            8: 0.35,
            9: 0.44,
            10: 0.56,
            11: 0.69,
            12: 0.85,
            13: 1.04,
            14: 1.26,
            15: 1.52,
            16: 1.82,
            17: 2.18,
            18: 2.59,
            19: 3.07,
            20: 3.64,
            21: 4.31,
            22: 5.09,
            23: 6.00,
            24: 7.08,
            25: 8.43,
            26: 9.84,
            27: 11.60,
            28: 13.70,
            29: 16.18,
            30: 19.13,
            31: 22.65,
            32: 26.87,
            33: 31.94,
            34: 38.04,
            35: 45.41,
            36: 54.36,
            37: 65.27,
            38: 78.61,
            39: 95.03,
            40: 115.31,
            41: 140.51,
            42: 171.99,
            43: 211.56,
            44: 261.60,
            45: 325.34,
            46: 407.11,
            47: 512.84,
            48: 650.67,
            49: 831.99,
            50: 1072.80
        }

        # Interpolación lineal si phi no está en el diccionario
        phi_keys = sorted(ny_dict.keys())
        if phi in ny_dict:
            Ny = ny_dict[phi]
        else:
            for i in range(len(phi_keys)-1):
                if phi_keys[i] < phi < phi_keys[i+1]:
                    # Interpolación lineal
                    Ny = ny_dict[phi_keys[i]] + (ny_dict[phi_keys[i+1]] - ny_dict[phi_keys[i]]) * (phi - phi_keys[i]) / (phi_keys[i+1] - phi_keys[i])
                    break
                else:
                    Ny = ny_dict[phi_keys[-1]]  # Si phi > max key

        # Cálculo de qu y qadm (FS = 3 por defecto)
        q = gamma * Df

        # 🔹 Factor según tipo de cimentación
        if tipo_cimentacion == "Square":
            factor_formag = 0.4
        elif tipo_cimentacion == "Rectangular":
            factor_formag = 0.5
        else:
            factor_formag = 0.3

        if tipo_cimentacion == "Rectangular":
            factor_formac = 0.0
        else:
            factor_formac = 1.3

        q = gamma * Df
        qu = (factor_formac * c * Nc) + (q * Nq) + (factor_formag * gamma * B * Ny)
        qadm = qu / FS

        # POP-UP DE ÉXITO - Esto aparecerá en medio de la pantalla
        st.success("Calculation completed!", icon="✅")

        # Eso muestra los globos
        st.balloons()
        
        st.subheader("📊 Results:")
        st.write(f"**Foundation type:** {tipo_cimentacion}")
        st.write(f"**Nc =** {Nc:.2f}")
        st.write(f"**Nq =** {Nq:.2f}")
        st.write(f"**Nγ =** {Ny:.2f}")
        st.success(f"Ultimate bearing capacity **qu = {qu:.2f} kPa**")
        st.info(f"Allowable bearing capacity (FS=3) **qadm = {qadm:.2f} kPa**")

        #st.markdown("**Nota:** El uso de esta aplicación es únicamente orientativo. Se recomienda corroborar la información con un especialista en geotecnia.")
        st.markdown("⚠️ **Disclaimer:** This application is an educational tool and does not replace the evaluation of a qualified geotechnical engineer. Always consult a professional for the final design.")
        #st.image("anunciate_aqui.gif", use_container_width=True)
        st.write("We appreciate user feedback to improve this tool. If you have suggestions or find errors, you can contact us through our social media or email geotecniapps@gmail.com.")
        st.markdown("<center><h5>Made by GeotecniApps.com</h5></center>", unsafe_allow_html=True)
        # Mostrar la ecuacion de capacidad de carga de terzagui con los valores insertados





    #titulo y descripción de la app
    st.set_page_config(page_title="GTN | GEOEXPLO GDL", page_icon=":material/sort:", layout="centered")
    
    #st.image("anunciate_aqui.gif", use_container_width=True)
    
    # Ingreso de datos del proyecto
    st.header("📝 Datos del Proyecto")
    nombre_proyecto = st.text_input("Nombre del proyecto")
    ubicacion = st.selectbox("Ubicación", ["Guadalajara", "Zapopan"])
    st.divider()
    
    st.write("El número de sondeos está en función del área de desplante de la construcción.")
    area = st.number_input("Área de construcción (m²)", min_value=1)
    st.divider()
    
    st.write("La profundidad de los sondeos está en función del número de niveles.")
    niveles = st.number_input("Número de niveles", min_value=1, step=1)
    st.info("El número de niveles considera solo los niveles superiores al nivel de calle. No considere sótanos en este dato.")
    nivel_PB = st.number_input("Nivel de planta baja o del nivel inferior del último sótano (en caso de existir), medido desde el nivel del terreno natural (m)", max_value=0)
    BTN_calc = st.button("CALCULAR", type='primary')
    
    # Cálculos simples
    if BTN_calc:
                #Determinar la profundidad de sondeos
           # NumeroDeNiveles = float(input('¿Cual es el NÚMERO DE NIVELES del proyecto? '))
    
        if niveles == 1:
            profundidad = 4
        elif niveles == 2:
            profundidad = 5
        elif niveles == 3:
            profundidad = 7
        elif niveles == 4:
            profundidad = 9
    
        elif niveles == 5:
            profundidad = 9
        elif niveles == 6:
            profundidad = 12
        elif niveles == 7:
            profundidad = 12
        elif niveles == 8:
            profundidad = 14
        elif niveles == 9:
            profundidad = 14
        elif niveles == 10:
            profundidad = 16
        elif niveles > 10 :
            profundidad = ">10"
        else:
            profundidad = 'error'   
    
        #Numero de sondeos
        if 0 < area <= 100:
            num_sondeos = 1
        elif 100 < area <= 250:
            num_sondeos = 2
        elif 250 < area <=1000:
            num_sondeos = 3
        elif area > 1000 :
            num_sondeos = ">4"
        else:
            num_sondeos = 'error'
                    
        #Tipo de sondeo
        tipo_sondeo = "SPT"
        
        # Mostrar resultados
        st.header("🔍 Recomendación Técnica")
        st.write(f"Tipo de sondeo sugerido: {tipo_sondeo}")
        
        st.write(f"Número de sondeos: {num_sondeos}")
        if num_sondeos == ">4":
            st.success("Para áreas de construcción mayores a 1 000 m², el número de sondeos dependerá de la variabilidad del terreno. Será responsabilidad del especialista geotécnico determinar dicho número y de la Dirección General de Obras Públicas aprobarlo.")
        
        st.write(f"Profundidad estimada por sondeo: {profundidad} m")
        st.info("Esta profundidad se mide desde el nivel de planta baja o desde el nivel inferior del último sótano, en caso de existir.")
        if profundidad != ">10":
            st.success(f"La profundidad total del sondeo debe ser de: {profundidad - nivel_PB} m medido desde el nivel de terreno natural.")
    
        if profundidad == ">10":
            st.success("Para proyectos de más de 10 niveles, la profundidad de los sondeos deberá ser tal que el incremento de esfuerzos no supere aproximadamente el 10 % de los esfuerzos efectivos iniciales. Será responsabilidad del especialista geotécnico determinar dichas profundidades, y de la Dirección General de Obras Públicas aprobarlas.")
    
        st.divider()
    
        st.warning("⚠️ **Nota importante:** Si se encuentra roca antes de alcanzar la profundidad mínima requerida, en construcciones de **diez (10) o más niveles** deberá perforarse al menos 3.00 m dentro de la roca para verificar que el manto sea continuo. Si la construcción tiene **menos de diez (10) niveles**, en lugar de perforar en roca se podrán realizar sondeos adicionales para constatar la continuidad del manto rocoso.")
        st.balloons()
    
        #st.header("💰 Si desea una Cotizacion")
        #st.write("📩Contácte a proyectos@geotecniaterranova.com")
        #st.write("✅o por Whatsapp https://wa.link/vai3cy") 
    
    st.warning("⚠️ **Descargo de responsabilidad:** Esta aplicación es una herramienta educativa y no sustituye la evaluación de un ingeniero geotécnico calificado. Consulta siempre a un profesional para el diseño final.")
    st.write("Agradecemos a los usuarios su retroalimentación para mejorar esta herramienta. Si tiene sugerencias o detecta errores, puede contactarnos a través de nuestras redes sociales o al correo electrónico geotecniapps@gmail.com.")
st.markdown("<center><h5>Made by GeotecniApps.com</h5></center>", unsafe_allow_html=True)
