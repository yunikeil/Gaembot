<p align="center">
    <img src="https://media.discordapp.net/attachments/1093506269593206895/1114972350279078029/image.png?width=802&height=353" alt="Discord logo">
</p>

# Gaembot

## О проекте

Gaembot - это чат-бот, разработанный в рамках изучения командной работы из курса университета. В современном мире многие проекты являются командными, для того, чтобы успешно работать в такой среде, необходимо понимать основные принципы подобной работы и уметь применять их на практике.

Discord - это платформа для общения и координации в командной среде, и боты для нее могут значительно упростить или разнообразить процесс общения и взаимодействия между участниками. Кроме того, создание бота для Discord может быть полезным упражнением для практики программирования и разработки приложений.

Проект Gaembot предназначен для лёгкого внедрения настольных игр в площадку Discord, что делает его интересным примером приложения, использующего навыки программирования для создания интерактивных игровых сред.


## Быстрый старт

* Прямая установка
   1. Клонируете репозиторий `git clone https://github.com/yunikeil/Gaembot`
   2. Запустите `python ./Gaembot/setup.py -i normal`
   3. Следуйте инструкциям установщика
   4. Готово!
* Старт with Docker
    1. Клонируете репозиторий `git clone https://github.com/yunikeil/Gaembot`
    2. Запустите `python ./Gaembot/setup.py -i docker`
    3. Запустите сборку `docker build -t Gaembot ./Gaembot`
    4. Запустите образ `docker run Gaembot`
    5. Готово!

## Общая структура проекта [^1]

Весь проект разделён на несколько главных папок:

* docs - включает в себя документацию по коду, а также различные примеры
* server_helpers - вспомогательные файлы инструкции и методы для удобного развёртывания и обновления конфигурации серверов
* src - включает в себя исходные файлы проекта

В свою очередь docs состоит из:

* docs_our - какие либо личные заметки по проекту, примеры из документации библиотек и т.д.
* docs_sphinx - документация собираемая с помощью Sphinx + reStructuredText

А директория src включает в себя:

* cogs - папка, содержащая в себе дополнительные модули для Discord бота, которые можно легко выгружать и загрузжать
* games - папка, содержащая в себе основной код игр
* configuration.py - файл конфигурации, генерируется в setup.py
* main.py -  главный файл, из него загружаются и выгружаются модули, производится отладка

### Файл - установщик

...

## Стандартные игры

К стандартным играм относятся те, которые были включены в данный репозиторий и описаны в документации.

### Крестики-Нолики

Данная игры была включена одной из первых и относится к играм, не требующим модуля отрисовки, были введены минимальные стандарты для проектирования модулей игры. Основная логика подобного представления заключается в простоте и малом количестве данных, которые можно отобразить в стандартном виде вывода, к примеру текст, embeds, или ввода дискорда: select или кнопки.

### 2048

Вторая из включённых игр. В ней был впервые добавлен модуль отрисовки, общая структура приобрела конечный вид.
При создании класса игры создаётся матрица в соответствии с размером, который выбрал пользователь. Далее в пустой матрице должны появиться начальные значения, которые могут быть: 2 и 2, 2 и 4, 4 и 4. Каждый из этих наборов появляется с определённой вероятностью, так например набор 4 и 4 встречается крайне редко, вероятность его появления около 1%, а набор 2 и 2 является самым частым и появляется с вероятностью большей, чем 50%. Пользователь может выполнять с матрицей четыре действия: сдвинуть все числа вверх, вниз, вправо или влево. Для каждого из этих действий в классе есть соответствующий метод, который выполняет сдвиг и объединение чисел на игровом поле. Если действие было выполнено, вызывается метод добавления нового числа. Он случайным образом выбирает пустую ячейку и вставляет в неё число 2 или 4, которое также выбирается случайно с определённой вероятностью. После выполнения этого метода, вызывается метод проверки окончания игры, который проверяет, возможно ли в матрице ещё выполнить сдвиг или объединение. Если такой возможности нет, игра завершается и пользователю выводится сообщение об окончании игры, иначе картинка с текущим игровым полем пользователя обновляется и пользователь продолжает игру.
Для отрисовки игры использовалась библиотека Pillow, которая позволяет осуществлять различные манипуляции и обработку изображений. Также библиотека позволяет рисовать простейшие фигуры, что и было использовано в проекте. Первоначально создается новое изображение с необходимыми нам размерами (в пикселях). Линии для разделения поля, а также отрисовки рамки по контуру создаются путем указания метода rectangle с указанием начальных и конечных координат. Далее при помощи вложенного цикла алгоритм проходит по матрице с записанными значениями. В зависимости от значения квадрат с числом по центру будет иметь различный цвет. Отображение блоков осуществляется от верхнего левого (начало координат) до нижнего правого угла.

