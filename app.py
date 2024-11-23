import streamlit as st
from llama_model.response_generator import get_llama_response

# Streamlit app configuration
st.set_page_config(
    page_title="Generate Blogs",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

def main():
    st.header("Generate Blogs 🤖")

    # Input for blog topic
    input_text = st.text_input("Enter the Blog Topic")

    # Additional fields using columns
    col1, col2 = st.columns(2)

    with col1:
        no_words = st.text_input("Number of Words")
    with col2:
        blog_style = st.selectbox(
            "Writing the blog for",
            ("Researchers", "Data Scientist", "Common People"),
            index=0
        )

    # Generate button
    if st.button("Generate"):
        # Validate inputs
        if not input_text.strip():
            st.error("Please enter a blog topic.")
        elif not no_words.isdigit() or int(no_words) <= 0:
            st.error("Please enter a valid number of words.")
        else:
            # Generate and display response
            response = get_llama_response(input_text, int(no_words), blog_style)
            st.write(response)

if __name__ == "__main__":
    main()
