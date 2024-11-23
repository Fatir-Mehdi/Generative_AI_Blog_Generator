from langchain_community.llms import CTransformers

def configure_llama_model(model_path: str, max_new_tokens: int = 256, temperature: float = 0.01):
    """
    Configures and returns the LLaMA 2 model.

    Args:
        model_path (str): Path to the model file.
        max_new_tokens (int): Maximum number of tokens to generate.
        temperature (float): Sampling temperature for text generation.

    Returns:
        CTransformers: Configured LLaMA model instance.
    """
    return CTransformers(
        model=model_path,
        model_type="llama",
        config={
            "max_new_tokens": max_new_tokens,
            "temperature": temperature
        }
    )
