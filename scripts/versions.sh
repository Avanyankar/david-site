#!/bin/bash

set -e

echo "=== Установленные версии ==="

echo "Python: $(python3 --version)"
echo "Node.js: $(node -v)"
echo "npm: $(npm -v)"
if [ -d "node_modules/tailwindcss" ]; then
    TAILWIND_VERSION=$(node -p "require('./node_modules/tailwindcss/package.json').version")
    echo "Tailwind CSS: v$TAILWIND_VERSION"
else
    echo "Tailwind CSS: не найден в node_modules"
fi
echo "Prettier: $(npx prettier --version)"

echo "Вывод завершён!"