# AI Voice Assistant

A Python-based voice assistant that uses speech recognition, text-to-speech, and AI language models to provide conversational AI capabilities.

## Features

- 🎤 Speech recognition using Google Speech Recognition
- 🗣️ Text-to-speech output with adjustable speech rate
- 🤖 AI-powered responses using Ollama's Mistral model
- 💭 Conversation history tracking
- 🔄 Continuous conversation loop

## Requirements

- Python 3.8 or higher
- Microphone for speech input
- Internet connection for speech recognition
- Ollama installed with Mistral model

## Installation

### 1. Clone or Download the Project

```bash
git clone <repository-url>
cd voice-assistant
```

### 2. Install Python Dependencies

```bash
pip install speech-recognition pyttsx3 langchain-community langchain-core langchain-ollama pyaudio
```

### 3. Install Ollama and Mistral Model

**On macOS/Linux:**

```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull the Mistral model
ollama pull mistral
```

**On Windows:**

- Download Ollama from [ollama.ai](https://ollama.ai)
- Install and run: `ollama pull mistral`

### 4. Install System Audio Dependencies

**On macOS:**

```bash
brew install portaudio
```

**On Ubuntu/Debian:**

```bash
sudo apt-get install portaudio19-dev python3-pyaudio
```

**On Windows:**

- PyAudio should install automatically with pip

## Usage

1. **Start the voice assistant:**

   ```bash
   python app.py
   ```

2. **Interact with the assistant:**

   - Wait for "Listening..." prompt
   - Speak your question or command
   - Listen to the AI response
   - Continue the conversation

3. **Exit the assistant:**
   - Say "exit" or "stop" to end the session

## Configuration

### Speech Rate Adjustment

Modify the speech rate in `app.py`:

```python
engine.setProperty('rate', 160)  # Adjust value (default: 160)
```

### Change AI Model

Replace "mistral" with another Ollama model:

```python
llm = OllamaLLM(model="llama2")  # or other models
```

## Troubleshooting

### Common Issues

**"Could not request results" error:**

- Check internet connection
- Verify microphone permissions

**"No module named 'pyaudio'" error:**

```bash
# On macOS
brew install portaudio
pip install pyaudio

# On Linux
sudo apt-get install portaudio19-dev
pip install pyaudio
```

**Ollama connection error:**

- Ensure Ollama is running: `ollama serve`
- Verify Mistral model is installed: `ollama list`

**Microphone not working:**

- Check system microphone permissions
- Test microphone with other applications
- Try different microphone devices

## File Structure

```
voice-assistant/
├── app.py          # Main application file
├── readme.md       # This file
└── requirements.txt # Python dependencies (optional)
```

## Dependencies

- `speech_recognition`: For converting speech to text
- `pyttsx3`: For text-to-speech conversion
- `langchain-community`: For chat message history
- `langchain-core`: For prompt templates
- `langchain-ollama`: For Ollama LLM integration
- `pyaudio`: For microphone audio capture

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE).
