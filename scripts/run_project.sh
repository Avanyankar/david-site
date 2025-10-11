#!/bin/bash

set -e

echo "=== Запуск проекта ==="

npm run build
./scripts/run_fastapi.sh

echo "Запуск завершён!"