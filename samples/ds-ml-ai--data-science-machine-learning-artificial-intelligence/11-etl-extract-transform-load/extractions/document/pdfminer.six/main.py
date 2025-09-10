"""
python -m venv .venv
source .venv/bin/activate
pip install pdfminer.six
pip install 'pdfminer.six[image]'
pip freeze > requirements.txt

pip install -r requirements.txt
python main.py
"""

from pdfminer.high_level import extract_text

text = extract_text("example.pdf")
print(text)


https://github-readme-stats.vercel.app/api?username=moljac
https://github-profile-trophy.vercel.app/?username=moljac
https://nirzak-streak-stats.vercel.app/?user=moljac
