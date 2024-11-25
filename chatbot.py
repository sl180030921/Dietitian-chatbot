import openai
import gradio as gr
import os




#openai.api_key = os.getenv("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")


openai.api_key = "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"

messages = [{"role": "system", "content": "You are a Dietitian and Nutritionist"}]

def CustomChatGPT(user_input):
    try:
        messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        return reply
    except openai.error.OpenAIError as e:
        return f"An error occurred: {str(e)}"

# Create Gradio interface
demo = gr.Interface(
    fn=CustomChatGPT,
    inputs="text",
    outputs="text",
    title="Dietitian & Nutritionist Chatbot"
)

# Launch the Gradio app
demo.launch(share=True)