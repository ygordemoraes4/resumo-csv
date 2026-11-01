try {
    $callInput = [Console]::In.ReadToEnd() | ConvertFrom-Json
} catch {
    [Console]::Error.WriteLine("Hook nao conseguiu ler a chamada: acao bloqueada por seguranca.")
    exit 2
}

$toolInput = $callInput.tool_input
$targets = @($toolInput.file_path, $toolInput.path, $toolInput.pattern, $toolInput.command)

foreach ($target in $targets) {
    if ($target -match '(?i)data[\\/]+raw') {
        [Console]::Error.WriteLine("Acesso a data/raw/ bloqueado: planilhas reais nao podem ser lidas.")
        exit 2
    }
}

exit 0
