import streamlit as st
import periodictable

st.set_page_config(page_title="Periodic Table Explorer", layout="wide")

st.title("🔬 Interactive Periodic Table")

# Define categories with colors
categories = {
    "Alkali Metal": "#FF6666",
    "Alkaline Earth Metal": "#FFDEAD",
    "Transition Metal": "#FFD700",
    "Post-transition Metal": "#FFB6C1",
    "Metalloid": "#ADFF2F",
    "Nonmetal": "#90EE90",
    "Halogen": "#87CEFA",
    "Noble Gas": "#DDA0DD",
    "Lanthanide": "#FFA07A",
    "Actinide": "#FF8C00",
    "Other": "#D3D3D3"
}

# Define groups by atomic number
noble_gases = {2, 10, 18, 36, 54, 86, 118}
alkali_metals = {3, 11, 19, 37, 55, 87}
alkaline_earth_metals = {4, 12, 20, 38, 56, 88}
halogens = {9, 17, 35, 53, 85, 117}

def categorize(el):
    if el.number in noble_gases:
        return "Noble Gas"
    elif el.number in alkali_metals:
        return "Alkali Metal"
    elif el.number in alkaline_earth_metals:
        return "Alkaline Earth Metal"
    elif el.number in halogens:
        return "Halogen"
    elif el.symbol in ["H", "C", "N", "O", "P", "S", "Se"]:
        return "Nonmetal"
    else:
        return "Other"

# Periodic table layout
rows = [
    [1, None, None, None, None, None, None, None, None, None, None, None, None, 2],
    [3, 4, None, None, None, None, None, None, None, None, None, None, 5, 6],
    [11, 12, None, None, None, None, None, None, None, None, None, None, 13, 14, 15, 16, 17, 18],
    [19, 20, None, None, None, None, None, None, None, None, None, None, 31, 32, 33, 34, 35, 36],
    [37, 38, None, None, None, None, None, None, None, None, None, None, 49, 50, 51, 52, 53, 54],
    [55, 56, None, None, None, None, None, None, None, None, None, None, 81, 82, 83, 84, 85, 86],
    [87, 88, None, None, None, None, None, None, None, None, None, None, 113, 114, 115, 116, 117, 118],
    [None, None, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, None],
    [None, None, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, None]
]

# Display grid
for row in rows:
    cols = st.columns(len(row))
    for i, atomic_no in enumerate(row):
        if atomic_no is None:
            cols[i].markdown(" ")
        else:
            el = periodictable.elements[atomic_no]
            cat = categorize(el)
            color = categories.get(cat, "#D3D3D3")
            with cols[i]:
                st.markdown(
                    f"""
                    <div style='background-color:{color};
                                border-radius:8px;
                                text-align:center;
                                padding:6px;
                                margin:2px;
                                color:black;
                                font-size:14px;'>
                        <b>{el.symbol}</b><br>
                        <span style='font-size:12px'>{el.name}</span><br>
                        <span style='font-size:11px; color:gray'>({cat})</span><br>
                        <span style='font-size:10px; color:dimgray'>{el.number}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

# Selected element info (optional future expansion)
if "selected" in st.session_state:
    el = st.session_state["selected"]
    st.subheader("Element Information")
    st.write(f"**Name:** {el.name.capitalize()}")
    st.write(f"**Symbol:** {el.symbol}")
    st.write(f"**Atomic Number:** {el.number}")
    st.write(f"**Atomic Mass:** {el.mass}")
    st.write(f"**Density:** {el.density}")
    st.write(f"**Category:** {categorize(el)}")

# Footer
st.markdown(
    """
    <hr>
    <div style='text-align: center; font-size: 14px; color: gray;'>
    Created by <b>Engr. Fijabi J Adekunle</b><br>
    Marine Engineer turned Data Scientist
    </div>
    """,
    unsafe_allow_html=True
)
