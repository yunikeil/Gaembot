#!/bin/bash

find . -maxdepth 1 -type f -name '[0-9]*.last' -exec rm {} \;
rename 's/([0-9]+)/$1.last/' *

source Venv/bin/activate
python3 main.py &> temp_output.txt &
sleep 1  # Добавляем небольшую задержку для уверенности, что процесс успел запуститься
pid=$(pgrep -f "python3 main.py")

# Получаем текущее время в секундах с начала эпохи Unix
current_time=$(date +%s)

# Получаем список PID-ов, которые соответствуют процессу "python3 main.py"
pids=($(pgrep -f "python3 main.py"))

# Цикл для обработки каждого PID-а
for pid in "${pids[@]}"; do
    # Получаем время создания процесса в секундах с начала эпохи Unix
    start_time=$(stat -c %Y "/proc/$pid")
    
    # Вычисляем разницу во времени
    time_diff=$((current_time - start_time))

    # Если прошло менее 10 секунд с момента запуска процесса, создаем файл
    if ((time_diff <= 10)); then
        touch "${pid}"
    fi
done


