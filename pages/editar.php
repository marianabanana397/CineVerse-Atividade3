<?php

require_once "../config/conexao.php";

$id = $_GET["id"];

$sql = "SELECT * FROM catalogo WHERE id = :id";

$stmt = $pdo->prepare($sql);

$stmt->execute([
    ":id" => $id
]);

$titulo = $stmt->fetch(PDO::FETCH_ASSOC);
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Editar título</title>
</head>
<body>

    <h1>Editar título</h1>

    <form action="atualizar.php" method="post">

        <input type="hidden" name="id" value="<?php echo $titulo['id']; ?>">

        <label>Título:</label>
        <input type="text" name="titulo" value="<?php echo htmlspecialchars($titulo['titulo']); ?>" required>

        <br><br>

        <label>Tipo:</label>
        <select name="tipo" required>
            <option value="Filme" <?php if ($titulo['tipo'] == 'Filme') echo 'selected'; ?>>Filme</option>
            <option value="Série" <?php if ($titulo['tipo'] == 'Série') echo 'selected'; ?>>Série</option>
        </select>

        <br><br>

        <label>Gênero:</label>
        <input type="text" name="genero" value="<?php echo htmlspecialchars($titulo['genero']); ?>" required>

        <br><br>

        <label>Ano:</label>
        <input type="number" name="ano" value="<?php echo $titulo['ano']; ?>" required>

        <br><br>

        <button type="submit">Salvar alterações</button>

    </form>

</body>
</html>