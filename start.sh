
cd /root/vscode/python/Gaembot/
source /root/vscode/python/Gaembot/Venv/bin/activate
/root/vscode/python/Gaembot/Venv/bin/python3.10 /root/vscode/python/Gaembot/src/main.py &> /root/vscode/python/Gaembot/gaembot.txt &
disown %
jobs -l 



