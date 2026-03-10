import streamlit as st
import numpy as np

def main():
    #titulo y descripción de la app
    st.set_page_config(page_title="GTN | SETTLEMENT CRC", page_icon=":material/sort:", layout="centered")
    st.title("GTN | ELASTIC SETTLEMENT")
        
    st.divider()
    
    col1, col2 = st.columns(2)
    
    #Funcion de Boussinesq rect al centro, esta z es desde la Df
    def bou_rect_c (q, L, B, z):
        m1 = L/B
        b = B/2
        n1 = z/b
    
        I4 = 2 / np.pi * ((m1*n1)/np.sqrt(1+m1**2+n1**2)*(1+m1**2+2*n1**2)/((1+n1**2)*(m1**2+n1**2))+np.asin(m1/(np.sqrt(m1**2+n1**2)*np.sqrt(1+n1**2))))
    
        Dsz = q * I4
    
        if Dsz < 0 : #Supone que el incremento de esfuerzos es representativo hasta la profundidad que llega el 10% de q y tambien evita errores si Dsz es negativo
            return 0
        else:
            return Dsz
    
    #Incremento de esfuerzos a diferentes profundidades
    def calculo_matrices(q, L, B, E):
        Matriz_z = [] #Profunididad
        Matriz_E = [] #modulo de young a la prof de calculo
        Matriz_Dsz = [] #Incremento de esfuerzos a la profundidad de calculo
        Matriz_Elastic_Settle = [] #Matriz de asentamientos en el suelo
        
        Delta_z = 0.1 #Valor para subdividir el medio
        prof_max = 8*B
    
        #Va a calcular los valores de cada valor de las matrices hasta llegar a la profundidad maxima
        z_actual = Delta_z
        s_acumulado = 0.0
        while z_actual < prof_max:
            Matriz_z.append(z_actual)
            
            E_actual = E #En el futuro este valor se puede hacer variar por estrato
            Matriz_E.append(E_actual)
    
            Dsz_actual = bou_rect_c(q, L, B, z_actual)
            Matriz_Dsz.append(Dsz_actual)
    
            Elastic_Settle_actual = (1 / E_actual) * Dsz_actual * Delta_z 
    
            s_acumulado= s_acumulado + Elastic_Settle_actual
    
            z_actual += np.round(Delta_z,2)
    
        return Matriz_z, Matriz_Dsz, Matriz_Elastic_Settle, s_acumulado
    
    with col1:
        st.header("Input data")
    
        B = st.number_input("Foundation width (B) [m]", min_value=0.01, value=2.0, step=0.01)
        L = st.number_input("Foundation length (L) [m]", min_value=0.01, value=4.0, step=0.01)
        q = st.number_input("Contact pressure (q) [kPa]", min_value=0.0, value=100.0, step=0.1)
        Es = st.number_input("Soil elasticity modulus (Es) [kPa]", min_value=1.0, value=15000.0, step=100.0)
    
        # z = st.slider("Profundidad z", min_value=0.1, max_value= 6*B, step=0.1)
        st.info("Adjust the parameters and click **CALCULATE** to get the results.")
    
    
            
    with col2:
        st.header("Results")
    
        if st.button("CALCULATE", type="primary"):
            
            # Ds_cal = bou_rect_c(q, L, B, z)
    
            # st.write(f"Incremento de esfuerzos Δσz: {Ds_cal:.2f} kPa")
            
            #Con matrices
            Matriz_zcal, Matriz_Dsz, Matriz_Elastic_Settle, Asent_acum = calculo_matrices(q, L, B, Es)
    
            Asent_acum_cm = Asent_acum * 100
    
            import matplotlib.pyplot as plt
    
            fig, ax = plt.subplots()
            ax.plot(Matriz_Dsz, Matriz_zcal)
            ax.set_xlabel("Stress increment Δσz [kPa]")
            ax.set_ylabel("Depth [m]")
            ax.set_title("Vertical Stress Increment Distribution vs Depth")
            ax.invert_yaxis()
            st.pyplot(fig)
    
            st.success(f"Total Settlement = {Asent_acum_cm:.2f} [cm]")
            st.balloons()
    
    st.warning("⚠️ **Disclaimer:** This application is an educational tool and does not replace the evaluation of a qualified geotechnical engineer. Always consult a professional for the final design.")
    st.write("We appreciate user feedback to improve this tool. If you have suggestions or find errors, you can contact us through our social media or email geotecniapps@gmail.com.")
    st.markdown("<center><h5>Made by GeotecniApps.com</h5></center>", unsafe_allow_html=True)