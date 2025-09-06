from huggingface_hub import snapshot_download
from huggingface_hub import hf_hub_download
import joblib

def download_model_to_folder(
                    repo_id: str, 
                    local_dir:"vicuna-hf",
                    local_dir_use_symlinks=False,
                    revision="main"
                    ) -> []:

    snapshot_download(
                        repo_id=repo_id,
                        local_dir=local_dir,
                        local_dir_use_symlinks=local_dir_use_symlinks,
                        revision=revision
                    )


from huggingface_hub import hf_hub_download

def download_hf_model_to_folder(
                                repo_id: str, 
                                file_name: str,
                                use_auth_token: bool
                                ) -> []:

    downloaded_model_path = hf_hub_download(
                                            repo_id=repo_id,
                                            filename=file_name,
                                            use_auth_token=use_auth_token
                                            ); 
    return downloaded_model_path
