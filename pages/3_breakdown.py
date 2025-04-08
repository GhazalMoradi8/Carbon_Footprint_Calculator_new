import streamlit as st
import matplotlib.pyplot as plt

# --- App Config ---
st.set_page_config(
    page_title="Green Tomorrow",
    page_icon="🌿",
    layout="centered"
)

# --- Force Logo to Appear at Top of Sidebar ---
st.markdown(
    """
    <style>
        [data-testid="stSidebar"]::before {
            content: "";
            display: block;
            background-image: url('https://raw.githubusercontent.com/GhazalMoradi8/Carbon_Footprint_Calculator/main/GreenPrint_logo.png');
            background-size: 90% auto;
            background-repeat: no-repeat;
            background-position: center;
            height: 140px;
            margin: 1.5rem auto -4rem auto;  /* SUPER tight top & bottom spacing */
        }

        section[data-testid="stSidebar"] {
            background-color: #d6f5ec;
        }

        .stApp {
            background-color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
        .stApp {
            background-color: white;  /* main content area */
        }
        section[data-testid="stSidebar"] {
            background-color: #e8f8f5;  /* soft green sidebar */
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📊 Emission Breakdown")
st.write("Here is how your estimated carbon footprint breaks down by activity.")

# Make sure emissions are available
if "emission_values" not in st.session_state or not st.session_state.emission_values:
    st.warning("No emission data found. Please fill in your activity data on the main page first.")
else:
    # Get emissions from session state
    emissions_dict = st.session_state.emission_values

    # Filter out zero values for a cleaner chart
    emissions_filtered = {k: v for k, v in emissions_dict.items() if v > 0}

    # If there's valid data to plot
    if emissions_filtered:
        labels = [activity.replace("_", " ").capitalize() for activity in emissions_filtered.keys()]
        values = list(emissions_filtered.values())

        # Create pie chart
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
        ax.axis("equal")  # Equal aspect ratio ensures pie is a circle

        st.pyplot(fig)

        # Show a table as well for details
        st.markdown("### 🔍 Detailed Emissions (tons CO₂):")
        for label, value in zip(labels, values):
            st.write(f"- **{label}**: {value:.4f} tons")
    else:
        st.info("Your inputs resulted in zero emissions. Try entering some activity data.")

