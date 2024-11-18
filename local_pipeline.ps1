# Vérifier que Git est disponible
if (!(Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Error "Git n'est pas installé ou introuvable dans le PATH."
    exit 1
}

$docker_username = 'edwin350'
$docker_password = 'Chillhouse3500!'

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

Write-Output 'Login DockerHub...'
$docker_password | docker login -u $docker_username --password-stdin

if ($LASTEXITCODE -ne 0) {
    Write-Error "Le login failed."
    exit $LASTEXITCODE
}

Write-Output 'Push Docker image in docker hub ...'
docker push edwin350/oc_lettings:$commitSha

if ($LASTEXITCODE -ne 0) {
    Write-Error "Push on dockerHub Failed"
    exit $LASTEXITCODE
}

Write-Output 'Pipeline Ok ! Image push on the dockerHub with Commit hash for tag'


