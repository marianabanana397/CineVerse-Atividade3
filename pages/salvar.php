<?php

require_once "../config/conexao.php";

$titulo = $_POST["titulo"];
$tipo = $_POST["tipo"];
$genero = $_POST["genero"];
$ano = $_POST["ano"];

$sql = "INSERT INTO catalogo (titulo, tipo, genero, ano)
        VALUES (:titulo, :tipo, :genero, :ano)";

$stmt = $pdo->prepare($sql);

$stmt->execute([
    ":titulo" => $titulo,
    ":tipo" => $tipo,
    ":genero" => $genero,
    ":ano" => $ano
]);

echo "Título cadastrado com sucesso!";
?>