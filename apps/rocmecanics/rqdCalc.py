import streamlit as st
import pandas as pd

def main():
    #titulo y descripción de la app
    st.title("GTN | RQD CALCULATOR")

    def calculate_rqd(core_pieces_str, total_length):
        """
        Calculates the Rock Quality Designation (RQD).
    
        Parameters:
        - core_pieces_str (str): A string containing core piece lengths, separated by commas.
        - total_length (float): The total length of the core run.
    
        Returns:
        - tuple: A tuple containing the RQD percentage, the sum of competent core pieces,
                 and a list of the competent core lengths. Returns (None, None, None) if inputs are invalid.
        """
        if total_length <= 0:
            return None, None, None
    
        try:
            # Convert the string of pieces into a list of floats
            pieces = [float(p.strip()) for p in core_pieces_str.split(',') if p.strip()]
            
            # Filter for pieces longer than 10 cm (0.1 m)
            competent_pieces = [p for p in pieces if p > 10]
            
            # Sum the lengths of the competent pieces
            sum_competent_pieces = sum(competent_pieces)
            
            # Calculate RQD
            rqd = (sum_competent_pieces / total_length) * 100
            
            return rqd, sum_competent_pieces, competent_pieces
        except (ValueError, ZeroDivisionError):
            return None, None, None
    
    def get_rqd_quality(rqd):
        """
        Determines the rock mass quality based on the RQD value.
    
        Parameters:
        - rqd (float): The RQD percentage.
    
        Returns:
        - str: The rock mass quality classification.
        """
        if rqd is None:
            return ""
        if rqd < 25:
            return "Very Poor"
        elif rqd < 50:
            return "Poor"
        elif rqd < 75:
            return "Fair"
        elif rqd < 90:
            return "Good"
        else:
            return "Excellent"
    
    # --- Streamlit App Interface ---
    
    st.set_page_config(page_title="GTN | RQD CALCULATOR", page_icon=":material/landslide:", layout="centered")
    
    # Custom CSS for better styling
    st.markdown("""
        <style>
        .metric-container {
            text-align: center;
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 1rem;
            margin-top: 1rem;
            background-color: #fafafa;
        }
        .metric-value {
            font-size: 2.5rem;
            font-weight: bold;
            color: #4CAF50;
        }
        .metric-label {
            font-size: 1.2rem;
            color: #555;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("""
    This application calculates the **Rock Quality Designation Index (RQD)** according to Deere's methodology (1967). 
    RQD is a fundamental parameter in geotechnics and rock mechanics for classifying rock mass quality from drilling cores.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. Data Input")
        
        # Input for total length of core run
        total_length = st.number_input(
            "Total borehole length (cm)",
            min_value=0.1,
            value=150.0,
            step=10.0,
            help="Enter the total borehole length in centimeters."
        )
    
        # Input for core pieces
        core_pieces_str = st.text_area(
            "Core piece lengths (cm)",
            "20, 35, 8, 15, 5, 25, 12, 9, 30",
            height=150,
            help="Enter the lengths of each recovered core piece, separated by commas."
        )
        
        calculate_button = st.button("Calculate RQD", type="primary")
    
    with col2:
        st.subheader("2. Results")
        
        if calculate_button:
            rqd, sum_competent, competent_list = calculate_rqd(core_pieces_str, total_length)
            st.balloons()
            
            if rqd is not None:
                quality = get_rqd_quality(rqd)
                
                st.markdown(f"""
                <div class="metric-container">
                    <div class="metric-label">Calculated RQD</div>
                    <div class="metric-value">{rqd:.2f}%</div>
                    <div class="metric-label" style="font-weight: bold; color: black; margin-top: 10px;">Rock Mass Quality: {quality}</div>
                </div>
                """, unsafe_allow_html=True)
    
                with st.expander("View calculation details"):
                    st.write(f"**Sum of pieces > 10 cm:** `{sum_competent:.2f} cm`")
                    st.write(f"**Total Borehole Length:** `{total_length:.2f} cm`")
                    st.latex(r'''
                    RQD = \left( \frac{\sum \text{piece lengths} > 10 \text{ cm}}{\text{Total Borehole Length}} \right) \times 100
                    ''')
                    st.latex(fr'''
                    RQD = \left( \frac{{{sum_competent:.2f}}}{{{total_length:.2f}}} \right) \times 100 = {rqd:.2f}\%
                    ''')
                    
                    st.subheader("Core pieces considered (> 10 cm):")
                    df_competent = pd.DataFrame(competent_list, columns=["Length (cm)"])
                    st.dataframe(df_competent, use_container_width=True)
    
            else:
                st.error("Please enter valid values. Make sure the total length is greater than zero and the piece lengths are numbers.")
    
    # --- RQD Quality Table ---
    st.subheader("Rock Mass Quality Classification Table (Deere, 1967)")
    
    data = {
        'RQD (%)': ['< 25', '25 - 50', '50 - 75', '75 - 90', '90 - 100'],
        'Rock Mass Quality': ['Very Poor', 'Poor', 'Fair', 'Good', 'Excellent']
    }
    df = pd.DataFrame(data)
    
    with st.expander("View Deere's rock mass quality classification reference table", expanded=False):
        st.table(df)
    
    st.info("Note: RQD is calculated by summing the length of intact rock core pieces of 10 cm or more and dividing that sum by the total borehole length.")
    st.warning("⚠️ **Disclaimer:** This application is an educational tool and does not replace the evaluation of a qualified geotechnical engineer. Always consult a professional for the final design.")
    st.write("We appreciate user feedback to improve this tool. If you have suggestions or find errors, you can contact us through our social media or email geotecniapps@gmail.com.")
    st.markdown("<center><h5>Made by GeotecniApps.com</h5></center>", unsafe_allow_html=True)