# text-to-speech

[![npm](https://img.shields.io/pypi/v/text-to-speech.svg)](https://pypi.org/project/text-to-speech/)

This is a simple text to speech engine with some customizable options.

## Installation

Run the following to install:

```console
pip install text-to-speech
```

## Usage

### Speak

```python
speak()
```

Params:

```
Text: String ? The text to be read.
Language: String ? The language (IETF language tag) to read the text in.
Slow: Boolean ? Reads text more slowly.
Save: Boolean ? If the file has to be saved or not.
File: String ? If save == true, the file name to save the mp3 to.
```

Demo:

```python
from text_to_speech import speak

speak("Hello World", "en", save=True, file="Hello-World.mp3")
```

# License
[MIT](https://github.com/dewittethomas/text-to-speech/blob/master/LICENSE)