import whisper
from openai import OpenAI
import os
from moviepy import VideoFileClip  # ✅ MoviePy actualizado
from config import OPENAI_API_KEY

# Inicializa cliente de OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

# Función para convertir mp4 a mp3
def convertir_a_mp3(ruta_mp4, ruta_salida_mp3):
    video = VideoFileClip(ruta_mp4)
    video.audio.write_audiofile(ruta_salida_mp3)

# Función para transcribir audio
def transcribir_audio(ruta_audio):
    modelo = whisper.load_model("base")
    resultado = modelo.transcribe(ruta_audio)
    return resultado["text"]

# Función para generar resumen con GPT
def generar_resumen(texto_transcrito):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": (
                    "Eres un psicólogo clínico que ayuda a analizar sesiones de terapia. "
                    "Tu tarea es extraer insights útiles, identificar patrones emocionales o conductuales, "
                    "y generar un resumen profesional que pueda ayudar en futuras sesiones."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Analiza la siguiente transcripción de una sesión de terapia y responde lo siguiente:\n\n"
                    f"1. 🧠 Principales temas tratados\n"
                    f"2. 😢 Emociones expresadas o subyacentes\n"
                    f"3. 🔄 Patrones de comportamiento o pensamientos repetitivos\n"
                    f"4. 💡 Insights relevantes sobre el progreso del paciente\n"
                    f"5. 🛠️ Posibles recomendaciones o puntos para trabajar en futuras sesiones\n\n"
                    f"Transcripción:\n{texto_transcrito}"
                )
            }
        ]
    )
    return response.choices[0].message.content


# Función principal
def procesar_sesiones_desde_mp4():
    # Crea carpetas si no existen
    os.makedirs("mp3_convertidos", exist_ok=True)
    os.makedirs("transcripciones", exist_ok=True)
    os.makedirs("resumenes", exist_ok=True)

    # Procesa cada archivo mp4 en la carpeta
    archivos_video = [f for f in os.listdir("sesiones_mp4") if f.endswith(".mp4")]

    for archivo in archivos_video:
        nombre_base = os.path.splitext(archivo)[0]
        ruta_mp4 = os.path.join("sesiones_mp4", archivo)
        ruta_mp3 = os.path.join("mp3_convertidos", f"{nombre_base}.mp3")

        print(f"\n🎥 Procesando video: {archivo}")

        # 1. Convertir a MP3
        convertir_a_mp3(ruta_mp4, ruta_mp3)

        # 2. Transcribir audio
        print("📝 Transcribiendo...")
        texto = transcribir_audio(ruta_mp3)
        with open(f"transcripciones/{nombre_base}.txt", "w", encoding="utf-8") as f:
            f.write(texto)

        # 3. Generar resumen
        print("🧠 Generando resumen...")
        resumen = generar_resumen(texto)
        with open(f"resumenes/{nombre_base}.md", "w", encoding="utf-8") as f:
            f.write(f"# Resumen de la sesión: {nombre_base}\n\n")
            f.write(resumen)

        print(f"✅ Completado: {archivo}\n")

if __name__ == "__main__":
    procesar_sesiones_desde_mp4()
