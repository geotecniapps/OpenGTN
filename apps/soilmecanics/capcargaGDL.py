import streamlit as st
import math


def main():
    # Título y descripción de la app
    st.set_page_config(page_title="GTN | GEOEXPLO GDL", page_icon=":material/sort:", layout="centered")
    
    st.title("**Design based on 1997 GDL Regulations**")
    st.link_button("Consult regulation", "https://www.smie.org.mx/uploads/1/2023-03/jalisco_reglamento_construccion_municipal_guadalajara.pdf",icon=":material/article:")
    st.divider()
    
    st.markdown("**Input data**")
    ni_fs = st.number_input("**FS:** Safety factor (minimum 2.5)",min_value=2.5 )
    
    st.divider()
    
    # Geometría
    st.write("**Foundation geometry**", )
    ni_B = st.number_input("**B:** Foundation width (m) ", min_value=0.1)
    ni_L = st.number_input("**L:** Foundation length (m) ", min_value=0.1)
    
    ni_df = st.number_input("**Df:** Foundation depth (m) ", min_value=0.0)
    
    st.divider()
    
    # Parámetros del suelo
    st.write("**Soil parameters**", )
    ni_y1 = st.number_input("**γ₁:** Unit weight of soil *above* foundation level (t/m³)", min_value=0.1)
    ni_y2 = st.number_input("**γ₂:** Unit weight of soil *below* foundation level (t/m³)", min_value=0.1)
    ni_c = st.number_input("**c:** Cohesion (t/m²)", min_value=0.0)
    ni_fi = st.number_input("**ϕ:** Internal friction angle (°)", min_value=0.0)
    
    if st.checkbox("Is there groundwater level (GWT) below the foundation?"):
        ni_NAF = st.number_input("**Z:** GWT depth from foundation level (m)", min_value=0.0)
    
        if ni_B > ni_NAF:
            ni_y2 = (ni_y2 - 1.0) + (ni_NAF /ni_B)*(ni_y2-(ni_y2 - 1.0)) 
        else:
            ni_y2 = ni_y2
    
    if st.checkbox("Is there moment or eccentricity on the short side?"):
        e_b = st.number_input("**e:** Load eccentricity with respect to short side (m)", min_value=0.0)
    
        ni_B = ni_B - 2 *e_b
    
    
    calcular = st.button("Calculate",type="primary")
    
    
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
    
        st.write("**The corrected factors are as follows:**")
    
        st.write(f"N_c = {Nc:.2f}")
        st.write(f"N_q = {Nq_cor:.2f}")
        st.write(f"N_γ= {Ny_cor:.2f}")
    
        st.divider()
    
        #Calcular la qadm
        
        qa = (ni_y1*ni_df*(Nq_cor-1)+1/2*ni_y2*ni_B*Ny_cor+ni_c*Nc)/ni_fs
    
        st.write("**The allowable bearing capacity is:**")
    
        st.latex(r"q_a = \frac{ \gamma_1 D_f (N_q - 1) + \frac{1}{2} \gamma_2 B N_\gamma + c N_c }{ F_s }")
    
        st.write(f"qₐ = {qa:.2f} t/m²")
        st.divider()
    
        #Calcular la Qadm
        st.write("**The total allowable bearing capacity of the element is:**")
        Qa = qa * ni_B * ni_L
        Area = ni_B * ni_L
    
        st.latex(r"A = B \cdot L")
        st.write(f"A = {Area:.2f} m²")
        st.latex(r"Q_a = q_a \cdot A")
        st.success(f"Qₐ = {Qa:.2f} t")
        st.divider()
    
    #st.markdown("**Nota:** El uso de esta aplicación es únicamente orientativo. Se recomienda corroborar la información con un especialista en geotecnia.")
    st.write("If you need to review the theory, we recommend the following video: [YouTube Video](https://www.youtube.com/watch?v=zOlavmyf2Gc)")
  
    st.markdown("⚠️ **Disclaimer:** This application is an educational tool and does not replace the evaluation of a qualified geotechnical engineer. Always consult a professional for the final design.")
    st.write("We appreciate user feedback to improve this tool. If you have suggestions or find errors, you can contact us through our social media or email geotecniapps@gmail.com.")
    st.markdown("<center><h5>Made by GeotecniApps.com</h5></center>", unsafe_allow_html=True)