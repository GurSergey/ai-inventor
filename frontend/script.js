document.getElementById('clear-button').addEventListener('click', function () {
    document.getElementById('industries-text').value = '';
    document.getElementById('target-text').value = '';
    document.getElementById('current-text').value = '';
    document.getElementById('faults-text').value = '';
});

document.getElementById("generate-button").addEventListener('click', function (e) {
    document.getElementById("generate-button").disabled = true
    let request = new XMLHttpRequest();   // new HttpRequest instance
    request.open("POST", 'api/answer');
    request.setRequestHeader("Content-Type", "application/json");
    request.onload = function () {
        let status = request.status;
        if (status === 200) {
            let answerDiv = document.getElementById("answer-div");
            let buttonP = document.getElementById('button-p')
            answerDiv.innerHTML = '';
            buttonP.innerHTML = '';
            JSON.parse(request.response).forEach(function (value, index, array) {

                let button = document.getElementById("button-collapse-template");
                button = button.content.cloneNode(true);
                button.querySelector('a').textContent += (index + 1)
                button.querySelector('a').setAttribute('aria-controls', 'collapse-id-' + index);
                button.querySelector('a').setAttribute('href', '#collapse-id-' + index)
                let divParagraph = document.getElementById("card-template");
                divParagraph = divParagraph.content.cloneNode(true);
                divParagraph.querySelector('.card-body').textContent += value
                divParagraph.querySelector('.collapse').setAttribute('id', 'collapse-id-' + index)
                divParagraph.querySelector('.header-solve').textContent += (index + 1)
                document.getElementById('button-p').appendChild(button);
                document.getElementById('answer-div').appendChild(divParagraph);
            })
            // document.getElementById("answer-div").innerText = JSON.parse(request.response).join(" <br> ");
        } else {
            console.log(status);
        }
        document.getElementById("generate-button").disabled = false
    };
    request.send(JSON.stringify({
        "industries": document.getElementById('industries-text').value,
        "targets": document.getElementById('target-text').value,
        "currents": document.getElementById('current-text').value,
        "faults": document.getElementById('faults-text').value,
        "model": document.getElementById('ml-model').value
    }));
})