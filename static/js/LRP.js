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
