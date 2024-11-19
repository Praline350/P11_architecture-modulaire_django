# Vérifier que Git est disponible
if (!(Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Error "Git n'est pas installé ou introuvable dans le PATH."
    exit 1
}

# Chemin vers le fichier .env
$envFilePath = ".\.env"

# Vérifie si le fichier .env existe
if (Test-Path $envFilePath) {
    # Lis chaque ligne du fichier
    Get-Content $envFilePath | ForEach-Object {
        # Ignore les lignes vides ou les commentaires
        if ($_ -and ($_ -notmatch "^\s*#")) {
            # Sépare la clé et la valeur
            $parts = $_ -split "=", 2
            $key = $parts[0].Trim()
            $value = $parts[1].Trim()
            
            # Ajoute la variable à l'environnement
            [System.Environment]::SetEnvironmentVariable($key, $value, "Process")
        }
    }
} else {
    Write-Output "Fichier .env non trouvé : $envFilePath"
}


Write-Output 'Login DockerHub...'
$env:DOCKER_PASSWORD | docker login -u $env:DOCKER_USERNAME --password-stdin

if ($LASTEXITCODE -ne 0) {
    Write-Error "Le login failed."
    exit $LASTEXITCODE
}


$commitSha = git rev-parse HEAD

Write-Output 'Linting...'
flake8

Write-Output 'Tests & Coverage...'
pytest --cov-report=term-missing --cov-fail-under=80

if ($LASTEXITCODE -ne 0) {
    Write-Output "Tests failed. Need 80% ! Pipeline stoped."
    exit $LASTEXITCODE
}

Write-Output 'Build Docker images...'
docker buildx build -t edwin350/oc_lettings:$commitSha -f Dockerfile .

if ($LASTEXITCODE -ne 0) {
    Write-Error "Docker build Failed"
    exit $LASTEXITCODE
}




Write-Output 'Push Docker image in docker hub ...'
docker push edwin350/oc_lettings:$commitSha

if ($LASTEXITCODE -ne 0) {
    Write-Error "Push on dockerHub Failed"
    exit $LASTEXITCODE
}

Write-Output 'Pipeline Ok ! Image push on the dockerHub with Commit hash for tag'


