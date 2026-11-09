<?php

require_once "../config/conexao.php";

$id = $_POST["id"];
$titulo = $_POST["titulo"];
$tipo = $_POST["tipo"];
$genero = $_POST["genero"];
$ano = $_POST["ano"];

$sql = "UPDATE catalogo
        SET titulo = :titulo,
            tipo = :tipo,
            genero = :genero,
            ano = :ano
        WHERE id = :id";

$stmt = $pdo->prepare($sql);

$stmt->execute([
    ":titulo" => $titulo,
    ":tipo" => $tipo,
    ":genero" => $genero,
    ":ano" => $ano,
    ":id" => $id
]);

echo "Título atualizado com sucesso!";

?>