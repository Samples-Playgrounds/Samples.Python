from huggingface_hub import snapshot_download
from huggingface_hub import hf_hub_download

import joblib

import os
from pathlib import Path

import json
import datetime
import time
from time import perf_counter
from time import perf_counter_ns

def download_hf_model_repo_to_folder_with_snapshot_download(
                                                                repo_id: str,
                                                                local_dir:".hwaifs/models/",
                                                                local_dir_use_symlinks=False,
                                                                revision="main"
                                                            ) -> []:
    """
    https://huggingface.co/docs/huggingface_hub/en/guides/download#download-an-entire-repository

    https://huggingface.co/docs/huggingface_hub/main/en/package_reference/file_download#huggingface_hub.snapshot_download

    '$HOME/.cache/huggingface/hub/models--{repo_owner}--{repo_name}/snapshots/'

    """


    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------

    directory = f".hwaifs/models/{repo_id}"
    Path(directory).mkdir(parents=True, exist_ok=True)

   snapshot_download(
                        repo_id=repo_id,
                        local_dir=f"{local_dir}{repo_id}",
                        local_dir_use_symlinks=local_dir_use_symlinks,
                        revision=revision
                    )

    #---------------------------------------------------------------------------
    time_stop_1 = time.time()
    time_total_1 = time_stop_1 - time_start_1
    time_stop_2 = perf_counter()
    time_total_2 = time_stop_2 - time_start_2
    time_stop_3 = perf_counter_ns()
    time_total_3 = (time_stop_3 - time_start_3) / 1_000_000_000

    times = {
        "function_method_name" : "extract_text_to_file_from_any_document",
        "time_start_1": time_start_1,
        "time_end_1": time_stop_1,
        "time_total_1": time_total_1,
        "time_start_2": time_start_2,
        "time_end_2": time_stop_2,
        "time_total_2": time_total_2,
        "time_start_3": time_start_3,
        "time_end_3": time_stop_3,
        "time_total_3": time_total_3,
    }

    timestamp = datetime.datetime.now().isoformat().replace(":", "-")
    with open(f"{directory}/performance-data-{timestamp}.python.json", "w") as f:
        f.write(json.dumps(times, indent=4))
    #---------------------------------------------------------------------------

    return


def download_hf_file_from_repo_to_folder(
                                    repo_id: str,
                                    file_name: str,
                                    use_auth_token: bool
                                ) -> []:

    """
    https://huggingface.co/docs/huggingface_hub/main/en/package_reference/file_download#download-a-single-file
    """
    #---------------------------------------------------------------------------
    time_start_1 = time.time()
    time_start_2 = perf_counter()
    time_start_3 = perf_counter_ns()
    #---------------------------------------------------------------------------

    directory = f"{source}.hwaifs/models/{repo_id}"
    Path(directory).mkdir(parents=True, exist_ok=True)

    downloaded_model_path = hf_hub_download(
                                                repo_id=repo_id,
                                                filename=f"{file_name}",
                                                use_auth_token=use_auth_token
                                            );


    # save to file
    with open(f"{directory}/content.txt", "w") as f:
        f.write(result_txt)

    #---------------------------------------------------------------------------
    time_stop_1 = time.time()
    time_total_1 = time_stop_1 - time_start_1
    time_stop_2 = perf_counter()
    time_total_2 = time_stop_2 - time_start_2
    time_stop_3 = perf_counter_ns()
    time_total_3 = (time_stop_3 - time_start_3) / 1_000_000_000

    times = {
        "function_method_name" : "extract_text_to_file_from_any_document",
        "time_start_1": time_start_1,
        "time_end_1": time_stop_1,
        "time_total_1": time_total_1,
        "time_start_2": time_start_2,
        "time_end_2": time_stop_2,
        "time_total_2": time_total_2,
        "time_start_3": time_start_3,
        "time_end_3": time_stop_3,
        "time_total_3": time_total_3,
    }

    timestamp = datetime.datetime.now().isoformat().replace(":", "-")
    with open(f"{directory}/performance-data-{timestamp}.python.json", "w") as f:
        f.write(json.dumps(times, indent=4))
    #---------------------------------------------------------------------------

    return downloaded_model_path
