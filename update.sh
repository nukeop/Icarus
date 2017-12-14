ps aux | grep icarus.py | cut -c10-15 | xargs kill
cp config.py config.bak
git reset --hard
git pull origin master
source venv/bin/activate
pip install -r requirements.txt
cp config.bak config.py
python icarus.py --updated
