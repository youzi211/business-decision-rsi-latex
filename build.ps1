$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot
$texFile = Get-ChildItem -LiteralPath $PSScriptRoot -Filter '*.tex' | Select-Object -First 1
$buildPath = Join-Path $PSScriptRoot 'work\latex-build'
New-Item -ItemType Directory -Path $buildPath -Force | Out-Null
for ($pass = 1; $pass -le 2; $pass++) {
    & xelatex '-interaction=nonstopmode' '-halt-on-error' "-output-directory=$buildPath" $texFile.FullName
    if ($LASTEXITCODE -ne 0) { throw "XeLaTeX failed on pass $pass" }
}
Copy-Item -LiteralPath (Join-Path $buildPath ($texFile.BaseName + '.pdf')) -Destination $PSScriptRoot -Force
