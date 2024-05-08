# Need to install the MiniGPT-4 dependencies
pip install -r requ.txt

# Need to install the llama3 weights into MiniGPT-4/models/Meta-Llama-3-8B-Instruct
git clone https://github.com/meta-llama/llama3.git
cd llama3
bash download.sh
# Should give te link for model downloading
# Select 8B-Instruct
cd ..
mkdir models
cd models
# Download the checkpoint from here https://drive.google.com/file/d/1aVbfW7nkCSYx99_vCRyP1sOlQiWVSnAl/view

# Finetune model (minigptv2 with llama3)
python3 train.py --cfg-path train_configs/minigptv2_finetune_llama3.yml
