import ollama
import gradio as gr
import socket
from typing import Tuple


class CulturalEtiquetteChecker:
    def __init__(self):
        """Initialize the etiquette checker with default model and connection check"""
        self.model = "mistral"  #Model using
        self.check_ollama_connection()  # Verify connection at startup

    def check_ollama_connection(self):
        """Verify Ollama server is reachable by attempting a socket connection"""
        try:
            # Try to establish a connection to Ollama's default port
            sock = socket.create_connection(("127.0.0.1", 11434), timeout=3)
            sock.close()
        except socket.error as err:
            raise ConnectionError(f"Ollama server not reachable: {err}")

    def get_etiquette_advice(self, country: str, situation: str) -> Tuple[str, str]:
        """
        Get cultural advice from Ollama model with proper error handling
        """
        try:
            # Send request to Ollama model
            response = ollama.chat(
                model=self.model,
                messages=[{
                    "role": "user",
                    "content": f"Provide detailed cultural etiquette advice for {country} regarding {situation}. "
                               f"Structure with: 1) Overview 2) Do's 3) Don'ts 4) Phrases 5) Tips"
                }],
                options={'temperature': 0.5}
            )
            return (
                f"## 🌍 {situation.capitalize()} Etiquette in {country.capitalize()}",
                response['message']['content']
            )
        except ollama.ResponseError as e:
            return "⚠️ Error", f"Model error: {e.error}"
        except Exception as e:
            return "⚠️ Error", f"Connection error: {str(e)}"


def format_response(country: str, situation: str) -> Tuple[str, str]:
    """Wrapper function to create checker instance and get advice"""
    checker = CulturalEtiquetteChecker()
    return checker.get_etiquette_advice(country, situation)


# Create Gradio web interface
with gr.Blocks(theme=gr.themes.Soft(), title="Cultural Etiquette Advisor") as app:
    gr.Markdown("# 🌐 Cultural Etiquette Checker")
    gr.Markdown("Get instant advice about customs and polite behavior worldwide")

    # Two-column layout
    with gr.Row():
        # Left column - input controls
        with gr.Column(scale=1):
            country = gr.Textbox(label="Country/Region", placeholder="Japan, Saudi Arabia, Brazil...")
            situation = gr.Textbox(label="Situation", placeholder="business meetings, dining, greetings...")
            btn = gr.Button("Get Cultural Advice", variant="primary")

        # Right column - output display
        with gr.Column(scale=2):
            header = gr.Markdown()
            output = gr.Markdown()

    # Example queries that users can click to try
    examples = gr.Examples(
        examples=[
            ["Japan", "business cards exchange"],
            ["United Arab Emirates", "business attire"],
            ["France", "dining etiquette"]
        ],
        inputs=[country, situation],
        outputs=[header, output],
        fn=format_response,
        cache_examples=True
    )

    # Connect button click to processing function
    btn.click(
        fn=format_response,
        inputs=[country, situation],
        outputs=[header, output]
    )

if __name__ == "__main__":
    try:
        # Verify Ollama connection before launching interface
        checker = CulturalEtiquetteChecker()
        print("✅ Ollama connection verified")
        # Launch web interface on port 7860
        app.launch(server_port=7860, server_name="0.0.0.0")
    except ConnectionError as e:
        # Show error message if Ollama isn't running
        print(f"❌ {str(e)}")
        print("Please ensure Ollama is running:")
        print("1. Open a terminal")
        print("2. Run: ollama serve")