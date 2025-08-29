import torch
import os

from safetensors import safe_open
from safetensors.torch import save_file
from typing import Any, Dict, List, Optional, Set, Tuple, Union


# https://huggingface.co/docs/safetensors/en/api/torch

def write_all_tensors(
    filename: str,
    tensors: Dict[str, torch.Tensor],
    metadata: Optional[Dict[str, str]] = None,
) -> str:

    save_file(tensors, filename)

    # Optionally, you can return the filename or any other relevant information
    return filename

def read_all_tensors(
    filename: str,
    metadata: Optional[Dict[str, str]] = None,
) -> Dict[str, torch.Tensor]:

    tensors = {}
    with safe_open("model.safetensors", framework="pt", device="cpu") as f:
        for key in f.keys():
            tensors[key] = f.get_tensor(key)
    return tensors
    
    # return api.load_file(filename, metadata=metadata)
