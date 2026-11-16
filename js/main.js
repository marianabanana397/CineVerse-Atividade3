
const API_URL = "http://127.0.0.1:5000/catalogo";

// PESQUISA
const formularioBusca = document.querySelector(".form-busca");

if (formularioBusca) {
    formularioBusca.addEventListener("submit", function(evento) {
        evento.preventDefault();

        const textoPesquisa = document.querySelector("#pesquisa").value.toLowerCase();
        const cards = document.querySelectorAll(".card");

        cards.forEach(function(card) {
            const titulo = card.querySelector("h3").textContent.toLowerCase();

            card.style.display = titulo.includes(textoPesquisa) ? "" : "none";
        });
    });
}

// CRIAR CARD
function criarCard(item) {
    const card = document.createElement("article");
    card.className = "card";

    const imagem = document.createElement("div");
    imagem.className = "card-imagem";
    imagem.style.display = "flex";
    imagem.style.alignItems = "center";
    imagem.style.justifyContent = "center";
    imagem.style.backgroundColor = "#252530";
    imagem.textContent = "CINEVERSE";

    const conteudo = document.createElement("div");
    conteudo.className = "card-conteudo";

    const tipo = document.createElement("span");
    tipo.className = "tipo";
    tipo.textContent = item.tipo.toUpperCase();

    const titulo = document.createElement("h3");
    titulo.textContent = item.titulo;

    const detalhes = document.createElement("p");
    detalhes.textContent = item.genero + " . " + item.ano;

    conteudo.append(tipo, titulo, detalhes);
    card.append(imagem, conteudo);

    return card;
}

// BUSCAR CATÁLOGO (GET)
async function carregarCatalogo() {
    try {
        const resposta = await fetch(API_URL);

        if (!resposta.ok) {
            throw new Error("Não foi possível carregar o catálogo.");
        }

        const catalogo = await resposta.json();

        catalogo.forEach(function(item) {
            const tipoNormalizado = item.tipo
                .normalize("NFD")
                .replace(/[\u0300-\u036f]/g, "")
                .toLowerCase();

            let container;

            if (tipoNormalizado === "filme") {
                container = document.querySelector("#catalogo-filmes");
            } else if (tipoNormalizado === "serie") {
                container = document.querySelector("#catalogo-series");
            }

            if (!container) return;

            const titulosExistentes = Array.from(
                container.querySelectorAll(".card h3")
            ).map(function(titulo) {
                return titulo.textContent.trim().toLowerCase();
            });

            if (!titulosExistentes.includes(item.titulo.trim().toLowerCase())) {
                container.appendChild(criarCard(item));
            }
        });

    } catch (erro) {
        console.error("Erro ao carregar catálogo:", erro);
    }
}

// CADASTRAR TÍTULO (POST)
const formularioCadastro = document.querySelector("#form-cadastro");

if (formularioCadastro) {
    formularioCadastro.addEventListener("submit", async function(evento) {
        evento.preventDefault();

        const mensagem = document.querySelector("#mensagem-cadastro");

        const dados = {
            titulo: document.querySelector("#titulo").value,
            tipo: document.querySelector("#tipo").value,
            genero: document.querySelector("#genero").value,
            ano: document.querySelector("#ano").value
        };

        try {
            const resposta = await fetch(API_URL, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(dados)
            });

            const resultado = await resposta.json();

            if (!resposta.ok) {
                throw new Error(resultado.erro || "Erro ao cadastrar título.");
            }

            mensagem.textContent = resultado.mensagem;
            mensagem.style.color = "#4ade80";

            formularioCadastro.reset();

            await carregarCatalogo();

        } catch (erro) {
            mensagem.textContent = erro.message;
            mensagem.style.color = "#ff5555";
        }
    });
}

// INICIAR
carregarCatalogo();
