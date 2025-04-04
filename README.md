# 🧠 MindScribe — Transcriptor y Analizador de Sesiones de Terapia

MindScribe es una herramienta automatizada que convierte grabaciones de sesiones de terapia en texto transcrito y luego genera un resumen con insights clave utilizando inteligencia artificial. Ideal para psicólogos, terapeutas o investigadores que desean documentar y analizar sesiones fácilmente.

## 🚀 Características

- 🎥 Convierte archivos `.mp4` en `.mp3`
- ✍️ Transcribe el audio usando **Whisper** (modelo base)
- 🧠 Genera un resumen profesional con **GPT-4**
- 🗂️ Organiza automáticamente transcripciones y resúmenes por sesión
- ✅ Listo para ejecutarse desde la terminal con una sola función

## 📁 Estructura del Proyecto

MindScribe/
- sesiones_mp4/          # Carpeta con tus videos .mp4
- mp3_convertidos/       # Audios generados en .mp3
- transcripciones/       # Textos transcritos
- resumenes/             # Archivos .md con el resumen de cada sesión
- config.py              # Contiene la clave OPENAI_API_KEY
- main.py  # Script principal
- .gitignore

## Requisitos

- Python 3.8+
- [ffmpeg](https://ffmpeg.org/) (necesario para MoviePy)
- Cuenta y API Key de OpenAI

## 📦 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/tuusuario/MindScribe.git
cd MindScribe
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Asegúrate de tener ffmpeg instalado:
```bash
brew install ffmpeg  # macOS
sudo apt install ffmpeg  # Linux
```

4. Crea un archivo .env:

```bash
# .env
OPENAI_API_KEY = "tu_api_key_aqui"
```

5. Coloca tus videos .mp4 dentro de la carpeta sesiones_mp4/

## Cómo usar?

Ejecutar

```bash
python main.py
```

Esto procesará todos los .mp4 de la carpeta sesiones_mp4, generando:
- El .mp3 del audio
- La transcripción en .txt
- Un resumen profesional en .md

## ✨ Ejemplo de resumen generado

Resumen de la sesión: paciente_001

1. 🧠 Temas tratados: ansiedad laboral, miedo al rechazo.
2. 😢 Emociones predominantes: frustración, inseguridad.
3. 🔄 Patrones observados: pensamientos negativos recurrentes.
4. 💡 Insights: reconoce su tendencia a exigirse demasiado.
5. 🛠️ Para trabajar: gestión emocional, límites saludables.

## 🛡️ Licencia
Este proyecto está bajo la Licencia MIT. Puedes usarlo, modificarlo o compartirlo con fines personales o profesionales.
