import gradio as gr
import whisper
from translate import Translator
from dotenv import dotenv_values
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings

config = dotenv_values(".env")
# validamos si el archivo .env existe y contiene la clave de API de ElevenLabs
if "ELEVENLABS_API_KEY" not in config:
    raise KeyError("La clave 'ELEVENLABS_API_KEY' no está definida en el archivo .env.")


# Cargar la clave de API de ElevenLabs desde el archivo .env
# Asegúrate de que el archivo .env contenga la línea: ELEVENLABS_API_KEY=tu_clave_aqui
ElevenLabs_API_Key = config["ELEVENLABS_API_KEY"]

def translator(audio_file):
    #proceso:
    # 1. Recibir  el audio grabado por el micrófono
    # 2. Transcribir el audio a texto:
    # para este proceso podemos usar varios metodos
    #     por ejemplo podemos usar:
    #       - assembly AI 
    #       - whisper 
    #     que son servicios que estan en la nube y que disponen de un api.
    #     en este caso voy a usar whisper local https://github.com/openai/whisper
    print(f"Ruta del archivo de audio: {audio_file}")
    print("Cargando modelo de Whisper...")
    try:
        model = whisper.load_model("base")
        result = model.transcribe(audio_file, language="Spanish", fp16=False)
        transcription = result["text"]
    except Exception as e:
        raise gr.Error(
            f"Se ha producido un error transcribiendo el texto: {str(e)}")

    print(f"Texto original: {transcription}")


    # 3. Traducir el texto a otro idioma
    #     para este proceso usamos el api de google translate
    #     que es un servicio que esta en la nube y que dispone de un api. 
    #     Pero atraves de translate ya tenemos este servicio
    print(f"iniciando proceso de tranduccion con la transcripcion: {transcription}")
    try:
        en_transcription = Translator(from_lang="es", to_lang="en").translate(transcription)
    except Exception as e:
        raise gr.Error(f"Error traduciendo  la trascripcion: {str(e)}")
    
    print(f"texto traducido: {en_transcription}")
# 4. Convertir el texto traducido a audio
#     para este proceso podemos usar varios metodos
#     por ejemplo podemos usar:
#       - google text to speech
#       - elevenlabs
#  Para este caso voy a usar elevenlabs que ofrece un tier gratuito tienes que generar tu propio api key
#     y luego lo pones en el archivo .env
    print(f"inicando proceso de conversion de texto a audio con elevenlabs")
    try:
        elClient =  ElevenLabs(api_key=ElevenLabs_API_Key)
        voiceResponse = elClient.text_to_speech.convert(
                                voice_id="21m00Tcm4TlvDq8ikWAM",
                                optimize_streaming_latency="0",
                                output_format="mp3_22050_32",
                                text=en_transcription,
                                model_id="eleven_turbo_v2_5",
                                voice_settings= VoiceSettings(
                                    stability=0,
                                    similarity_boost=1.0,
                                    style=0,
                                    use_speaker_boost=True,
                                )
                            )
    except Exception as e:
        raise gr.Error(f"Error convirtiendo o sintetizando el texto a audio: {str(e)}")

    print(f"Finalizado el proceso de proceso de conversion de texto a audio con elevenlabs")
# 5. Guardar el audio en un archivo
#     en este proceso recibimos un objeto de tipo bytes proveniente de un stream de audio
#  y lo guardamos en un archivo mp3
# directorio para identificar el audio en idioma
    save_file_path = f"en.mp3"

    print(f"iniciando proceso de guardado de audio en el archivo: {save_file_path}")
# y con esta iteracion escibimos el audio en un archivo mp3 en la ruta especificada
    try:
            with open(save_file_path, "wb") as audio_file:
                for chunk in voiceResponse:
                    if chunk:
                        audio_file.write(chunk)

    except Exception as e:
            raise gr.error(f"Error saving audio file: {str(e)}")  

    return save_file_path 

site = gr.Interface(
    fn= translator, 
    inputs=gr.Audio(
        type="filepath"
    ), 
    outputs=[gr.Audio(label ="Audio")],
    title="AI Voice Translator",
    description="Translate your voice to any language you want.",
    theme="default")

site.launch()