import streamlit as st
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(
    page_title='Trends tracker',
    page_icon='📰'
)

st.sidebar.info("select a page above.")

st.title("Welcome to Trend Tracker 👋")

st.markdown("""
###### This app helps journalists to stay on top of trending topics and discover new article ideas by identifying gaps in existing coverage.
""")

st.markdown('\n')

st.subheader("📈 Trend tracking")
st.markdown("""
Analyze the popularity of keyword(s) over time. See if it’s currently trending, identify peak interest periods, and plan content based on those graph.
""")


st.markdown("""
1. **Enter a Keyword**: Type a word or phrase in the search bar.
2. **Set Date Range**: Select a date range in the sidebar.
3. **View Trends**: Check the interest graph to see when the keyword was most popular.
""")

st.markdown("---")

st.subheader("🧐 Coverage analysis")
st.markdown("""
Find trending topics that RTBF hasn’t covered. Get fresh article ideas based on high-interest themes with minimal or no coverage.
""")


st.markdown("""
1. **Compare with Trends**: The app checks trending topics across the web.
2. **Identify Gaps**: See popular topics not yet covered by RTBF.
3. **Get Suggestions**: Offers interesting topics for new articles.
""")



st.markdown("---")

st.subheader("💬 RTBFgpt")
st.markdown("""
Interact with the RTBF Trend Bot to get insights about RTBF articles. Ask questions about specific topics to see related articles or discover what has been covered.
""")

st.markdown("""
1. **Ask a Question**: Enter a keyword or topic you are interested in.
2. **Receive Article Insights**: Get a list of the latest RTBF articles that match your query.
""")

st.markdown("---")

st.markdown("**Let's find some ideas.. 🔎**")

first, second, third = st.columns(3)

with first:
    trend_tracking = st.button("Trends tracker")
    if trend_tracking:
        switch_page("trends tracker")


with second:
    trend_tracking = st.button("Coverage analysis")
    if trend_tracking:
        switch_page("Coverage analysis")


with third:
    trend_tracking = st.button("Chatbot")
    if trend_tracking:
        switch_page("Chatbot")
