import os


def check_fw_local_models():
    model_size_list = [
        "tiny",
        "tiny.en",
        "base",
        "base.en",
        "small",
        "small.en",
        "medium",
        "medium.en",
        "large",
        "large-v1",
        "large-v2",
        "large-v3",
    ]
    for i, size in enumerate(model_size_list):
        if os.path.exists(f"tools/asr/models/faster-whisper-{size}"):
            model_size_list[i] = size + "-local"
    return model_size_list


asr_dict = {
    "FunASR": {
        "lang": ["zh"],
        "size": ["large"],
        "path": "funasr_asr.py",
    },
    "Whisper": {
        "lang": ["auto", "zh", "en", "ja"],
        "size": check_fw_local_models(),
        "path": "fasterwhisper_asr.py",
    },
}
