import torch
import gradio as gr
from transformers import pipeline

# text_summary=pipeline(task="summarization",model="sshleifer/distilbart-cnn-12-6")
model_path=("../Models/models--sshleifer--distilbart-cnn-12-6/snapshots/a4f8f3ea906ed274767e9906dbaede7531d660ff")
text_summary= pipeline(
    task="summarization",
    model=model_path,
    torch_dtype=torch.float16
)



def summary(input_text,summary_type):

    if summary_type == "Short":
        max_len = 50
        min_len = 20

    elif summary_type == "Medium":
        max_len = 100
        min_len = 40

    else:  # Detailed
        max_len = 200
        min_len = 80

    output=text_summary(

        input_text,
        max_length=max_len,
        min_length=min_len,
        do_sample=False
    )
    return output[0]['summary_text']

gr.close_all()



demo = gr.Interface(
    fn=summary,
    inputs=[
        gr.Textbox(lines=10, label="Input Text"),
        gr.Dropdown(
            choices=["Short", "Medium", "Detailed"],
            value= "Medium",
            label="Summary Type",
        )
            ],
    outputs=gr.Textbox(label="Summary"),
    title="AI Text Summarizer",
    description="Paste a long text and generate a concise summary."
)


demo.launch()

