"""
rm -fr
python -m venv .venv
source .venv/bin/activate
pip install safetensors torch numpy packaging
pip freeze > requirements.txt

python main.py
"""

from typing import Any, Dict, List, Optional, Set, Tuple, Union
import torch
import api

tensors_data: Dict[str, torch.Tensor] = {
   "weight1": torch.zeros((1024, 1024)),
   "weight2": torch.zeros((1024, 1024))
}

api.write_all_tensors("model.safetensors",tensors_data)

tensors_data = api.read_all_tensors("model.safetensors")

for key in tensors_data.keys():
   print(tensors_data[key])
