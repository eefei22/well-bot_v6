# audio_raw

folder stores downloaded raw audio datasets used for training and inference.
To download them again, use the scripts in `/scripts/`:
- `download_cremaD.py`
- `download_ravdess.py`
- `download_TESS.py`

```
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8008

Get-ChildItem -Path "$env:USERPROFILE" -Recurse -Filter "pyvenv.cfg" -ErrorAction SilentlyContinue
```


# =========== Mallam model  ===========
# from transformers import AutoModelForCausalLM, AutoTokenizer
# _tok_mallam = AutoTokenizer.from_pretrained("mesolitica/mallam-5B-4096")
# _model_mallam = AutoModelForCausalLM.from_pretrained(
#     "mesolitica/mallam-5B-4096", 
#     device_map="auto"
# )