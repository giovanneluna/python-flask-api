# API
This api was made as a form of study using flask, it create,update, list and delete.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.
You need to have [Docker](https://docs.docker.com/manuals/) installed

```bash
pip install -r requirements.txt
```

## Usage
```
sudo docker build -t python-db .
sudo docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=RootPassword -e MYSQL_DATABASE=concessionaire -e MYSQL_USER=MyUser -e MYSQL_PASSWORD=MainPassword python-db
```
