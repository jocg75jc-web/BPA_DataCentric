$ErrorActionPreference = 'Stop'

$base = "C:\Users\javier.castaneda\botsquad\BPA_DataCentric"

$dirs = @(
    "$base\apps\monitor-frontend",
    "$base\apps\monitor-backend",
    "$base\services\extraction-runner",
    "$base\shared\unified-extraction",
    "$base\shared\contracts",
    "$base\data\querys\titania",
    "$base\data\querys\onnet",
    "$base\data\outputs\titania",
    "$base\data\outputs\onnet",
    "$base\data\parametros\titania",
    "$base\data\parametros\onnet",
    "$base\config\profiles",
    "$base\ops\docker",
    "$base\ops\scripts",
    "$base\ops\runbooks"
)

foreach ($dir in $dirs) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
        Write-Output "CREATED $dir"
    } else {
        Write-Output "EXISTS  $dir"
    }
}

Write-Output "SPRINT1_STRUCTURE_READY"
