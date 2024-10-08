@echo off
echo Vérification de l'installation de 'requests'...
pip show requests >nul 2>&1

IF %ERRORLEVEL% NEQ 0 (
    echo 'requests' n'est pas installé. Installation en cours...
    pip install requests
) ELSE (
    echo 'requests' est déjà installé.
)

pause
