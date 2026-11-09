<?php

require_once "../config/conexao.php";

$id = $_GET["id"];

$sql = "DELETE FROM catalogo WHERE id = :id";

$stmt = $pdo->prepare($sql);

$stmt->execute([
    ":id" => $id
]);

echo "Título excluído com sucesso!";

?>