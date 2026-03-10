import streamlit as st
import math

def main():
        #titulo y descripción de la app
        st.title("GTN | CAP CARGA CDMX")
        
        st.markdown("**Design according to NTC CDMX - 2023**")
        
        col1, col2, col3 = st.columns([1,1,1])
        
        with col1:
            st.link_button("Consult regulation", "https://data.consejeria.cdmx.gob.mx/portal_old/uploads/gacetas/b3c4f4ff37241d0a93cc6742a8b0bf2f.pdf", icon=":material/article:")
        with col2:
            st.markdown(" ")
        with col3:
            st.markdown(" ")
        
        st.divider()
        
        st.markdown("For shallow foundations, compliance with the following inequality shall be verified for the different possible combinations of vertical actions.")
        
        st.latex(r"\frac{\sum QFc}{A} < r")
        
        st.info("In Mexico City, the equation to use is different for cohesive or frictional soils, please select the soil type in your project.")
        
        suelo = st.selectbox("**Select soil type**", options=["Cohesive soils", "Frictional soils"], key="tipo_suelo")
        
        if suelo == "Cohesive soils":
            st.write("For cohesive soils")
            st.latex(r"r = c_u N_c F_R + p_v")
        
        elif suelo == "Frictional soils":
            st.write("For frictional soils")
            st.latex(r"r = \left[\bar{p}_v(N_q - 1) + \frac{\gamma B N_\gamma}{2}\right]F_R + p_v")
        else:
            st.error("Select a soil type")
        
        st.divider()
        #Datos de entrada
        st.markdown("**Input data**")
        Fr = st.selectbox("**Fr:**   Resistance reduction factor", options=[0.35, 0.65], index=0, help="a) FR=0.35 for load capacity under any combination of actions at the base of any type of footings in zone I, boundary footings founded at less than 5 m depth in zones II and III, and piles and piers supported on a frictional stratum. b) FR=0.65 for other cases. ")
        
        st.divider()
        
        #Geometía
        st.write("**Foundation geometry**", )
        ni_B = st.number_input("**B:** Foundation width in m (shorter side)", min_value=0.1)
        ni_L = st.number_input("**L:** Foundation length in m ", min_value=ni_B)
        
        ni_df = st.number_input("**Df:** Foundation depth in m ", min_value=0.0)
        
        st.divider()
        
        #PAránetros del suelo
        st.write("**Soil parameters**", )
        ni_y1 = st.number_input("**γ:** Unit weight of soil **ABOVE** foundation level (t/m3) ")
        ni_y2 = st.number_input("**γ:** Unit weight of soil **BELOW** foundation level (t/m3) ")
        
        #'Cohesión del suelo'
        if suelo =="Cohesive soils":
            ni_c = st.number_input("**c:** Apparent cohesion of soil determined by unconsolidated-undrained UU triaxial test (t/m2) ", min_value=0.0)
            ni_fi = 0.0
        elif suelo == "Frictional soils":
            st.info("In FRICTIONAL soils cohesion is assumed as 0 and is not considered for calculation")    
        else:
            st.error("Select a soil type")
        
        #Fi del suelo
        if suelo =="Cohesive soils":
            st.info("In COHESIVE soils the internal friction angle is assumed as 0 and is not considered for calculation")    
        
        elif suelo == "Frictional soils":
            ni_c = 0.0
            ni_fi = st.number_input("**ϕ:** Internal friction angle (°)", min_value=0.0)
        
        else:
            st.error("Select a soil type")    
        
        # REVISAR A PARTIR DE AQUÍ *********************************************************************************************************************************************************************************
        ni_Pv = st.number_input("**pv:**  TOTAL vertical pressure at foundation depth due to soil self-weight (t/m2) ", min_value=0.0) #Puede ser gama por Df o una carga adicional
        
        ni_Pv_ef = st.number_input("**pv':**  EFFECTIVE vertical pressure at foundation depth (t/m2) ", min_value=0.0) #Puede ser gama -1 por Df
        
        if st.checkbox("Is there GWT below the foundation?"):
            ni_NAF = st.number_input("**Z:** GWT depth from foundation level (m)")
            ni_NAF_r = ni_df + ni_NAF
        
            if ni_NAF_r <= ni_df:
                ni_y2_r = ni_y2 - 1.0
            elif ni_NAF < ni_B:
                ni_y2_r = (ni_y2 - 1.0) + (ni_NAF /ni_B)*(ni_y2-(ni_y2 - 1.0)) 
            else:
                ni_y2_r = ni_y2
        
        if st.checkbox("Is there moment or eccentricity on the short side?"):
            e_b = st.number_input("**e:** Load eccentricity with respect to short side (m)", min_value=(ni_B/3)) #La excentricidad no puede ser mayor a B/3, en caso de ser así se debe de replantear la cimentación o usar contratrabe. 
            ni_B = ni_B - 2 *e_b
        
        # REVISAR HASTA AQUÍ *********************************************************************************************************************************************************************************
        
        calcular = st.button("Calculate",type="primary")
        
        st.divider()
        
        # RESULTADOS
        if calcular:
            st.success("Results have been calculated:")
            #Calcular Nc, Nq y Ngamma de Vesic sin corregir
            phi_rad = math.radians(ni_fi)
        
            Nq = math.exp(math.pi*math.tan(phi_rad) )* math.tan(math.radians(45 + ni_fi/2))**2
        
            Ny = 2 * (Nq + 1) * math.tan(phi_rad)
           
            #Calcular Nc, Nq y Ngamma de Vesic Corregidos
            FC_q = 1 +(ni_B/ni_L) * math.tan(phi_rad)
        
            Nq_cor = Nq * FC_q
        
            FC_y = 1 - 0.4 * (ni_B/ni_L)
            Ny_cor = Ny * FC_y
        
            if ni_df/ni_B > 2:
                Df_B = 2
            else:
                Df_B = ni_df/ni_B
        
            Nc = 5.14 * (1 + 0.25 * Df_B + 0.25 * ni_B/ni_L)
        
            #lo que aparece en la app
            st.write("**The corrected dimensionless factors are as follows:**")
        
            if suelo == "Cohesive soils":
                st.latex(r"N_c = 5.14 \left(1 + 0.25 \frac{D_f}{B} + 0.25 \frac{B}{L}\right)")
                st.write(f"Nc = {Nc:.2f}")
                Nq_cor = 0.0
                Ny_cor = 0.0
        
            elif suelo == "Frictional soils":
                Nc = 0.0
        
                st.latex(r"N_q = e^{\pi \tan\phi} \tan^2\left(45^\circ + \frac{\phi}{2}\right)")
                st.write(f"Nq = {Nq_cor:.2f}")
        
                st.latex(r"N_\gamma = 2(N_q + 1)\tan\phi")
                st.write(f"Ny= {Ny_cor:.2f}")
            else:
                st.error("Select a soil type")
        
            st.divider()
        
            #Calcular la r
            
            if suelo == "Cohesive soils":
                qa = (ni_c*Nc)*Fr + ni_Pv
        
            elif suelo == "Frictional soils":
                qa = (ni_Pv_ef*(Nq_cor-1.0)+1/2*ni_y2_r*ni_B*Ny_cor)*Fr + ni_Pv
            else:
                st.error("Select a soil type")
        
            st.write("**The reduced load capacity (i.e., affected by the corresponding resistance factor) of the foundation is:**")
        
            if suelo == "Cohesive soils":
                st.write("For cohesive soils")
                st.latex(r"r = c_u N_c F_R + p_v")
        
            elif suelo == "Frictional soils":
                st.write("For frictional soils")
                st.latex(r"r = \left[\bar{p}_v(N_q - 1) + \frac{\gamma B N_\gamma}{2}\right]F_R + p_v")
            else:
                st.error("Select a soil type")
           
            st.write(f"r = {qa:.2f} t/m2")
            st.divider()
        
            #Calcular la Qadm
            st.write("**The TOTAL reduced load capacity of the element is:**")
        
            Qa = qa * ni_B * ni_L
            Area = ni_B * ni_L
        
            st.latex(r"A = B \cdot L")
            st.write(f"A = {Area:.2f} m2")
            st.latex(r"R = r \cdot A")
            st.success(f"R = {Qa:.2f} t")
            st.balloons()
            st.divider()
        
        st.info('Additionally, the possibility of "soft stratum effect" or "extrusion failure" should be reviewed')
        
        st.write("If you need to review the theory we recommend the following video: [YouTube Video](https://www.youtube.com/watch?v=3aZSLJGrLSQ)")
        
        #st.video("https://www.youtube.com/watch?v=zOlavmyf2Gc")
        
        st.warning("⚠️ **Disclaimer:** This application is an educational tool and does not replace the evaluation of a qualified geotechnical engineer. Always consult a professional for the final design.")
        
        st.write("We appreciate user feedback to improve this tool. If you have suggestions or find errors, please contact us through our social media or email geotecniapps@gmail.com")
        st.markdown("<center><h5>Made by GeotecniApps.com</h5></center>", unsafe_allow_html=True)