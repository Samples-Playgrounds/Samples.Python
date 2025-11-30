# `deepdoctection`


*   https://github.com/deepdoctection/deepdoctection

```
pip install gradio_client   # requires Python >= 3.10 
```

```python
from gradio_client import Client, handle_file

if __name__ == "__main__":

    client = Client("deepdoctection/deepdoctection")
    result = client.predict(
        img=handle_file('/local_path/to/dir/file_name.jpeg'),  # accepts image files, e.g. JPEG, PNG
        pdf=None,   
        max_datapoints = 2,
        api_name = "/analyze_image"
    )
    print(result)
```

from gradio_client import Client, handle_file

if __name__ == "__main__":

    client = Client("deepdoctection/deepdoctection")
    result = client.predict(
        img=None,
        pdf=handle_file("/local_path/to/dir/your_doc.pdf"),
        max_datapoints = 2, # increase to process up to 9 pages
        api_name = "/analyze_image"
    )
    print(result)



pip install transformers
pip install python-doctr==0.10.0 # If you use Python 3.10 or higher you can use the latest version.
pip install deepdoctection

pip install tensorpack
pip install deepdoctection
pip install "numpy>=1.21,<2.0" --upgrade --force-reinstall  # because TF 2.11 does not support numpy 2.0 
pip install "python-doctr==0.9.0"


pip install deepdoctection[pt]

pip install deepdoctection[tf]

https://pypi.org/project/deepdoctection/0.15/

pip install deepdoctection==0.15

https://konfuzio.com/en/deepdoctection/

