# Simple Dietitian Chatbot Using OpenAI and Gradio
This project is a simple chatbot application built using OpenAI's gpt 4.0 migrate model and the Gradio library. The chatbot acts as a conversational assistant, responding to user inputs with helpful replies. It is easy to set up and serves as an example of integrating OpenAI's API with a user-friendly web interface.

## Features
Powered by OpenAI's GPT-4.o for conversational responses.

Simple and interactive Gradio web interface.

Customizable chatbot role (e.g., Dietitian, Teacher, or Assistant).

Deployable locally or shareable via a public link.

## Requirements
Python 3.7 or later
An OpenAI API Key (https://platform.openai.com/account/a...)
Installed Python libraries: openai, gradio

## Installation & Usage
1. Install the required Python packages.
2. Set up your OpenAI API Key.
3. Run the chatbot script.
4. Open the Gradio interface link in your browser. For example:
   
Running on local URL:  http://127.0.0.1:7860/
Running on public URL: https://abcde12345.gradio.live 

5. Interact with the chatbot by typing a message and receiving replies.
6. Limit conversation context: Modify the MAX_CONTEXT_LENGTH to manage the memory of past conversations.

## Example Output
User: "What is a healthy breakfast?"

Chatbot: "A healthy breakfast might include whole grains, lean proteins, and fruits. For example, oatmeal with berries and a boiled egg."
