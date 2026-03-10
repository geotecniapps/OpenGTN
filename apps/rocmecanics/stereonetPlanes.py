import streamlit as st
import matplotlib.pyplot as plt
import mplstereonet

def main():
    #-------------------------------
    # Streamlit app for estereonets
    #-------------------------------
    
    # Título y descripción de la app
    st.set_page_config(page_title="GTN | STEREOGRAM", page_icon=":material/sort:", layout="centered")
    
    st.title("GTN | STEREOGRAM PLANE VISUALIZER")
    st.markdown("This application allows you to visualize planes on a stereonet by entering their strike and dip. You can input multiple planes and see their great circles and poles on the stereonet.")
    st.markdown("The library utilized for the stereonet is [mplstereonet](https://mplstereonet.readthedocs.io/en/latest/), which is a powerful tool for plotting stereonets in Python.")
   

    # Banner de publicidad
    st.divider()
    
    # User selects the number of planes
    number_of_planes = st.number_input("How many planes do you want to visualize?", min_value=1, max_value=10, value=1, step=1)
    
    planes=[] # Creates a void list to storage the planes data
    
    # User inputs trike and dip for each plane
    st.info("Enter the strike and dip of each plane.")
    st.write("This application considers strike in *azimuthal* form (from 0° to 360°) and dip using the *right-hand rule* (from 0° to 90°).")
    
    st.divider()
    
    for i in range(number_of_planes):
        
        # Cretes two columns for a better layout
        st.write(f'Plane {i+1}')
        col1, col2 = st.columns(2)
    
        with col1:
            # strike = st.number_input(f'Rumbo {i+1} (°)', min_value=0, max_value=360, value=0)
            strike = st.slider(f'Strike {i+1} (°)', 0, 360, 45)
    
        with col2:
            # dip = st.number_input(f'Echado {i+1} (°)', min_value=0, max_value=90, value=0)
            dip = st.slider(f'Dip {i+1} (°)', 0, 90, 45)
    
        planes.append((strike, dip)) # Appends each plane to planes list
    
        st.divider() # Adds a divider between planes
    
    # Creates the estereonets
    
    # Create the figure
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, projection='stereonet')
    
    #plot each plane and pole
    for i, (strike, dip) in enumerate(planes, start=1):
        #plot the plane great circle
        plane_line = ax.plane(strike, dip, '-', linewidth=2, label=f'Plane {i}: Strike {strike}°, Dip {dip}°')
        #plot the pole as a circle marker of the same color as the plane
        ax.pole(strike, dip, marker='o', color=plane_line[0].get_color() ,markersize=10)
    
    #add graph grid and legend
    ax.grid(True, linewidth=0.5)             # show the grid
    # for azimuth ticks
    ax.set_azimuth_ticks(range(0, 360, 15))  # at 15°
    
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2)
    
    #Display the figure in the app
    st.pyplot(fig)
    
    st.warning("⚠️ **Disclaimer:** This application is an educational tool and does not replace the evaluation of a qualified geotechnical engineer. Always consult a professional for the final design.")
    st.write("We appreciate user feedback to improve this tool. If you have suggestions or find errors, you can contact us through our social media or email geotecniapps@gmail.com.")
    st.markdown("<center><h5>Made by GeotecniApps.com</h5></center>", unsafe_allow_html=True)