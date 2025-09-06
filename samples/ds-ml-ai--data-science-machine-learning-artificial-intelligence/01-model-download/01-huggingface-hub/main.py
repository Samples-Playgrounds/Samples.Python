"""
rm -fr .venv
python -m venv .venv
source .venv/bin/activate
pip install "huggingface_hub[hf_transfer]"  joblib
pip freeze > requirements.txt

pip install "huggingface_hub[hf_transfer]"
HF_HUB_ENABLE_HF_TRANSFER=1 hf download ...
"""

import api_huggingface_hub_model_snapshot_download as api


#model_id="lmsys/vicuna-13b-v1.5"
#api.download_model_to_folder(
#                                repo_id=model_id,
#                                local_dir="vicuna-hf",
#                                local_dir_use_symlinks=False,
#                                revision="main"
#                            )

model_id="CompVis/stable-diffusion-v-1-4-original"
file = api.download_hf_model_to_folder(
                                        repo_id=model_id,
                                        file_name="sd-v1-4.ckpt",
                                        use_auth_token=False
                                    )

print(file)