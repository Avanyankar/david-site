#!/bin/bash

set -e

echo "=== Настройка webserver ==="

sudo apt install -y nginx uvicorn

echo "Настройка завершена!"