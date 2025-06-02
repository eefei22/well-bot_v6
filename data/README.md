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

Get-ChildItem -Path "$env:USERPROFILE" -Recurse -Filter "pyvenv.cfg" -ErrorAction SilentlyContinue
```