#!/bin/bash

set -e

echo "=== Настройка ==="

./scripts/setup_system.sh
./scripts/setup_frontend.sh
./scripts/setup_webserver.sh
./scripts/setup_python.sh
./scripts/versions.sh

echo "Настройка завершена!"