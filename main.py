import streamlit as st

from apps.soilmecanics import capcargaTER

if 'app' not in st.session_state:
    st.session_state['app'] = None

# Set page config based on current app
if st.session_state.app is None:
    st.set_page_config(page_title="GTN | MAIN MENU", page_icon=":material/menu:", layout="centered")


if st.button("HOME", type="primary", key="home_button", icon=":material/home:", help="Go back to the main menu"):
    st.session_state.clear()
    st.rerun()

if st.session_state.get("app") == None:
        from menu import main as mainmenu
        mainmenu()


#*****RENDERIZAR APLICACIONES SEGÚN SELECCIÓN EN EL MENÚ PRINCIPAL*****
#Renderizar la aplicación seleccionada

#----- BEARING CAPACITY
if st.session_state.get("app") == "CAP CARGA CDMX":
    st.set_page_config(page_title="GTN | CAP CARGA CDMX", page_icon=":material/calculate:", layout="centered")
    from apps.soilmecanics.capcargaCDMX import main as capcargaCDMX
    capcargaCDMX()

if st.session_state.get("app") == "CAP CARGA GDL":
    st.set_page_config(page_title="GTN | CAP CARGA GDL", page_icon=":material/calculate:", layout="centered")
    from apps.soilmecanics.capcargaGDL import main as capcargaGDL
    capcargaGDL()

if st.session_state.get("app") == "CAP CARGA TERZ":
    st.set_page_config(page_title="GTN | CAP CARGA TERZ", page_icon=":material/calculate:", layout="centered")
    from apps.soilmecanics.capcargaTER import main as capcargater
    capcargater()

if st.session_state.get("app") == "CAP CARGA PER":
    st.set_page_config(page_title="GTN | CAP CARGA PER", page_icon=":material/calculate:", layout="centered")
    from apps.soilmecanics.capcargaPER import main as capcargaPer
    capcargaPer()

#----- ELASTIC SETTLEMENT    
if st.session_state.get("app") == "ELASTIC SETTLEMENT":
    st.set_page_config(page_title="GTN | ELASTIC SETTLEMENT", page_icon=":material/sort:", layout="centered")
    from apps.shallowFoundSettle.elasticsettle import main as elasticsettle
    elasticsettle()

#----- GEOTECHNICAL EXPLORATION
if st.session_state.get("app") == "EXPLO GDL":
    st.set_page_config(page_title="GTN | GEOEXPLO GDL", page_icon=":material/sort:", layout="centered")
    from apps.geoexplo.geoexplgdl import main as geoexplgdl
    geoexplgdl()

#----- LAB TESTS
if st.session_state.get("app") == "TRIAXIAL":
    st.set_page_config(page_title="GTN | TRIAXIAL", page_icon=":material/sort:", layout="centered")
    from apps.LabTests.triaxial import main as triaxial
    triaxial()

#----- ROCK MECHANICS
if st.session_state.get("app") == "RQD CALCULATOR":
    st.set_page_config(page_title="GTN | RQD CALCULATOR", page_icon=":material/landslide:", layout="centered")
    from apps.rocmecanics.rqdCalc import main as rqdCalc
    rqdCalc()

if st.session_state.get("app") == "STEREONET POLE DENSITY":
    st.set_page_config(page_title="GTN | STEREONET POLE DENSITY", page_icon=":material/landslide:", layout="centered")
    from apps.rocmecanics.stereonetPoleDens import main as stereonetPoleDens
    stereonetPoleDens()

if st.session_state.get("app") == "STEREOGRAM PLANE VISUALIZER":
    st.set_page_config(page_title="GTN | STEREOGRAM PLANE VISUALIZER", page_icon=":material/landslide:", layout="centered")
    from apps.rocmecanics.stereonetPlanes import main as stereonetPlanes
    stereonetPlanes()


#------- RETAINING WALLS AND SLOPES
if st.session_state.get("app") == "EARTH PRESSURE RANKINE":
    st.set_page_config(page_title="GTN | EARTH PRESSURE RANKINE", page_icon=":material/sort:", layout="centered")
    from apps.retWallsAndSlopes.epRankine import main as epRankine
    epRankine()