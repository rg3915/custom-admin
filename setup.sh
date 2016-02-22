# Usage: source setup.sh

# Colors
red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

echo "${green}>>> Cloning repo...${reset}"
git clone https://github.com/rg3915/custom-admin.git

echo "${green}>>> Enter in custom-admin directory.${reset}"
cd custom-admin

echo "${green}>>> Creating virtualenv...${reset}"
python -m venv .venv
echo "${green}>>> venv is created.${reset}"

sleep 2
echo "${green}>>> activate the venv.${reset}"
source .venv/bin/activate

echo "${green}>>> Short the prompt path.${reset}"
PS1="(`basename \"$VIRTUAL_ENV\"`)\e[1;34m:/\W\e[00m$ "
sleep 2

echo "${green}>>> Installing dependencies...${reset}"
pip install -r requirements.txt

echo "${green}>>> Creating .env${reset}"
cp contrib/env-sample .env

echo "${green}>>> Running migrate...${reset}"
python manage.py migrate

echo "${green}>>> Create Superuser...${reset}"
python manage.py createsuperuser --username='admin' --email=''

echo "${green}>>> Done.${reset}"
