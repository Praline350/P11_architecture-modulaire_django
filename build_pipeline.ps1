param (
    [SecureString]$DockerPassword
)

$DockerUsername = "edwin350"


# Vérifie que Docker est en cours d'exécution
if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    Write-Host "Docker n'est pas installé ou en cours d'exécution."
    exit 1
}

# Récupérer le hash du commit
$COMMIT_HASH = git rev-parse --short HEAD
if (-not $COMMIT_HASH) {
    Write-Host "Échec de la récupération du hash du commit. Assurez-vous d'être dans un dépôt Git valide."
    exit 1
}

# Exécuter le linting avec Flake8
Write-Host "Exécution du linting avec Flake8..."
flake8

# Exécuter les tests avec pytest
Write-Host "Exécution des tests avec pytest..."
pytest --cov-config=.coveragerc --cov-report=term-missing --cov-report=html
coverage report --fail-under=80

# Vérifier si la commande a échoué
if ($LASTEXITCODE -ne 0) {
    Write-Host "La couverture de test est inférieure à 80%."
    exit 1
} else {
    Write-Host "La couverture de test est suffisante."
}

# Construire l'image Docker
$IMAGE_NAME = "edwin350/oc_lettings:$COMMIT_HASH"
Write-Host "Construction de l'image Docker : $IMAGE_NAME..."
docker build -t $IMAGE_NAME .

# Se connecter à Docker Hub
if (-not $DockerUsername -or -not $DockerPassword) {
    Write-Host "Nom d'utilisateur ou mot de passe Docker non spécifié."
    exit 1
}

Write-Host "Connexion à Docker Hub..."

# Convertir le SecureString en chaîne de caractères
$BSTR = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($DockerPassword)
$PlainTextPassword = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($BSTR)

# Effectuer la connexion à Docker Hub
$PlainTextPassword | docker login -u $DockerUsername --password-stdin

# Pousser l'image vers Docker Hub
Write-Host "Pousser l'image Docker vers Docker Hub..."
docker push $IMAGE_NAME

Write-Host "Script terminé avec succès !"
