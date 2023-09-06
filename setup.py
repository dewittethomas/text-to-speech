from setuptools import setup, find_packages

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
    name = "text_to_speech",
    version = "1.6.1",
    author = "Thomas Dewitte",
    author_email = "thomasdewittecontact@gmail.com",
    license = "MIT",
    url = "https://github.com/dewittethomas/text-to-speech",
    
    description = 'A versatile and user-friendly Python Text-to-Speech engine',
    long_description = long_description,
    long_description_content_type = "text/markdown",

    package_dir = {"text_to_speech": "text_to_speech"},
    install_requires = [
        "gTTS>=2.3.1"
    ],

    packages = find_packages(),

    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],

    keywords = "sound playsound music wave wav mp3 media song play audio"
)