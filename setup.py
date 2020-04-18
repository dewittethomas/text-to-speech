import setuptools

with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Thomas Dewitte",
    author_email="thomasdewittecontact@gmail.com",

    name='text_to_speech',
    version='1.2.2',
    license="MIT",
    url='https://github.com/dewittethomas/text-to-speech',
    python_requires='>= 3.5',
    
    description='A simple text to speech engine',
    long_description=README,
    long_description_content_type="text/markdown",

    package_dir={"text_to_speech": "text_to_speech"},
    install_requires=["playsound>=1.2.2", "gTTS>=2.0.4", "mutagen>=1.44.0"],
    
    packages=setuptools.find_packages(),

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ]
)