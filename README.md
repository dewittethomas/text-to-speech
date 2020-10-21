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

```python
import text_to_speech as speech

speech.speak("Hello", lang="en")
```

"text" is the text,
and "lang" is an IETF language tag such as en or pt-br.