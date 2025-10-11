#!/bin/bash

set -e

echo "Выберите скрипт:"
echo "1) Запуск проекта"
echo "2) Запуск fastapi"
echo "3) Настройка системы"
echo "4) Настройка Frontend инструментов"
echo "5) Настройка инструментов Веб-сервера"
echo "6) Настройка Python"
echo "7) Полная настройка"
echo "8) Посмотреть установленные версии"

read -p "Введите номер: " choice

case $choice in
    1) ./scripts/run_project.sh ;;
    2) ./scripts/run_fastapi.sh ;;
    3) ./scripts/setup_system.sh ;;
    4) ./scripts/setup_frontend.sh ;;
    5) ./scripts/setup_webserver.sh ;;
    6) ./scripts/setup_python.sh ;;
    7) ./scripts/setup.sh ;;
    8) ./scripts/versions.sh ;;
    *) echo "Ошибка ввода" ;;
esac