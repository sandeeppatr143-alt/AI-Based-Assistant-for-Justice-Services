import gradio as gr

def legal_bot(message, history):
    responses = {
        "theft": "Section 379 — Whoever commits theft shall be punished with imprisonment which may extend to three years, or with fine, or both.",
        "force": "Section 390 — When theft is accompanied by violence, it is robbery. Punishment may extend to ten years with fine.",
        "murder": "Section 302 — Whoever commits murder shall be punished with death or imprisonment for life, and shall also be liable to fine.",
    }
    for key in responses:
        if key in message.lower():
            return responses[key]
    return "I'm JusticeMate — please ask me about IPC sections or legal terms!"

def user_interaction(message, history):
    reply = legal_bot(message, history)
    return reply, reply  # text and voice output

with gr.Blocks(title="JusticeMate: Legal Chatbot") as app:
    gr.Markdown("## ⚖️ JusticeMate — Your Legal Chatbot with Voice Output")
    chatbot = gr.Chatbot(label="JusticeMate Chat")
    msg = gr.Textbox(placeholder="Ask me about legal topics...")
    audio = gr.Audio(label="Voice Output", type="filepath")

    msg.submit(user_interaction, [msg, chatbot], [chatbot, audio])

app.launch()
