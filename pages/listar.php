<?php

require_once "../config/conexao.php";

$sql = "SELECT * FROM catalogo";

$stmt = $pdo->query($sql);

$titulos = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Catálogo CineVerse</title>
</head>
<body>

    <h1>Catálogo CineVerse</h1>

    <?php foreach ($titulos as $titulo): ?>

        <h2><?php echo htmlspecialchars($titulo["titulo"]); ?></h2>
        <p>Tipo: <?php echo htmlspecialchars($titulo["tipo"]); ?></p>
        <p>Gênero: <?php echo htmlspecialchars($titulo["genero"]); ?></p>
        <p>Ano: <?php echo htmlspecialchars($titulo["ano"]); ?></p>

        <hr>

    <?php endforeach; ?>

</body>
</html>