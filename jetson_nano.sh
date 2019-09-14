sudo apt-get -y install python3-dev

# Configuring Python environment

# Install pip
wget https://bootstrap.pypa.io/get-pip.py
sudo -H python3 get-pip.py
rm get-pip.py

# Install Python virtual environments
sudo pip install virtualenv virtualenvwrapper

#nano ~/.bashrc
# # virtualenv and virtualenvwrapper
# export WORKON_HOME=$HOME/.virtualenvs
# export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
# source /usr/local/bin/virtualenvwrapper.sh
# source ~/.bashrc

# Install pycuda, seems to work only with pip3
sudo pip3 install pycuda


# Successfully installed opencv 4.0.0 using the installation scripts github
# Might need to increase swap space!
