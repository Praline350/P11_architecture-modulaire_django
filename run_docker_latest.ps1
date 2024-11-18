Write-Output 'Pull latest image'
docker pull edwin350/oc_lettings:latest

Write-Output 'Run Image'
docker run -it -e "PORT=8000" -e "DEBUG=0" -p 8000:8000 edwin350/oc_lettings:latest
