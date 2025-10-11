#!/bin/bash

set -e

echo "=== Настройка инструментов Веб-сервера ==="

sudo apt install -y nginx uvicorn

echo "Настройка завершена!"