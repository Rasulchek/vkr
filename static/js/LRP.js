const API_V1_PREFIX = '/api/v1';

function checkBinaryInput(input) {
        input.value = input.value.replace(/[^01]/g, "");
    }

const lrpStartButton = document.getElementById("lrp_start");

lrpStartButton.addEventListener("click", function () {

    let pol1 = document.getElementById('pol1').value;
    let pol0 = document.getElementById('pol0').value;

    let url = new URL(window.location.origin + API_V1_PREFIX + '/lrp');
    let params = new URLSearchParams();
    var body = {
        pol1: pol1,
        pol0: pol0
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
                document.getElementById('k').value = data.k;
                document.getElementById('d').value = data.d;
                document.getElementById('L').value = data.L;
                document.getElementById('Lo').value = data.L2;
                document.getElementById('alpha').value = data.alpha;
                document.getElementById('c').value = data.c;
            }
        );
});

// document.getElementById('lrp_start')
//     .onclick((d) => {
//     let pol1 = document.getElementById('pol1').value;
//     console.log(pol1);
// });

// const form = document.querySelector('form');
//         form.addEventListener('submit', (event) => {
//             const inputField1 = document.getElementById('pol0');
//             const inputField2 = document.getElementById('pol1');
//             if (!inputField1.checkValidity() || !inputField2.checkValidity()) {
//                 event.preventDefault();
//                 event.stopPropagation();
//                 inputField1.classList.add('is-invalid');
//                 inputField2.classList.add('is-invalid');
//             } else {
//                 inputField1.classList.remove('is-invalid');
//                 inputField2.classList.remove('is-invalid');
//             }
//         });