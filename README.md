# ENVIOSFEDEMY

## Installations

### Install python

Download [python](https://www.python.org/downloads/).

### Virtual environment Python

```powershell
python -m venv env
```

### Create virtual environment

```bash
env\Scripts\activate
```

### Note

When you don't have permissions to create the virtual environment, run the following commands.

```powershell
Set-PSRepository -Name 'PSGallery' -InstallationPolicy Trusted
```

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

When listing the policies the localmachine must be in "AllSigned"

```powershell
Get-ExecutionPolicy -List
```

### Install packages

```bash
pip install -r requirements.txt
```

### Run project

```bash
python manage.py runserver
```
