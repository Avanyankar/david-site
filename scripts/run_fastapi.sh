#!/bin/bash

set -e

echo "=== Запуск fastapi ==="

source venv/bin/activate
python3 src/main.py

echo "Запуск завершён!"