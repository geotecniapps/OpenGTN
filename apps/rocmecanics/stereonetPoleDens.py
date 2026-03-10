import streamlit as st
import mplstereonet

def main():
    #-------------------------------
    # Streamlit app for stereonets pole density
    #-------------------------------
    
    st.set_page_config(page_title="GTN | PD STEREOGRAM", page_icon=":material/landslide:", layout="centered")
    st.title("GTN | STEREONET POLE DENSITY")
    st.markdown("This application allows you to create a pole density stereogram based on the strike and dip of planes you want to analyze. You can enter the data for each plane and generate the stereogram with a single click.")
    st.markdown("The library utilized for the stereonet is [mplstereonet](https://mplstereonet.readthedocs.io/en/latest/), which is a powerful tool for plotting stereonets in Python.")
    # Banner de publicidad
    st.divider()
    
    # User selects the number of planes
    number_of_planes = st.number_input(
        "How many planes do you want to analyze?",
        min_value=1, max_value=50, value=1, step=1,
        help="The maximum number of planes is 50"
    )
    
    planes = []  # Lista para almacenar los datos de los planos
    
    #----User inputs strike and dip for each plane
    st.info("Enter the strike in *azimuthal* form (from 0° to 360°) and dip (from 0° to 90°) for each plane using the *right-hand rule*.")
    st.divider()
    
    for i in range(number_of_planes):
        st.write(f'Plane {i+1}')
        col1, col2 = st.columns(2)
    
        with col1:
            strike = st.slider(f'Strike {i+1} (°)', 0, 360, 45)
    
        with col2:
            dip = st.slider(f'Dip {i+1} (°)', 0, 90, 45)
    
        planes.append((strike, dip))
        st.divider()
    
    # Botón para generar el estereograma
    BTN_generator = st.button("Generate stereogram", type='primary')
    
    #----Crea el estereograma
    if BTN_generator:
        # Placeholder para el mensaje de estado
        mensaje = st.empty()
        mensaje.success("Generating stereogram! Please wait...")
    
        # Subtítulo del gráfico
        st.subheader("Pole Density Stereogram")
    
        # Crear figura y ejes del estereograma
        fig2, ax2 = mplstereonet.subplots()
    
        strikes, dips = zip(*planes)  # Toma los strikes y dips de la lista de planos
    
        # Generar densidad de polos
        cax = ax2.density_contourf(strikes, dips, measurement='poles', method="exponential_kamb")
        ax2.pole(strikes, dips)
        ax2.grid(True)
        ax2.set_azimuth_ticks(range(0, 360, 15))  # cada 15°
    
        # Mostrar figura en Streamlit
        st.pyplot(fig2)
    
        # Actualizar mensaje a "generado"
        mensaje.success("✅ Stereogram generated. Please scroll down")
        st.balloons()
    
    # Mensajes finales
    st.warning("⚠️ **Disclaimer:** This application is an educational tool and does not replace the evaluation of a qualified geotechnical engineer. Always consult a professional for the final design.")
    st.write("We appreciate user feedback to improve this tool. If you have suggestions or find errors, you can contact us through our social media or email geotecniapps@gmail.com.")
    st.markdown("<center><h5>Made by GeotecniApps.com</h5></center>", unsafe_allow_html=True)