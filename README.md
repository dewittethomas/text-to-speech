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

speak("hello", lang="en")
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

"text" is the text, and "lang" is an IETF language tag such as en or pt-br, "slow" is the option if it has to be read slow or not.