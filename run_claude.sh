#!/bin/zsh

# Настройки для запуска через OmniRoute
export ANTHROPIC_BASE_URL="http://localhost:20128/v1"
export ANTHROPIC_AUTH_TOKEN="sk-8ee715e2624912c6-ead434-8d436c27"

# Очищаем стандартный ключ во избежание конфликтов
export ANTHROPIC_API_KEY=""

# Указываем OmniRoute как для основной, так и для "быстрой" модели
export ANTHROPIC_MODEL="kr/claude-sonnet-4.5"
export ANTHROPIC_SMALL_FAST_MODEL="kr/claude-sonnet-4.5"

# Отключаем лишний трафик и беты
export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1
export CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1

echo "Starting Claude Code via OmniRoute..."
# Запускаем claude и передаем ему все возможные аргументы скрипта
claude "$@"