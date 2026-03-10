import streamlit as st

def main():
    #titulo y descripción de la app
    st.title("GTN | GEOEXPLO GDL")
    
    # Ingreso de datos del proyecto
    st.header("📝 Project Data")
    nombre_proyecto = st.text_input("Project name")
    ubicacion = st.selectbox("Location", ["Guadalajara", "Zapopan"])
    st.divider()
    
    st.write("The number of boreholes depends on the construction footprint area.")
    area = st.number_input("Construction area (m²)", min_value=1)
    st.divider()
    
    st.write("The depth of boreholes depends on the number of levels.")
    niveles = st.number_input("Number of levels", min_value=1, step=1)
    st.info("The number of levels only considers levels above street level. Do not include basements in this data.")
    nivel_PB = st.number_input("Ground floor level or lower level of the last basement (if any), measured from natural ground level (m)", max_value=0)
    BTN_calc = st.button("CALCULATE", type='primary')
    
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
        st.header("🔍 Technical Recommendation")
        st.write(f"Suggested borehole type: {tipo_sondeo}")
        
        st.write(f"Number of boreholes: {num_sondeos}")
        if num_sondeos == ">4":
            st.success("For construction areas greater than 1,000 m², the number of boreholes will depend on ground variability. It will be the responsibility of the geotechnical specialist to determine this number and the General Directorate of Public Works to approve it.")
        
        st.write(f"Estimated depth per borehole: {profundidad} m")
        st.info("This depth is measured from the ground floor level or from the lower level of the last basement, if any.")
        if profundidad != ">10":
            st.success(f"The total borehole depth should be: {profundidad - nivel_PB} m measured from natural ground level.")
    
        if profundidad == ">10":
            st.success("For projects with more than 10 levels, the borehole depth should be such that the stress increase does not exceed approximately 10% of the initial effective stresses. It will be the responsibility of the geotechnical specialist to determine these depths, and the General Directorate of Public Works to approve them.")
    
        st.divider()
    
        st.warning("⚠️ **Important note:** If rock is encountered before reaching the required minimum depth, in constructions of **ten (10) or more levels**, at least 3.00 m should be drilled into the rock to verify that the layer is continuous. If the construction has **less than ten (10) levels**, instead of drilling into rock, additional boreholes may be performed to verify the continuity of the rock layer.")
        st.balloons()
    
        #st.header("💰 If you want a Quote")
        #st.write("📩Contact proyectos@geotecniaterranova.com")
        #st.write("✅or by Whatsapp https://wa.link/vai3cy") 
    
    st.warning("⚠️ **Disclaimer:** This application is an educational tool and does not replace the evaluation of a qualified geotechnical engineer. Always consult a professional for the final design.")
    st.write("We appreciate user feedback to improve this tool. If you have suggestions or find errors, you can contact us through our social media or email geotecniapps@gmail.com.")
    st.markdown("<center><h5>Made by GeotecniApps.com</h5></center>", unsafe_allow_html=True)