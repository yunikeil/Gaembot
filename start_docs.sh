
cd /root/vscode/python/Gaembot/Docs/docs_sphinx/_build/html
python3 -m http.server 80 --bind 45.152.113.189 &> /root/vscode/python/Gaembot/http_output.txt & > /root/vscode/python/Gaembot/http_proc_num.txt
disown %
jobs -l 
# ps aux
