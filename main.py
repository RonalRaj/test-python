from typing import Optional
import yaml
import os

def load_config():
    branch = os.environ.get('BRANCH', 'main')
    if branch == "main":
        filename = 'config_production.yaml'
    elif branch == "dev":
        filename = 'config_staging.yaml'
    else:
        raise ValueError(f"Unsupported branch: {branch}")

    with open(filename, 'r') as file:
        config = yaml.safe_load(file)

    return config

config = load_config()

    # ... rest of the code

    # Use the LB DNS from the config
lb_dns = config['lb_dns']
print(lb_dns)