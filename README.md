# Vision to Speech

This project is designed to process video frames and generate descriptions using a vision model. It extracts frames at specific intervals, resizes them, and prompts the model to describe what it sees.

## Table of Contents
- [Installation](#installation)
- [Creating and Activating a Virtual Environment](#creating-and-activating-a-virtual-environment)
- [Installing Requirements](#installing-requirements)
- [Downloading Model Weights](#downloading-model-weights)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/sunatte-saad/vision_to_speech.git
cd vision_to_speech
```

---

## Creating and Activating a Virtual Environment

### On Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

### On macOS and Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Installing Requirements

Before installing the requirements, make sure to install the `moondream` package:
```bash
pip install moondream==0.0.5
```

Make sure your virtual environment is activated, then run:
```bash
pip install -r requirements.txt
```

---

## Downloading Model Weights

Download the model weights from the [Moondream GitHub repository](https://github.com/vikhyat/moondream) and place them in the following directory:

```
vision_model
```

Ensure that the downloaded files include:
- `moondream-0_5b-int8.mf`  
- `moondream-2b-int8.mf` (if applicable)

---

## Configuration

Update the following parameters in the configuration section of your main script:

```python
MODEL_PATH = r"vision_model\moondream-0_5b-int8.mf" # or replace by "vision_model\moondream-2b-int8.mf"
FRAME_INTERVAL = 120
MAX_FRAMES = 5
RESIZE_DIM = (640, 360)

PROMPT = "what do you see?"
```

> **Tip:** Ensure that the `MODEL_PATH` points to the correct model file you wish to use.

---

## Usage

Run the main script with:
```bash
python video_input.py
```

---

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
