const API_V1_PREFIX = '/api/v1';

function checkBinaryInput(input) {
        if (document.getElementById('field').value === "2")
        input.value = input.value.replace(/[^01]/g, "");
        else {
            input.value = input.value.replace(/[^012]/g, "");
        }
    }

const abmStartButton = document.getElementById("abm_start");

function reloadScript() {
    var container = document.getElementById("tableContainer");
    MathJax.typesetPromise([container]).then(() => {
        console.log('Библиотека успешно подгружена.');
    }).catch((err) => console.error('Ошибка при подгрузке библиотеки.', err));
}

abmStartButton.addEventListener("click", function () {

    let G = document.getElementById('anpol').value;
    let p = document.getElementById('field').value;

    let url = new URL(window.location.origin + API_V1_PREFIX + '/abm');
    let params = new URLSearchParams();
    var body = {
        G: G,
        p: p,
    };
    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(body)
    })
        .then(response => response.json())
        .then(data => {

                var table1 = document.getElementById('table');
                if(table1)
                {
                    // Удаляем элемент из DOM
                    table1.parentNode.removeChild(table1);
                    console.log('вот так вот, удалил значит');
                    console.log(table1);
                }
                else {
                    console.log('вот так вот, значит не удалил');
                    console.log(table1);
                }

                document.getElementById('len').value = data.l;
                document.getElementById('k_abm').value = data.k;
                document.getElementById('bm').value = data.L;
                // document.getElementById('Lo').value = data.L2;
                // document.getElementById('alpha').value = data.alpha;
                // document.getElementById('c').value = data.c;
                // Создание нового элемента таблицы
                var table = document.createElement("table");
                table.setAttribute("id", "table")
                table.classList.add("table-striped", "table-bordered", "text-center");
                // Определение максимальной длины списка
                var maxLength = Math.max(data.g_list.length, data.h_list.length, data.m_list.length, data.b_list.length);
                var numCols = 4;
                // Генерация заголовка таблицы
                var thead = document.createElement("thead");
                var headerRow = document.createElement("tr");

                var th = document.createElement("th");
                th.innerHTML = "\\( j \\)";
                headerRow.appendChild(th);

                var th = document.createElement("th");
                th.innerHTML = "\\( g \\)";
                headerRow.appendChild(th);

                var th = document.createElement("th");
                th.innerHTML = "\\( h \\)";
                headerRow.appendChild(th);

                var th = document.createElement("th");
                th.textContent = "\\( m \\)";
                headerRow.appendChild(th);

                var th = document.createElement("th");
                th.textContent = "\\( b \\)";
                headerRow.appendChild(th);


                thead.appendChild(headerRow);
                table.appendChild(thead);
                // Генерация таблицы
                var tbody = document.createElement("tbody");
                for (var i = 0; i < maxLength; i++) {
                    var row = document.createElement("tr");

                    var cellj = document.createElement("td");
                    cellj.textContent = "\\( " + i + " \\)";
                    row.appendChild(cellj);

                    var cell1 = document.createElement("td");
                    cell1.textContent = i < data.g_list.length ? "\\( " + data.g_list[i] + " \\)" : "";
                    row.appendChild(cell1);

                    var cell2 = document.createElement("td");
                    cell2.textContent = i < data.h_list.length ? "\\( " + data.h_list[i] + " \\)" : "";
                    row.appendChild(cell2);

                    var cell3 = document.createElement("td");
                    cell3.textContent = i < data.m_list.length ? "\\( " + data.m_list[i] + " \\)" : "";
                    row.appendChild(cell3);

                    var cell4 = document.createElement("td");
                    cell4.textContent = i < data.b_list.length ? "\\( " + data.b_list[i] + " \\)" : "";
                    row.appendChild(cell4);

                    tbody.appendChild(row);
                }

                table.appendChild(tbody);

                // Получение ссылки на элемент, куда нужно добавить таблицу
                var container = document.getElementById("tableContainer");

                // Добавление таблицы в контейнер
                container.appendChild(table);
                // MathJax.Hub.Queue(["Typeset", MathJax.Hub, container]);
                reloadScript();
            }
        );

});
