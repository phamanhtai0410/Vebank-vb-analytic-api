```
$$\    $$\ $$$$$$$$\ $$$$$$$\   $$$$$$\  $$\   $$\ $$\   $$\ 
$$ |   $$ |$$  _____|$$  __$$\ $$  __$$\ $$$\  $$ |$$ | $$  |
$$ |   $$ |$$ |      $$ |  $$ |$$ /  $$ |$$$$\ $$ |$$ |$$  / 
\$$\  $$  |$$$$$\    $$$$$$$\ |$$$$$$$$ |$$ $$\$$ |$$$$$  /  
 \$$\$$  / $$  __|   $$  __$$\ $$  __$$ |$$ \$$$$ |$$  $$<   
  \$$$  /  $$ |      $$ |  $$ |$$ |  $$ |$$ |\$$$ |$$ |\$$\  
   \$  /   $$$$$$$$\ $$$$$$$  |$$ |  $$ |$$ | \$$ |$$ | \$$\ 
    \_/    \________|\_______/ \__|  \__|\__|  \__|\__|  \__|
```

# VeBank Analytics API

In-depth documentation on VeBank V1 is available at [https://docs.vebank.io/](https://docs.vebank.io/).

# Local Development

The following assumes the use of `python@>=3.8`.

## Install Dependencies

`pip3 install -r requirements.txt`

## Clone Library
`git clone https://gitlab.rinznetwork.com/vebank/vb-lib.git lib `

## Running command

### Service: 
`python3 manage.py run`

### Job: 
`python3 jobs/<hob_file_name> run -e <exchange_name> - k <key_name> -q <queue_name>`