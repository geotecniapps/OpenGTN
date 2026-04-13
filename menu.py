import streamlit as st

def main():
    st.set_page_config(page_title="GTN Software Suite", page_icon="🧱", layout="centered")
    
    st.title("🧱 GTN | HOME")
    st.markdown("Welcome to the **GTN software suite** for geotechnical engineering!")
    st.markdown("---")

    st.markdown("### 📂 Applications")

    col1, col2, col3 = st.columns([6,1,6])

    with col1:
        st.markdown("#### 🏗️ Shallow Foundations")
        st.markdown("*Bearing Capacity*")
        with st.expander("Click to see available apps", expanded=False): 

            st.write("1. **CAP CARGA CDMX** 🇲🇽: A tool to verify the load capacity of shallow foundations according to the NTC CDMX - 2023, with different equations for cohesive and frictional soils.")
            if st.button("CAP CARGA CDMX", type="primary", key="btn_cap_cdmx"):
                st.session_state.app = "CAP CARGA CDMX"
                st.rerun()
            
            st.write("2. **CAP CARGA GDL** 🇲🇽: A tool to verify the load capacity of shallow foundations according to the 1997 GDL regulations.")
            if st.button("CAP CARGA GDL", type="primary", key="btn_cap_gdl"):
                st.session_state.app = "CAP CARGA GDL"
                st.rerun()

            st.write("3. **CAP CARGA TERZ**: A tool to verify the load capacity of shallow foundations according to Terzaghi's bearing capacity theory.")
            if st.button("CAP CARGA TERZ", type="primary", key="btn_cap_terz"):
                st.session_state.app = "CAP CARGA TERZ"
                st.rerun()

            st.write("4. **CAP CARGA PER** 🇵🇪: A tool to verify the load capacity of shallow foundations according to the NTC of Peru.")
            if st.button("CAP CARGA PER", type="primary", key="btn_cap_per"):
                st.session_state.app = "CAP CARGA PER"
                st.rerun()

        st.markdown("---")
        st.markdown("#### 📐 Shallow Foundations")
        st.markdown("*Settlement*")
        with st.expander("Click to see available apps", expanded=False): 

            st.write("1. **ELASTIC SETTLEMENT**: A tool to calculate the elastic settlement of shallow foundations according to the theory of elasticity.")
            if st.button("ELASTIC SETTLEMENT", type="primary", key="btn_elastic"):
                st.session_state.app = "ELASTIC SETTLEMENT"
                st.rerun()

        st.markdown("---")
        st.markdown("#### 🔬 Geotechnical Exploration")
        with st.expander("Click to see available apps", expanded=False): 

            st.write("1. **EXPLO GDL** 🇲🇽: A simple tool to determine the number and depth of boreholes for geotechnical exploration in Guadalajara.")
            if st.button("EXPLO GDL", type="primary", key="btn_explo_gdl"):
                st.session_state.app = "EXPLO GDL"
                st.rerun()

    with col2:
        st.write("")

    with col3:
        st.markdown("#### 🧪 Laboratory Tests")
        with st.expander("Click to see available apps", expanded=False): 

            st.write("1. **TRIAXIAL**: A tool to analyze the behavior of soils under triaxial stress conditions.")
            if st.button("TRIAXIAL", type="primary", key="btn_triaxial"):
                st.session_state.app = "TRIAXIAL"
                st.rerun()

        st.markdown("---")
        st.markdown("#### 🪨 Rock Mechanics")
        with st.expander("Click to see available apps", expanded=False):
            
            st.write("1. **RQD CALCULATOR**: A tool to calculate the Rock Quality Designation (RQD) based on the length of core pieces.")
            if st.button("RQD CALCULATOR", type="primary", key="btn_rqd"):
                st.session_state.app = "RQD CALCULATOR"
                st.rerun()

            st.write("2. **STEREONET POLE DENSITY**: A tool to create a pole density stereogram based on the strike and dip of planes.")
            if st.button("STEREONET POLE DENSITY", type="primary", key="btn_stereonet_density"):
                st.session_state.app = "STEREONET POLE DENSITY"
                st.rerun()

            st.write("3. **STEREOGRAM PLANE VISUALIZER**: A tool to visualize planes on a stereonet.")
            if st.button("STEREOGRAM PLANE VISUALIZER", type="primary", key="btn_stereonet_visualizer"):
                st.session_state.app = "STEREOGRAM PLANE VISUALIZER"
                st.rerun()

        st.markdown("---")
        st.markdown("#### 🧱 Retaining Walls and Slopes")
        with st.expander("Click to see available apps", expanded=False):
            
            st.write("1. **EARTH PRESSURE RANKINE**: A tool to calculate the active, passive, and at-rest earth pressures on retaining walls using Rankine's theory.")
            if st.button("EARTH PRESSURE RANKINE", type="primary", key="btn_earth_pressure"):
                st.session_state.app = "EARTH PRESSURE RANKINE"
                st.rerun()