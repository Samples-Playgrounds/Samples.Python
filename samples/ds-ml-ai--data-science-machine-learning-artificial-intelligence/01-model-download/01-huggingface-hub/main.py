"""
deactivate
rm -fr .venv/ __pycache__/
rm *.pyc
"""

"""
python -m venv .venv
source .venv/bin/activate
pip install "huggingface_hub[hf_transfer]"
pip install joblib
pip install timer
pip install codetiming
pip freeze > requirements.txt
"""

"""
pip install -r requirements.txt
python main.py
"""

"""
HF_HUB_ENABLE_HF_TRANSFER=1 hf download
"""

# https://huggingface.co/models?search=csharp
# https://huggingface.co/models?sort=created&search=python
# https://huggingface.co/models?p=1&sort=created&search=android
models = [
    "Alexis-Az/Qwen-2.5-Coder-7B-4bit-CSharp-Alpaca-Instruct",
    "Alexis-Az/Qwen-2.5-Coder-7B-4bit-CSharp-Alpaca-Code-ORPO-LoRA",
    "Alexis-Az/Qwen-2.5-Coder-7B-4bit-CSharp",
    "Safurai/Safurai-Csharp-34B",
    "Safurai/Safurai-Csharp-34B-GGUF",
]
import api_huggingface_hub_model_snapshot_download as api

#model_id="lmsys/vicuna-13b-v1.5"
#api.download_model_to_folder(
#                                repo_id=model_id,
#                                local_dir="vicuna-hf",
#                                local_dir_use_symlinks=False,
#                                revision="main"
#                            )

# model_id="CompVis/stable-diffusion-v-1-4-original"
# file = api.download_hf_model_to_folder(
#                                         repo_id=model_id,
#                                         file_name="sd-v1-4.ckpt",
#                                         use_auth_token=False
#                                     )


def main():
   for model in models:
      print(f"huggingface_hub <- downloadin = {model}")
      result_txt = api.download_model_repo_to_folder_with_snapshot_download(
                                                                            model,
                                                                            local_dir=".hwaifs/models/"
                                                                        )

if __name__ == '__main__':
    main()
