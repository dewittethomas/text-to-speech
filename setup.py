from setuptools import setup, find_packages

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
    name = "text_to_speech",
    version = "1.5.0",
    license = "MIT",
    url = "https://github.com/dewittethomas/text-to-speech",
    
    description = 'A simple text to speech engine',
    long_description = long_description,
    long_description_content_type = "text/markdown",

    package_dir = {"text_to_speech": "text_to_speech"},
    install_requires = [
        "playsound>=1.2.2", 
        "gTTS>=2.0.4"
    ],

    packages = find_packages(),

    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
    ],

    keywords = 'sound playsound music wave wav mp3 media song play audio'
)