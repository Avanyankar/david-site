#!/bin/bash

set -e

echo "=== Настройка frontend ==="

curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -
sudo apt install -y nodejs
npm install -D tailwindcss
npm install -D prettier prettier-plugin-tailwindcss

echo "Настройка завершена!"