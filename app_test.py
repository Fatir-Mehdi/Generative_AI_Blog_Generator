import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

# Function to get response from LLaMA 2 model
def get_llama_response(input_text, no_words, blog_style):
    try:
        # LLaMA 2 model configuration
        llm = CTransformers(
            model=r'C:\Users\asus\Desktop\llama model\llama-2-7b-chat.ggmlv3.q8_0.bin',
            model_type='llama',
            config={
                'max_new_tokens': 256,
                'temperature': 0.01
            }
        )

        # Prompt template
        template = """
        Write a blog for {blog_style} job profile on the topic "{input_text}"
        within {no_words} words.
        """
        prompt = PromptTemplate(
            input_variables=["blog_style", "input_text", "no_words"],
            template=template
        )

        # Generate response from the LLaMA 2 model
        response = llm.invoke(
            prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words)
        )
        return response
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Streamlit app configuration
st.set_page_config(
    page_title="Generate Blogs",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

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
        response = get_llama_response(input_text, no_words, blog_style)
        st.write(response)
