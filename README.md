# text-to-speech

[![npm](https://img.shields.io/pypi/v/text-to-speech.svg)](https://pypi.org/project/text-to-speech/)

A simple text to speech engine

## Installation
To install the package run this command:

```bash
pip install text-to-speech
```

## Usage

### Speak

Write ‘hello’ in English

```python
from text_to_speech import speak 

speak("hello")
```

Write ‘bonjour’ in French

```python
from text_to_speech import speak 

speak("bonjour", lang="fr")
```

Write ‘hello’ in English slow

```python
from text_to_speech import speak 

speak("hello", lang="en", slow=True)
```

Write ‘hello’ in English and save the file as "speech.mp3"
```python
from text_to_speech import speak 

speak("hello", lang="en", save=True)
```

Write ‘hello’ in English and save the file as "hello.mp3"
```python
from text_to_speech import speak 

speak("hello", lang="en", save=True, file="hello.mp3")
```


"text" is the text, and "lang" is an IETF language tag such as en or pt-br, "slow" is the option if it has to be read slow or not, "save" is if it has to be saved or not by default it is saved as "speech.mp3", "file" is if "save" = True you could choose a specific path or filename.