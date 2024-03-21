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

    # Keywords input
    keywords = st.text_area("Keywords (comma-separated)")
    
    # Number of words
    num_words = st.slider("Number of Words", min_value=100, max_value=1000, step=50)

    #Number of images 

    #Submit Button
    submit_button=st.button("Genrate Blog")