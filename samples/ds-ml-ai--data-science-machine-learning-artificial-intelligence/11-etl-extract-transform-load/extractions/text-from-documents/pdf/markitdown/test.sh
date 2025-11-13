#!/bin/bash

deactivate
rm -fr .venv/ __pycache__/
rm *.pyc



python -m venv .venv
source .venv/bin/activate

pip install markitdown[all]
pip install 'markitdown[pdf, docx, pptx]'
pip install 'markitdown[pdf, docx, pptx, xslx, xsl, outlook, audio-transcription, youtube-transcription]'

pip install timer
pip install codetiming

pip freeze > requirements.txt


python main.py
