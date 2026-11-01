# Gate de verificacao: roda ruff e pytest e para no primeiro erro.
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

$venv = Join-Path $PSScriptRoot ".venv\Scripts"

Write-Host "== ruff check ==" -ForegroundColor Cyan
& (Join-Path $venv "ruff.exe") check .
if ($LASTEXITCODE -ne 0) {
    Write-Host "FALHOU: ruff encontrou problemas." -ForegroundColor Red
    exit 1
}

Write-Host "== pytest ==" -ForegroundColor Cyan
& (Join-Path $venv "python.exe") -m pytest -q
if ($LASTEXITCODE -ne 0) {
    Write-Host "FALHOU: algum teste nao passou." -ForegroundColor Red
    exit 1
}

Write-Host "OK: ruff e pytest passaram." -ForegroundColor Green
