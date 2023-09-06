# Text-to-Speech

A versatile and user-friendly Python Text-to-Speech engine with customizable options.

[![PyPi Version](https://img.shields.io/pypi/v/text-to-speech.svg)](https://pypi.org/project/text-to-speech/)
[![MIT License](https://img.shields.io/pypi/l/text-to-speech.svg)](https://github.com/dewittethomas/text-to-speech/blob/master/LICENSE)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Parameters](#parameters)
  - [Example with Slow Speech](#example-with-slow-speech)
- [Contributing](#contributing)
- [License](#license)
  
## Installation

You can install the `text-to-speech` module using pip:

```bash
pip install text-to-speech
```

## Usage

### Basic Usage

You can use this module to convert text to speech and save it as an audio file. Here's a basic example:

```python
from text_to_speech import save

text = "Hello, World!"
language = "en"  # Specify the language (IETF language tag)
output_file = "hello_world.mp3"  # Specify the output file (only accepts .mp3)

save(text, language, file=output_file)
```

### Parameters

Here are the available parameters for the `save` function:

| Parameter     | Description                                            | Default Value   |
|---------------|--------------------------------------------------------|-----------------|
| `text`        | The text to be converted to speech.                    |                 |
| `language`    | The language (IETF language tag) to use for speech synthesis. | "en"         |
| `slow`        | Set to `True` if you want the text to be read more slowly. | `False`         |
| `file`        | The name of the output audio file. Only accepts .mp3 format. | "speech.mp3"   |
| `lang_check`  | Set to `True` to check the text for language errors.   | `False`         |

### Example with Slow Speech

You can make the speech slower by setting the `slow` parameter to `True`:

```python
from text_to_speech import save

text = "This is a slow speech example."
language = "en"
output_file = "slow_speech.mp3"

save(text, language, slow=True, file=output_file)
```

## Contributing

Contributions to this project are welcome. If you have any improvements or bug fixes, please submit a pull request.

## License

This project is licensed under the MIT License.