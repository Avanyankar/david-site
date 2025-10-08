sudo apt update && sudo apt upgrade
sudo apt install python3
sudo apt install python3-pip
sudo apt install nginx
sudo apt install uvicorn
sudo apt install -y python3-venv
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt