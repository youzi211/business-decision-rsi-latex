$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot
$texFile = Get-ChildItem -LiteralPath $PSScriptRoot -Filter '*.tex' | Select-Object -First 1
$buildPath = Join-Path $PSScriptRoot 'work\latex-build'
New-Item -ItemType Directory -Path $buildPath -Force | Out-Null
for ($pass = 1; $pass -le 2; $pass++) {
    & xelatex '-interaction=nonstopmode' '-halt-on-error' "-output-directory=$buildPath" $texFile.FullName
    if ($LASTEXITCODE -ne 0) { throw "XeLaTeX failed on pass $pass" }
}
$outputName = '模型治理与决策节点优化.pdf'
$builtPdf = Join-Path $buildPath ($texFile.BaseName + '.pdf')
$outputPdf = Join-Path $PSScriptRoot $outputName
Copy-Item -LiteralPath $builtPdf -Destination $outputPdf -Force
$oldPdf = Join-Path $PSScriptRoot '业务决策节点轻量化与双闭环RSI自优化方案.pdf'
if (Test-Path -LiteralPath $oldPdf) { Remove-Item -LiteralPath $oldPdf -Force }
