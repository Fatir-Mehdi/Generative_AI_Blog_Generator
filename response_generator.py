from langchain.prompts import PromptTemplate
from llama_model.model_config import configure_llama_model

# Path to the LLaMA model file
MODEL_PATH = r"C:\Users\asus\Desktop\llama model\llama-2-7b-chat.ggmlv3.q8_0.bin"

def get_llama_response(input_text: str, no_words: int, blog_style: str) -> str:
    """
    Generates a blog response using the LLaMA model.

    Args:
        input_text (str): Topic of the blog.
        no_words (int): Number of words for the blog.
        blog_style (str): Target audience style (e.g., Researchers, Data Scientists).

    Returns:
        str: Generated blog response.
    """
    try:
        # Configure the model
        llm = configure_llama_model(MODEL_PATH)

        # Prompt template
        template = """
        Write a blog for {blog_style} job profile on the topic "{input_text}"
        within {no_words} words.
        """
        prompt = PromptTemplate(
            input_variables=["blog_style", "input_text", "no_words"],
            template=template
        )

        # Generate response
        response = llm.invoke(
            prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words)
        )
        return response
    except Exception as e:
        return f"Error generating response: {str(e)}"
