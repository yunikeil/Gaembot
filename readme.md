# Gaembot

## Описание проекта

Проект Gaembot - это бот для Discord, созданный в рамках проекта по изучению командной работы. Бот предназначен для игры в настольные игры, такие как 2048, крестики-нолики и шашки.

## Установка

Для установки необходимо выполнить следующие команды:

```shell-session
# Для Windows
> python -m venv Venv 
> Venv\Scripts\Activate.ps1
> pip install -r requrements.txt
> python .\main.py
```

```shell-session
# Для Linux
> python3.10 -m venv Venv 
> source Venv/bin/activate
> pip install -r requrements.txt
> python3.10 .\main.py
```

## Зависимости

Бот использует следующие зависимости:

- nextcord
- aeval
- pillow
- sphinx
-requests

## Ресурсы

Для разработки бота были использованы следующие ресурсы:

- https://github.com/nextcord/nextcord
- https://docs.nextcord.dev/en/stable/ext/commands/api.html#cogs
- https://discord.com/developers/docs/
- https://discord.com/developers/applications
- https://discord.com/api/oauth2/