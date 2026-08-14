#!/usr/bin/env bash
apt-get update
apt-get install -y libgl1-mesa-glx libglib2.0-0

pip install --upgrade pip
pip install -r requirements.txt

python -c "from paddleocr import PaddleOCR; PaddleOCR(lang='ru')"