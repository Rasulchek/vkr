const API_V1_PREFIX = '/api/v1';

function checkBinaryInput(input) {
        input.value = input.value.replace(/[^01]/g, "");
    }

const sealstart = document.getElementById("calculate_seal");

sealstart.addEventListener("click", function () {
    document.getElementById('key').value = '';
    document.getElementById('T').value = '';
    document.getElementById('S').value = '';
    document.getElementById('R').value = '';
    var fieldn = document.getElementById('n')
    let a = document.getElementById('secret_key').value;
    let n = parseInt(fieldn.value);

    let url = new URL(window.location.origin + API_V1_PREFIX + '/seal');
    let params = new URLSearchParams();
    var body = {
        a: a,
        n: n,
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
                document.getElementById('key').value = data.key;
                document.getElementById('T').value = data.T;
                document.getElementById('S').value = data.S;
                document.getElementById('R').value = data.R;
            }
        );
})

const encrstart = document.getElementById('encrypt');

encrstart.addEventListener("click", function () {
    document.getElementById('text16').value = '';
    document.getElementById('etext').value = '';
    document.getElementById('detext').value = '';
    document.getElementById('detext16').value = '';
    let key = document.getElementById('key').value;
    let text = document.getElementById('text').value;
    if (key === "") {
        alert("Сначала создайте поток ключей!"); // Выводим сообщение, поток ключей не создан
        return; // Прерываем выполнение функции
    }
    if (text === "") {
        alert("Введите текст!"); // Выводим сообщение, поток ключей не создан
        return; // Прерываем выполнение функции
    }

    let url = new URL(window.location.origin + API_V1_PREFIX + '/sealencr');
    let params = new URLSearchParams();
    var body = {
        text: text,
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
                document.getElementById('text16').value = data.text16;
                document.getElementById('etext').value = data.etext;
            }
        );
})

const decrstart = document.getElementById('decrypt');

decrstart.addEventListener("click", function () {

    document.getElementById('detext').value = '';
    document.getElementById('detext16').value = '';
    let etext = document.getElementById('etext').value;
    if (etext === "") {
        alert("Сначала зашифруйте текст!"); // Выводим сообщение, поток ключей не создан
        return; // Прерываем выполнение функции
    }

    let url = new URL(window.location.origin + API_V1_PREFIX + '/sealdecr');
    let params = new URLSearchParams();
    var body = {
        etext: etext,
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
                document.getElementById('detext').value = data.detext;
                document.getElementById('detext16').value = data.detext16;
            }
        );
})
