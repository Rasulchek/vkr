const API_V1_PREFIX = '/api/v1';

// Получение элементов формы
var fieldp = document.getElementById('p');
var fieldq = document.getElementById('q');
var fielde1 = document.getElementById('e1');
var fielde2 = document.getElementById('e2');
var fieldm = document.getElementById('m');
var fielda = document.getElementById('a');
var fieldc = document.getElementById('c');

// Функция для вычисления поля m
function calculateFieldm() {
    var valuep = parseInt(fieldp.value);
    var valueq = parseInt(fieldq.value);
    var valuee1 = parseInt(fielde1.value);
    var valuee2 = parseInt(fielde2.value);
    if (!isNaN(valuep) && !isNaN(valuee1) && !isNaN(valuee2) && !isNaN(valueq)) {
        var res = Math.pow(valuep, valuee1) * Math.pow(valueq, valuee2);
        fieldm.value = res;
    }
}

// Обработчик события изменения поля p
fieldp.addEventListener('change', calculateFieldm);

// Обработчик события изменения поля e
fielde1.addEventListener('change', calculateFieldm);

// Обработчик события изменения поля e
fielde2.addEventListener('change', calculateFieldm);

// Обработчик события изменения поля q
fieldq.addEventListener('change', calculateFieldm);


function showElement(elementId) {
    var element = document.getElementById(elementId);
    if (element) {
        element.style.display = "block";
    }
}

function hideElement(elementId) {
    var element = document.getElementById(elementId);
    if (element) {
        element.style.display = "none";
    }
}

function testprim() {

    let a = document.getElementById('a').value;
    let p = document.getElementById('p').value;
    let e = document.getElementById('e1').value;


    let url = new URL(window.location.origin + API_V1_PREFIX + '/lkpTPr');
    let params = new URLSearchParams();
    var body = {
        a: a,
        p: p,
        e: e
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
                if (data.massage === true) {
                    hideElement('tp_a');
                    showElement('tp_s');
                }
                if (data.massage === false) {
                    hideElement('tp_s');
                    showElement('tp_a');
                }
            }
        );
}

function check_testprim() {
    var fieldp = document.getElementById('p');
    var fielde1 = document.getElementById('e1');
    var fielda = document.getElementById('a');
    var valuep = parseInt(fieldp.value);
    var valuea = parseInt(fielda.value);
    var valuee1 = parseInt(fielde1.value);
    if (!isNaN(valuep) && !isNaN(valuee1) && !isNaN(valuea)) {
        testprim();
    }
}

// Обработчик события изменения поля p
fieldp.addEventListener('change', check_testprim);

// Обработчик события изменения поля e
fielde1.addEventListener('change', check_testprim);

// Обработчик события изменения поля q
fielda.addEventListener('change', check_testprim);


function testmulprim() {

    let a = document.getElementById('a').value;
    let c = document.getElementById('c').value;
    let m = document.getElementById('m').value;


    let url = new URL(window.location.origin + API_V1_PREFIX + '/lkpTMPr');
    let params = new URLSearchParams();
    var body = {
        a: a,
        c: c,
        m: m
    };
    var mas = document.getElementById('massage')
    var text = ""
    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(body)
    })
        .then(response => response.json())
        .then(data => {
                if (data.massage1 === true && data.massage2 === true && data.massage3 === true) {
                    hideElement('tm_a');
                    showElement('tm_s');
                }
                if (data.massage1 === false || data.massage2 === false || data.massage3 === false) {
                    if (data.massage1 === false) {
                        text += '1) b = a-1 не делится на все простые делители числа m ';
                        text += '<br> '
                    }
                    if (data.massage2 === false) {
                        text += '2) если m делится на 4, то и b должно делится на 4';
                        text += ' <br> '
                    }
                    if (data.massage3 === false) {
                        text += '3) число c не взаимно простое с m ';
                    }
                    mas.innerHTML = text
                    hideElement('tm_s');
                    showElement('tm_a');
                }
            }
        );
}

function check_testmulprim() {
    var fielda = document.getElementById('a');
    var fieldc = document.getElementById('c');
    var fieldm = document.getElementById('m');
    var valuea = parseInt(fielda.value);
    var valuec = parseInt(fieldc.value);
    var valuem = parseInt(fieldm.value);
    if (!isNaN(valuea) && !isNaN(valuec) && !isNaN(valuem)) {
        testmulprim();
    }
}

// Обработчик события изменения поля p
fielda.addEventListener('change', check_testmulprim);

// Обработчик события изменения поля e
fieldc.addEventListener('change', check_testmulprim);

// Обработчик события изменения поля q
fieldm.addEventListener('change', check_testmulprim);

fieldp.addEventListener('change', check_testmulprim);

fieldq.addEventListener('change', check_testmulprim);

fielde1.addEventListener('change', check_testmulprim);


function lkppower() {

    let a = document.getElementById('a').value;
    let m = document.getElementById('m').value;


    let url = new URL(window.location.origin + API_V1_PREFIX + '/lkpPow');
    let params = new URLSearchParams();
    var body = {
        a: a,
        m: m
    };

    var mas = document.getElementById('power')
    text = 'Мощность ЛКП равна '

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(body)
    })
        .then(response => response.json())
        .then(data => {
                if (data.test === true) {
                    text += data.power
                    mas.innerHTML = text
                    hideElement('p_a');
                    showElement('p_s');
                }
                if (data.test === false) {
                    hideElement('p_s');
                    showElement('p_a');
                }
            }
        );
}

function check_lkppower() {
    var fielda = document.getElementById('a');
    var fieldm = document.getElementById('m');
    var valuea = parseInt(fielda.value);
    var valuem = parseInt(fieldm.value);
    if (!isNaN(valuea) && !isNaN(valuem)) {
        lkppower();
    }
}

// Обработчик события изменения поля p
fielda.addEventListener('change', check_lkppower);

// Обработчик события изменения поля q
fieldm.addEventListener('change', check_lkppower);

fieldp.addEventListener('change', check_lkppower);

fieldq.addEventListener('change', check_lkppower);

fielde1.addEventListener('change', check_lkppower);


const culkEl = document.getElementById("calculate_element");

culkEl.addEventListener("click", function () {

    let a = document.getElementById('a').value;
    let c = document.getElementById('c').value;
    let m = document.getElementById('m').value;
    let unkn_num = document.getElementById('num_des_el').value;
    let kn_num = document.getElementById('num_kn_el').value;
    let kn_el = document.getElementById('kn_el').value;

    let url = new URL(window.location.origin + API_V1_PREFIX + '/calcel');
    let params = new URLSearchParams();
    var body = {
        a: a,
        c: c,
        m: m,
        unkn_num: unkn_num,
        kn_num: kn_num,
        kn_el: kn_el,

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
                if (data.test === true) {
                    document.getElementById('des_el').value = data.unkn_el;
                    hideElement('c_a');
                    showElement('c_s');
                }
                if (data.test === false) {
                    document.getElementById('des_el').value = "";
                    hideElement('c_s');
                    showElement('c_a');


                }
            }
        );


})


const lrpstart = document.getElementById("calculate_lrp");

lrpstart.addEventListener("click", function () {

    let x = document.getElementById('x0').value;
    let a = document.getElementById('a').value;
    let c = document.getElementById('c').value;
    let m = document.getElementById('m').value;
    let l = document.getElementById('l').value;

    let url = new URL(window.location.origin + API_V1_PREFIX + '/lkp');
    let params = new URLSearchParams();
    var body = {
        x: x,
        a: a,
        c: c,
        m: m,
        l: l,
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
                document.getElementById('lrp').value = data.L;
            }
        );
})