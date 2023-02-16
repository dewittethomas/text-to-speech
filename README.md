# text-to-speech

[![npm](https://img.shields.io/pypi/v/text-to-speech.svg)](https://pypi.org/project/text-to-speech/)

This is a simple text to speech engine with some customizable options.

## Installation

Run the following to install:

```console
pip install text-to-speech
```

## Usage

### Save

```python
save()
```

Params:

```
Text: String ? The text to be read.
Language: String ? The language (IETF language tag) to read the text in.
Slow: Boolean ? Reads text more slowly.
File: String ? The file to save the text to, default is = "speech.mp3", only accepts .mp3.
Lang_check: Boolean ? If the text has to be checked on language errors.
```

Demo:

```python
from text_to_speech import save

save("Hello World", "en", file="Hello-World.mp3")
```

# License
[MIT](https://github.com/dewittethomas/text-to-speech/blob/master/LICENSE)
