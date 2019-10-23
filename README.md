# text-to-speech

[![npm](https://img.shields.io/pypi/v/text-to-speech.svg)](https://pypi.org/project/text-to-speech/)

A python package that says something of your choice

## Installation
To install the package run this command:

```bash
pip install text-to-speech
```

## Usage

### Speak

```python
speak("text", "language")
```
You have to put a ISO 639-1 Code in the language

Demo:

```python
import text_to_speech as speech

speech.speak("text")
```