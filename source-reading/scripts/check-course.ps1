[CmdletBinding()]
param(
    [string]$CourseRoot
)

$ErrorActionPreference = 'Stop'
if ([string]::IsNullOrWhiteSpace($CourseRoot)) {
    $CourseRoot = Join-Path $PSScriptRoot '..'
}
$root = (Resolve-Path -LiteralPath $CourseRoot).Path
$repoRoot = (Resolve-Path -LiteralPath (Join-Path $root '..')).Path

function Get-RelativePath {
    param(
        [Parameter(Mandatory)][string]$BasePath,
        [Parameter(Mandatory)][string]$TargetPath
    )

    $baseFull = [IO.Path]::GetFullPath($BasePath).TrimEnd('\') + '\'
    $baseUri = [Uri]$baseFull
    $targetUri = [Uri][IO.Path]::GetFullPath($TargetPath)
    return [Uri]::UnescapeDataString($baseUri.MakeRelativeUri($targetUri).ToString()).Replace('/', '\')
}

$requiredFiles = @(
    'README.md',
    '00-reading-method.md',
    '01-progress.md',
    '02-version-lock.md',
    'templates/source-map.md',
    'templates/weekly-session.md',
    'templates/phase-gate.md',
    'templates/cold-start-report.md',
    'maps/01-spring-petclinic.md',
    'maps/02-gson.md',
    'maps/03-spring-framework.md',
    'maps/04-openai-python.md',
    'maps/05-langgraph.md',
    'maps/06-dify.md',
    'cold-start/openai-agents-python.md'
)

for ($week = 1; $week -le 12; $week++) {
    $prefix = 'w{0:D2}-' -f $week
    $weekFile = Get-ChildItem -LiteralPath (Join-Path $root 'weeks') -Filter "$prefix*.md" -File -ErrorAction SilentlyContinue |
        Select-Object -First 1
    if (-not $weekFile) {
        $requiredFiles += "weeks/${prefix}<topic>.md"
    }
    else {
        $requiredFiles += Get-RelativePath -BasePath $root -TargetPath $weekFile.FullName
    }
}

$errors = [System.Collections.Generic.List[string]]::new()

foreach ($relativePath in $requiredFiles) {
    $fullPath = Join-Path $root $relativePath
    if ($relativePath -like '*<topic>*') {
        $errors.Add("Missing week file matching: $relativePath")
    }
    elseif (-not (Test-Path -LiteralPath $fullPath -PathType Leaf)) {
        $errors.Add("Missing required file: $relativePath")
    }
}

$markdownRelativePaths = @(& git -C $repoRoot -c core.quotepath=false ls-files --cached --others --exclude-standard -- '*.md')
$markdownFiles = foreach ($relativePath in $markdownRelativePaths) {
    Get-Item -LiteralPath (Join-Path $repoRoot $relativePath)
}
$linkPattern = [regex]'!?\[[^\]]*\]\((?<target>[^)]+)\)'

foreach ($file in $markdownFiles) {
    $relativeFile = Get-RelativePath -BasePath $repoRoot -TargetPath $file.FullName
    $content = Get-Content -Raw -LiteralPath $file.FullName
    if ($null -eq $content) {
        $content = ''
    }

    foreach ($match in $linkPattern.Matches($content)) {
        $target = $match.Groups['target'].Value.Trim()
        if ($target -match '^(https?://|mailto:|codex://|#)') {
            continue
        }

        $target = ($target -split '#', 2)[0]
        if ([string]::IsNullOrWhiteSpace($target)) {
            continue
        }

        $target = [Uri]::UnescapeDataString($target)
        $resolved = Join-Path $file.DirectoryName $target
        if (-not (Test-Path -LiteralPath $resolved)) {
            $errors.Add("Broken relative link in ${relativeFile}: $target")
        }
    }

    if ($relativeFile -like 'source-reading\weeks\*.md') {
        foreach ($heading in @('## 自测', '## 必交产出')) {
            $escapedHeading = [regex]::Escape($heading)
            if ($content -notmatch $escapedHeading) {
                $errors.Add("Missing '$heading' in $relativeFile")
            }
        }
    }
}

$secretPatterns = @(
    'sk-(?:proj-)?[A-Za-z0-9_-]{20,}',
    'gh[pousr]_[A-Za-z0-9]{20,}',
    'AKIA[0-9A-Z]{16}',
    '-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----'
)

$textRelativePaths = @(& git -C $repoRoot -c core.quotepath=false ls-files --cached --others --exclude-standard -- `
    '*.md' '*.ps1' '*.py' '*.java' '*.json' '*.toml' '*.yml' '*.yaml')
$textFiles = foreach ($relativePath in $textRelativePaths) {
    Get-Item -LiteralPath (Join-Path $repoRoot $relativePath)
}

foreach ($file in $textFiles) {
    $relativeFile = Get-RelativePath -BasePath $repoRoot -TargetPath $file.FullName
    $content = Get-Content -Raw -LiteralPath $file.FullName
    if ($null -eq $content) {
        $content = ''
    }
    foreach ($pattern in $secretPatterns) {
        if ($content -match $pattern) {
            $errors.Add("Possible secret in $relativeFile (pattern: $pattern)")
        }
    }
}

if ($errors.Count -gt 0) {
    Write-Host "Course validation failed with $($errors.Count) issue(s):" -ForegroundColor Red
    $errors | ForEach-Object { Write-Host " - $_" -ForegroundColor Red }
    exit 1
}

Write-Host "Course validation passed." -ForegroundColor Green
Write-Host "Checked $($requiredFiles.Count) required files and $($markdownFiles.Count) Markdown files."
