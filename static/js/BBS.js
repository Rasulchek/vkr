const API_V1_PREFIX = '/api/v1';
const mas = document.getElementById('massage')

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

var fieldp = document.getElementById('p');
var fieldq = document.getElementById('q');

function testCongruate() {
    var text = ""
    var valuep = parseInt(fieldp.value);
    var valueq = parseInt(fieldq.value);
    console.log(valuep)
    console.log(valueq)
    var res1 = 3;
    var res2 = 3;
    if (!isNaN(valuep)) {
        res1 = valuep % 4
    }
    if (!isNaN(valueq)) {
        res2 = valueq % 4
    }
    if (res1 !== 3) {
        text += 'P не конгруэнтно 3 по модулю 4'
        text += '<br> '
    }
    if (res2 !== 3) {
        text += 'Q не конгруэнтно 3 по модулю 4'
        text += '<br> '
    }

    let url = new URL(window.location.origin + API_V1_PREFIX + '/bbsmr');
    let params = new URLSearchParams();
    var body = {
        p: valuep,
        q: valueq,
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
                if (data.test1 === false) {
                    text += 'P не простое';
                    text += '<br> ';
                }
                if (data.test2 === false) {
                    text += 'Q не простое';
                    text += '<br> ';
                }
                if (res1 !== 3 || res2 !== 3 || data.test1 === false || data.test2 === false) {
                    mas.innerHTML = text
                    hideElement('bbs_s');
                    showElement('bbs_a');
                } else {
                    hideElement('bbs_a');
                    showElement('bbs_s');
                }
            }
        );

}

// Обработчик события изменения поля p
fieldp.addEventListener('change', testCongruate);

// Обработчик события изменения поля q
fieldq.addEventListener('change', testCongruate);

const bbsstart = document.getElementById("calculate_bbs");

bbsstart.addEventListener("click", function () {

    let p = document.getElementById('p').value;
    let q = document.getElementById('q').value;
    let seed = document.getElementById('seed').value;
    let l = document.getElementById('l').value;

    let url = new URL(window.location.origin + API_V1_PREFIX + '/bbs');
    let params = new URLSearchParams();
    var body = {
        p: p,
        q: q,
        seed: seed,
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
                document.getElementById('bbs').value = data.L;
            }
        );
})