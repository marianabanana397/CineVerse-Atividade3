const formularioBusca = document.querySelector(".form-busca");

if (formularioBusca) {

    formularioBusca.addEventListener("submit", function(evento) {

        evento.preventDefault();

        const textoPesquisa = document.querySelector("#pesquisa").value.toLowerCase();

        const cards = document.querySelectorAll(".card");

        cards.forEach(function(card) {

            const titulo = card.querySelector("h3").textContent.toLowerCase();

            if (titulo.includes(textoPesquisa)) {
                card.style.display = "";
            } else {
                card.style.display = "none";
            }

        });

    });

}