### Шашки

Третья игра изменила способ ввода с кнопок на modals. Эксперементально была подтверждена возможность и удобство использования различных методов ввода. Ранее в играх были только кнопки, сейчас можно спокойно подключать контекстные команды, команды приложений, modals, кнопки, а также использовать их в связке друг с другом, всё ограничивается лишь вашей фантазией и API Discord'а.
При создании нового объекта класса шашек в конструкторе создаётся матрица с 12 чёрными и 12 белыми шашками. Во время выполнении хода пользователь должен выбрать начальные координаты фигуры, которой он хочет походить и конечные координаты точки, в которую фигуру нужно переместить. Основной метод выполнения хода проверяет, возможно ли переместить шашку по координатам, указанным пользователем. Если такой ход возможен, он выполняется и для пользователя выводится сообщение об успешность хода. В противном случае выводится одно из нескольких сообщений об ошибках, таких как невозможность перемещения фигуры по введённым координатам или нарушение очерёдности хода.
В том случае, если ход был выполнен, выполняется несколько проверок:

* во-первых, окончание игры. После того, как один игрок совершил ход, программа проверяет, может ли соперник совершить ход. Если у соперника нет возможности походить, то игра завершается и игрок, совершивший последний ход, считается победителем.
* во-вторых, может ли пользователь, выполнивший этот ход продолжить его. В таком случае возможность следующего хода предоставляется обоим игрокам для той ситуации, когда у текущего пользователя есть возможность продолжить ход, но он её не замечает, тогда ходит его соперник. Если же возможности продолжить ход нет, возможность ходить следующим предоставляется только противоположному игроку.

Отрисовка также строится на библиотеке Pillow. Помимо непосредственно игры на изображении выводится игровая информация (чей ход, невозможность хода и т.д.).  Во вложенном цикле осуществляется отрисовка игрового поля путем создания на определенном расстоянии друг от друга квадратов с установленными координатами. Цвет поля зависит от счетчика типа булево который изменяется после каждой отрисовки. В этом же цикле осуществляется и отрисовка шашек и дамок. Алгоритм определяет вид фигуры путем считывания ячейки массива. Далее наносится координатная сетка. Цикл наносит вначале цифры изменяя координату X, затем путем считывания посимвольно строки с буквами наносятся координаты вертикальные (изменяя координату Y).

## Добавление своих игр

Так этот проект предоставляет каркас для добавления игр, вы также можете попытаться сделать что то своё. Для этого нужно следовать правилам, по которым бот регестрирует и обрабатывает игры.

### Основная структура файла игры

Тут должен лежать файлик

### Регистрация игры в конфигурации бота

TODO

### Обновление без полной остановки бота

...

## Ресурсы, использующиеся в разработке

Для разработки бота были использованы следующие ресурсы:

* <https://github.com/nextcord/nextcord>
* <https://docs.nextcord.dev/en/stable/ext/commands/api.html#cogs>
* <https://discord.com/developers/docs/>
* <https://discord.com/developers/applications>
* <https://discord.com/api/oauth2/>

[^1]: "Подробнее о структуре папок":http://docs.yunikeil.ru/