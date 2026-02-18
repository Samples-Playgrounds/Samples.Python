

deactivate
rm -fr .venv/ __pycache__/
rm *.pyc

python -m venv .venv
source .venv/bin/activate

pip install shell-gpt
pip install "shell-gpt[litellm]"

export OPENAI_API_KEY='ollama'
export LITELLM_API_KEY=$OPENAI_API_KEY
export DEFAULT_MODEL=ollama/mistral-large:latest
export OPENAI_USE_FUNCTIONS=false
export USE_LITELLM=true
ollama serve &
sgpt --model ollama/mistral-large:latest  "Who are you?"

sgpt --shell
sgpt --shell "echo hello"
sgpt --shell "ls"



pwd
figlet stop
figlet $LIBRARY


$HOME/.config/shell_gpt/.sgptrc

```
API_BASE_URL=http://localhost:11434/v1
DEFAULT_MODEL=ollama/mistral-large:latest
OPENAI_USE_FUNCTIONS=false
USE_LITELLM=true
```