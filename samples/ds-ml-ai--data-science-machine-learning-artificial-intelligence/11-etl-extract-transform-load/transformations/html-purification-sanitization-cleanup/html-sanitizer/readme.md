

https://pypi.org/project/html-sanitizer/



https://github.com/matthiask/html-sanitizer/

pip install html-sanitizer


from html_sanitizer import Sanitizer
sanitizer = Sanitizer()  # default configuration
sanitizer.sanitize('<span style="font-weight:bold">some text</span>')
'<strong>some text</strong>'