#!/bin/bash

set -e

echo "=== Настройка системы ==="

sudo apt update && sudo apt upgrade -y
sudo apt install -y curl wget build-essential

echo "Настройка завершена!"