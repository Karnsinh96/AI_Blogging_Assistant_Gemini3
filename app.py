import streamlit as st

st.set_page_config(layout="wide")

#title of our app
st.title('✍️कृत्रिम लेखक✍️- Your AI Writing Companion🤖')

#create a subheader
st.subheader("🦾In The Era of AI, We make Your Blogging Easy 👨🏻‍💻")

#sidebar for user input
with st.sidebar:
    st.title("Input Your Blog Details")
    st.subheader("Enter Details of the Blog You want to generate")

    #Blog title
    blog_title=st.text_input("Blog Title")