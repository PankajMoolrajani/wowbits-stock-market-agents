import os
from litellm import completion

def run_llm(model: str, message: str) -> str:
    """
    Run any LLM model using litellm and return the response.
    
    Args:
        model (str): The model identifier (e.g. "gpt-3.5-turbo", "claude-2", etc.)
        message (str): The input message/prompt to send to the model
        
    Returns:
        str: The model's response text
    """
    try:
        print(f"Running model {model} with message {message}")
        response = completion(
            model=model,
            messages=[{
                "role": "user",
                "content": message
            }]
        )
        
        # Extract the response text from the completion
        if response and hasattr(response, 'choices') and len(response.choices) > 0:
            return response.choices[0].message.content
        else:
            return "Error: No response generated"
            
    except Exception as e:
        return f"Error running model {model}: {str(e)}"
