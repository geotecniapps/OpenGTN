import streamlit as st
import math

def main():
    #APP de cálculo de Capacidad de carga para cimentaiciones superficiales de acuerdo con las NTC de Perú
    
    # Título y descripción de la app
    st.set_page_config(page_title="GTN | CAP CARGA 🇵🇪", page_icon=":material/sort:", layout="centered")
    st.title("GTN | CAP CARGA PERU 🇵🇪")
    st.write("**TECHNICAL STANDARD E.050 SOILS AND FOUNDATIONS OF THE NATIONAL BUILDING REGULATIONS**")
    
    col1, col2, col3 = st.columns([1,1,1])
    
    with col1:
        st.link_button("Consult regulation", "https://cdn.www.gob.pe/uploads/document/file/2366655/54%20E.050%20SUELOS%20Y%20CIMENTACIONES%20RM%20N%C2%B0%20406-2018-VIVIENDA.pdf?v=1677250657", icon=":material/article:")
    with col2:
        st.markdown(" ")
    with col3:
        st.markdown(" ")
    
    st.markdown("The load capacity (qd) is the ultimate pressure or shear failure pressure of the soil. Consult the standard for more information.")
    
    st.divider()
    
    #------------INPUTS----------------
    st.subheader("📝 Input parameters")
    st.write("Enter soil and foundation parameters")
    # Inputs para los parámetros
    c = st.number_input("Enter soil cohesion (c) in kPa", min_value=0.0, value=25.0)
    phi = st.number_input("Enter soil internal friction angle (φ) in degrees", min_value=0.0, value=0.0)
    gamma1 = st.number_input("Enter unit weight of soil above foundation level (γ1) in kN/m³", min_value=0.0, value=15.0)
    gamma2 = st.number_input("Enter unit weight of soil below foundation level (γ2) in kN/m³", min_value=0.0, value=15.0)
    B = st.number_input("Enter foundation width (B) in m", min_value=0.0, value=1.0)
    L = st.number_input("Enter foundation length (L) in m", min_value=0.0, value=1.0, help="Length must be greater than or equal to width")
    Df = st.number_input("Enter foundation depth (Df) in m", min_value=0.0, value=1.5)
    alpha = st.number_input("Load angle with respect to vertical α° in degrees", min_value=0.0, max_value=90.0, value=0.0, help="If the load is vertical, enter 0°")
    
    #Seleccionar si el suelo es cohesivo o friccionante
    
    st.info("The standard considers a different equation for cohesive or frictional soils, please select the soil type you want to evaluate")
    
    SB_tiposuelo = st.selectbox("Select soil type", ("Cohesive Soils", "Frictional Soils"))
    
    st.divider()
    
    exentricidad = st.toggle("The foundation is eccentrically loaded", value=False)
    
    if exentricidad:
        #poner boton a imagen guia
        
        Q = st.number_input("Enter applied vertical load Q in kN", min_value=0.0, value=100.0)
    
        M1 = st.number_input("Enter moment with respect to long side M1 in kN·m", min_value=0.0, value=0.0)
    
        M2 = st.number_input("Enter moment with respect to short side M2 in kN·m", min_value=0.0, value=0.0)
    
        #Cálculo de L' y B'
    
        st.write("The effective dimensions are as follows: ")
        st.latex(r"""B' = B - \frac{M_2}{Q} """)
        B = B - M2/Q
        st.write(f"The value of effective width B' is: {B:.2f} m")
    
        st.latex(r""" L' = L - \frac{M_1}{Q}""")
        L = L - M1/Q
        st.write(f"The value of effective length L' is: {L:.2f} m")
    
    calcular = st.button("CALCULATE", type="primary")
    
    st.divider()
    
    #-------CALCULOS-----
    #mostrar figura de la zapata
    
    if calcular:
        st.success("✅ The following results have been calculated:")
    
        st.subheader("📊 Results:")
    
        if SB_tiposuelo == "Cohesive Soils":
            st.subheader("Load Capacity Calculation for Cohesive Soils")
            st.write("20.2. In cohesive soils (clay, silty clay and clayey silt), an internal friction angle (φ) equal to zero is used.")
            st.write("For cohesive soils, the load capacity (qd) is calculated using the following equation:")
            st.latex(r"""q_d = s_c i_c c N_c """)
    
            with st.expander("View detailed calculation results"):
                st.write("Where:")
                st.write("- c = cohesion of soil below the footing.")
                st.write("- ic = correction coefficient for load inclination corresponding to cohesion")
                st.write("- sc = correction coefficient for foundation shape corresponding to cohesion")
                st.write("- Nc = load capacity coefficient corresponding to cohesion = 5.14")
    
                #Cáulculo de ic y sc
                st.markdown("The correction coefficients ic and sc are determined according to the following equations:")
                st.latex(r"""
                i_{c} = i_{q} = \left(1 - \frac{\alpha^{\circ}}{90^{\circ}}\right)^{2}
                """)
    
                st.write("Where:")
                st.write("- α° = angle in degrees between load and vertical")
    
                st.write("Substituting in the ic formula:")
            
                ic = (1 - alpha/90)**2
    
                st.success(f"The value of correction coefficient ic is: {ic:.2f}")
    
                st.latex(r"""
                S_{c}  = 1 + 0.2 \frac{B}{L}
                """)
    
                sc = 1 + 0.2 * (B/L)
    
                st.success(f"The value of correction coefficient Sc is: {sc:.2f}")
    
    
                phi_rad = math.radians(phi)  # Convertir grados a radianes si es necesario
    
    
                #Calcular Nc
                Nq = math.exp(math.pi*math.tan(phi_rad) )* math.tan(math.radians(45 + phi/2))**2
    
                # st.latex(r"N_q = e^{\pi \tan\phi} \tan^2\left(45^\circ + \frac{\phi}{2}\right)")
    
                # st.write(f"Nq = {Nq:.2f}")
    
                Nc = 5.14
    
                st.latex(r"N_c = 5.14")
    
                st.success(f"The value of Nc = {Nc:.2f}")
    
                qd = sc * ic * c * Nc
    
                st.latex(r"""q_d = s_c i_c c N_c """)
    
                st.success(f"The ultimate load capacity qd is: {qd:.2f} kPa")
    
            st.success(f"The ultimate load capacity qd is: {qd:.2f} kPa")
    
        if SB_tiposuelo == "Frictional Soils":
                st.subheader("Load Capacity Calculation for Frictional Soils")
                st.write("20.3. In frictional soils (gravels, sands and sandy-gravels), a cohesion (c) equal to zero is used.")
                st.write("For frictional soils, the load capacity (qd) is calculated using the following equation:")
                st.latex(r"""
                q_d = i_q \, \gamma_1 \, D_f \, N_q + 0.5 \, s_\gamma \, i_\gamma \, \gamma_2 \, B' \, N_\gamma
                """)
                
                with st.expander("View detailed calculation results"):
                    st.write("Where:")
                    st.write("- iq = correction coefficient for load inclination corresponding to surcharge (γDf)")
    
                    st.write("- sγ = correction coefficient for foundation shape corresponding to friction")
                    st.write("- iγ = correction coefficient for load inclination corresponding to friction")
                    st.write("- γ1 = unit weight of soil above foundation level.")
                    st.write("- γ2 = effective unit weight of soil below foundation level.")
                    st.write("- Nc = load capacity coefficient corresponding to cohesion")
                    st.write("- Nq = load capacity coefficient corresponding to surcharge (γDf)")
                    st.write("- Nγ = load capacity coefficient corresponding to friction")
                    st.write("- B' = width of the 'effective area'")
                    st.write("- α° = angle in degrees between load and vertical")
    
                    #Cáulculo de iq, iγ y sγ
                    st.markdown("The correction coefficients iq, iγ and sγ are determined according to the following equations:")
    
                    #iq
                    st.latex(r"""
                    i_{q} = \left(1 - \frac{\alpha^{\circ}}{90^{\circ}}\right)^{2}
                    """)
    
                    st.write("Where:")
                    st.write("- α° = angle in degrees between load and vertical")
    
                    st.write("Substituting in the iq formula:")
                
                    iq = (1 - alpha/90)**2
    
                    st.success(f"The value of correction coefficient iq is: {iq:.2f}")
    
                    #iγ
                    st.latex(r"""
                    i_{\gamma}  = \left(1 - \frac{\alpha^{\circ}}{\phi^{\circ}}\right)^{2}
                    """)
    
                    igamma = (1 - alpha/90)**2
    
                    st.success(f"The value of correction coefficient iγ is: {igamma:.2f}")
    
                    #sγ
                    st.latex(r"""
                    S_{\gamma}  = 1 - 0.2 \frac{B}{L}
                    """)
    
                    sgamma = 1 - 0.2 * (B/L)
    
                    st.success(f"The value of correction coefficient Sγ is: {sgamma:.2f}")
    
    
                    phi_rad = math.radians(phi)  # Convertir grados a radianes si es necesario
    
    
                    #Calcular Nq y Ngamma
                    Nq = math.exp(math.pi*math.tan(phi_rad) )* math.tan(math.radians(45 + phi/2))**2
    
                    st.latex(r"N_q = e^{\pi \tan\phi} \tan^2\left(45^\circ + \frac{\phi}{2}\right)")
    
                    st.write(f"Nq = {Nq:.2f}")
    
                    # Nγ
    
                    Ngamma = (Nq - 1) * math.tan(1.4*phi_rad)
    
                    st.latex(r"N_{\gamma} = (N_{q} - 1) \tan(1.4 \phi')")
    
                    st.success(f"The value of Nγ = {Ngamma:.2f}")
    
                    qd = iq * gamma1 * Df * Nq + 0.5 * sgamma * igamma * gamma2 * B * Ngamma
    
                    st.latex(r"""q_d = i_q \, \gamma_1 \, D_f \, N_q + 0.5 \, s_\gamma \, i_\gamma \, \gamma_2 \, B' \, N_\gamma""")
    
                    st.success(f"The ultimate load capacity qd is: {qd:.2f} kPa")
    
                st.success(f"The ultimate load capacity qd is: {qd:.2f} kPa")
                st.balloons()
        
        #La capacidad de carga total
        st.write("The ultimate load capacity of the element Qd is calculated as:")
        Qd = qd * B * L
        st.latex(r"Q_d = q_d \cdot B' \cdot L'")
        st.write(f"The total load capacity Qd is: {Qd:.2f}")
    
        st.divider()
                
        #La capacidad de carga admisible
        st.subheader("Allowable load capacity")
        st.write("The minimum safety factors by regulation are as follows:")
        st.write("For static loads: 3.0")
        st.write("For maximum earthquake or wind loading (whichever is more unfavorable): 2.5")
    
        st.success(f"The total allowable load capacity of the element for STATIC loads Qadm is: {Qd/3:.2f} kN")
    
        st.success(f"The total allowable load capacity of the element for maximum EARTHQUAKE or WIND loading Qadm_smax is: {Qd/2.5:.2f} kN")
    
    st.divider()
    
    st.warning("⚠️ **Disclaimer:** This application is an educational tool and does not replace the evaluation of a qualified geotechnical engineer. Always consult a professional for the final design.")
    st.write("We appreciate user feedback to improve this tool. If you have suggestions or find errors, you can contact us through our social media or email geotecniapps@gmail.com.")
    st.markdown("<center><h5>Made by GeotecniApps.com</h5></center>", unsafe_allow_html=True)