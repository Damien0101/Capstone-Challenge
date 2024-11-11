import streamlit as st


st.title("Coverage Analyzer 🔎")

with st.sidebar:
    st.write('# ⚙️ Settings')
    st.write("**Tip**: Try shorter date ranges to focus on recent changes in trends.")

    st.markdown("### Data Source:")
    st.markdown("This data come from [Google Trends](https://trends.google.com/trends/)")

