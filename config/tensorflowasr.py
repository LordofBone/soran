from pathlib import Path

model_path = Path(__file__).parent.parent / f"models"
vocab_path = Path(__file__).parent.parent / model_path / f"conformer"
file_path = Path(__file__).parent.parent / f"audio"
config_path = Path(__file__).parent.parent / f"config"

model = str(model_path / "conformer/latest.h5")
config_file = str(config_path / "config.yml")
audio_file = str(file_path / "recording.wav")
subwords_file = str(vocab_path / "conformer.subwords")

beam_width = None
timestamp = None
device = 0
cpu = True
sentence_piece = False
