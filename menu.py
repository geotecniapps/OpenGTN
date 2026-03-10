import streamlit as st

def main():
    st.title("GTN | HOME")
    st.write("Welcome to the GTN software suite!")

    #st.divider()

    st.write("Please select one of the following applications to access its features and tools. Each application is designed to assist you with specific tasks related to geotechnical engineering and soil mechanics.")

    #*********Secciones*********
    st.divider()
    st.markdown("**Applications**")


    col1, col2, col3 = st.columns([6,1,6])

    with col1:
        #----- SHALLOW FOUNDATIONS | BEARING CAPACITY
        st.write("Shallow Foundations | Bearing Capacity")
        with st.expander("Click to see available apps", expanded=False): 


            st.write("1. **CAP CARGA CDMX**: A tool to verify the load capacity of shallow foundations according to the NTC CDMX - 2023, with different equations for cohesive and frictional soils.")
            if st.button("CAP CARGA CDMX", type="primary"):
                st.session_state.app = "CAP CARGA CDMX"
                st.rerun()  # Rerun the app to reflect the changes in session state
            
            st.write("2. **CAP CARGA GDL**: A tool to verify the load capacity of shallow foundations according to the 1997 GDL regulations, with different equations for cohesive and frictional soils, and corrections for groundwater level and eccentricity.")
            if st.button("CAP CARGA GDL", type="primary"):
                st.session_state.app = "CAP CARGA GDL"
                st.rerun()  # Rerun the app to reflect the changes in session state


            st.write("3. **CAP CARGA TERZ**: A tool to verify the load capacity of shallow foundations according to Terzaghi's bearing capacity theory, with different equations for cohesive and frictional soils, and corrections for groundwater level and eccentricity.")
            if st.button("CAP CARGA TERZ", type="primary"):
                st.session_state.app = "CAP CARGA TERZ"
                st.rerun()  # Rerun the app to reflect the changes in session state

            st.write("4. **CAP CARGA PER**: A tool to verify the load capacity of shallow foundations according to the NTC of Peru, with different equations for cohesive and frictional soils, and corrections for groundwater level and eccentricity.")
            if st.button("CAP CARGA PER", type="primary"):
                st.session_state.app = "CAP CARGA PER"
                st.rerun()  # Rerun the app to reflect the changes in session state

        #----- SHALLOW FOUNDATIONS |  SETTLEMENT
        st.divider()
        st.write("Shallow Foundations | Settlement")
        with st.expander("Click to see available apps", expanded=False): 

            st.write("1. **ELASTIC SETTLEMENT**: A tool to calculate the elastic settlement of shallow foundations according to the theory of elasticity.")
            if st.button("ELASTIC SETTLEMENT", type="primary"):
                # Updates
                st.session_state.app = "ELASTIC SETTLEMENT"    # Attribute API
                st.rerun()  # Rerun the app to reflect the changes in session state

    #----- GEOTECHNICAL EXPLORATION
        st.divider()
        st.write("Geotechnical Exploration")
        with st.expander("Click to see available apps", expanded=False): 

            st.write("1. **EXPLO GDL**: A simple tool to determine the number and depth of boreholes for geotechnical exploration in Guadalajara, according to the guidelines provided by the city government.")
            if st.button("EXPLO GDL", type="primary"):
                # Updates
                st.session_state.app = "EXPLO GDL"    # Attribute API
                st.rerun()  # Rerun the app to reflect the changes in session state

    with col2:
        st.write(" ")



    with col3:
    #----- LAB TESTS
        st.write("Laboratory Tests")
        with st.expander("Click to see available apps", expanded=False): 

            st.write("1. **TRIAXIAL**: A tool to analyze the behavior of soils under triaxial stress conditions.")
            if st.button("TRIAXIAL", type="primary"):
                # Updates
                st.session_state.app = "TRIAXIAL"    # Attribute API
                st.rerun()  # Rerun the app to reflect the changes in session state

    #----- ROC MECHANICS
        st.divider()
        st.write("Rock Mechanics")
        with st.expander("Click to see available apps", expanded=False):
            
            st.write("1. **RQD CALCULATOR**: A tool to calculate the Rock Quality Designation (RQD) based on the length of core pieces and total core length.")
            if st.button("RQD CALCULATOR", type="primary"):
                # Updates
                st.session_state.app = "RQD CALCULATOR"    # Attribute API
                st.rerun()  # Rerun the app to reflect the changes in session state

            st.write("2. **STEREONET POLE DENSITY**: A tool to create a pole density stereogram based on the strike and dip of planes, using the mplstereonet library.")
            if st.button("STEREONET POLE DENSITY", type="primary"):
                # Updates
                st.session_state.app = "STEREONET POLE DENSITY"    # Attribute API
                st.rerun()  # Rerun the app to reflect the changes in session state

            st.write("3. **STEREOGRAM PLANE VISUALIZER**: A tool to visualize planes on a stereonet by entering their strike and dip, showing their great circles and poles using the mplstereonet library.")
            if st.button("STEREOGRAM PLANE VISUALIZER", type="primary"):
                # Updates
                st.session_state.app = "STEREOGRAM PLANE VISUALIZER"    # Attribute API
                st.rerun()  # Rerun the app to reflect the changes in session state

    #----- RETAINING WALLS AND SLOPES
        st.divider()
        st.write("Retaining Walls and Slopes")
        with st.expander("Click to see available apps", expanded=False,):
            
            st.write("1. **EARTH PRESSURE RANKINE**: A tool to calculate the active, passive, and at-rest earth pressures on retaining walls using Rankine's theory, based on soil properties and wall dimensions.")
            if st.button("EARTH PRESSURE RANKINE", type="primary"):
                # Updates
                st.session_state.app = "EARTH PRESSURE RANKINE"    # Attribute API
                st.rerun()  # Rerun the app to reflect the changes in session state