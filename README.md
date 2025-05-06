# AI Voice Translator

Este proyecto permite traducir el audio grabado por un micrófono en tiempo real utilizando la API de Whisper para transcripción y ElevenLabs para convertir el texto traducido a audio. 

## Requisitos

- Python 3.x
- Instalación de las siguientes dependencias:
  - `gradio`
  - `whisper`
  - `translate`
  - `dotenv`
  - `elevenlabs`

### Instalación de dependencias

Puedes instalar las dependencias necesarias ejecutando:

```bash
pip pip install -r requirements.txt
```

## Configuración

Para utilizar el servicio, necesitarás obtener una clave de API de **ElevenLabs**. Puedes hacerlo de la siguiente manera:

1. Regístrate en [ElevenLabs](https://elevenlabs.io).
2. Obtén tu clave API y guárdala en un archivo `.env` dentro de tu directorio de proyecto.

El archivo `.env` debe tener el siguiente formato:

```
ELEVENLABS_API_KEY=tu_clave_aqui
```

## Cómo usar

1. Graba un mensaje usando tu microfono , o cualquier otro archivo de audio en formato `.mp3`, `.wav` compatible con Gradio.
2. El sistema transcribirá el audio usando **Whisper** (modelo local).
3. Luego, traducirá el texto a inglés usando la API de **Translate**.
4. Finalmente, convertirá el texto traducido a audio usando **ElevenLabs** y lo guardará en un archivo de salida.

### Ejecutar la aplicación

Para ejecutar la aplicación, simplemente corre el siguiente comando en tu terminal:

```bash
python -u "main.py"
```
Abre el navegador en la URL proporcionada (por defecto: http://127.0.0.1:7860).

Esto abrirá la interfaz de **Gradio** en tu navegador donde podrás grabar o subir un archivo de audio y ver el proceso de traducción y conversión a voz en acción.

## Estructura del Código

1. **Cargar el modelo de Whisper:** El código utiliza el modelo de transcripción de Whisper para convertir el audio en texto.
2. **Traducción del texto:** Usando la API de Translate, el texto transcrito se traduce al inglés.
3. **Conversión de texto a voz:** Se utiliza ElevenLabs para convertir el texto traducido a audio.
4. **Guardado del archivo de audio:** El archivo de audio resultante se guarda como un archivo `.mp3`.

## Archivos

- **.env**: Debe contener tu clave de API de ElevenLabs.
- **main.py**: El archivo principal con el código de la aplicación.
- **en.mp3**: El archivo de audio traducido generado por el sistema.

## Notas

- Asegúrate de que tu archivo `.env` contenga correctamente la clave API de ElevenLabs.
- El servicio está basado en la nube, por lo que necesitarás una conexión a internet para las API de Whisper, Translate y ElevenLabs.
- Puedes modificar la configuración para soportar otros idiomas y personalizar los parámetros de la voz generada por ElevenLabs.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE`.

---

Gracias por usar el **AI Voice Translator**. ¡Disfruta de la traducción de voz automatizada!
