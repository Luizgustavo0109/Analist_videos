import os
from flask import Flask, render_template, request, redirect, url_for, flash
from googleapiclient.discovery import build
import google.generativeai as genai
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv(".env")

# Configuração da API Gemini e YouTube
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Para gerenciar mensagens flash

def fetch_video_details(video_id):
    """Busca título e descrição de um vídeo do YouTube."""
    request = youtube.videos().list(
        part="snippet,contentDetails", id=video_id
    )
    response = request.execute()
    if not response["items"]:
        raise Exception("Vídeo não encontrado")
    video_data = response["items"][0]["snippet"]
    return video_data["title"], video_data["description"]

def analyze_with_gemini(prompt):
    """Faz análise usando o modelo Gemini."""
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(prompt)
    return ''.join([stream.text for stream in response if stream.text])

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video_url = request.form.get("video_url")
        try:
            video_id = video_url.split("v=")[-1].split("&")[0]
            title, description = fetch_video_details(video_id)
            prompt = (
                f"Analise o seguinte vídeo do YouTube:\n\n"
                f"**Título:** {title}\n"
                f"**Descrição:** {description}\n\n"
                f"Faça um resumo deste vídeo e identifique o tema central."
            )
            analysis = analyze_with_gemini(prompt)
            return render_template("index.html", analysis=analysis, video_url=video_url)
        except Exception as e:
            flash(f"Erro: {e}")
            return redirect(url_for("index"))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)