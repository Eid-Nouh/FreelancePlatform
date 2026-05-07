
     function getData() {
            fetch('/api/')
            .then(response => response.json())
            .then(data => {
                document.getElementById("result").innerText = data.message;
            })
            .catch(error => console.log(error));
        }


        