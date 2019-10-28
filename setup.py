import setuptools

with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Thomas Dewitte",
    author_email="thomasdewittecontact@gmail.com",

    name='text_to_speech',
    version='1.0.9',
    license="MIT",
    url='https://github.com/dewittethomas/text-to-speech',
    python_requires='>= 2.7',
    
    description='A simple text to speech engine',
    long_description=README,
    long_description_content_type="text/markdown",

    package_dir={"text_to_speech": "text_to_speech"},
    install_requires=["playsound>=1.2.2", "gTTS>=2.0.4"],
    
    packages=setuptools.find_packages(),

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)