# # from typing import Optional
# # import yaml
# # import os

# # def load_config():
# #     branch = os.environ.get('BRANCH', 'main')
# #     if branch == "main":
# #         filename = 'config_production.yaml'
# #     elif branch == "dev":
# #         filename = 'config_staging.yaml'
# #     else:
# #         raise ValueError(f"Unsupported branch: {branch}")

# #     with open(filename, 'r') as file:
# #         config = yaml.safe_load(file)

# #     return config

# # config = load_config()

# #     # ... rest of the code

# #     # Use the LB DNS from the config
# # lb_dns = config['lb_dns']
# # print(lb_dns)

# from typing import Optional
# import yaml
# import os
# from dotenv import load_dotenv

# load_dotenv()  # Load values from .env file

# def load_config():
#     branch = os.environ.get('BRANCH', 'main')

#     if branch == "main":
#         lb_dns = os.environ.get('MAIN_LB')
#     elif branch == "dev":
#         lb_dns = os.environ.get('DEV_LB')
#     else:
#         raise ValueError(f"Unsupported branch: {branch}")

#     if lb_dns is None:
#         raise ValueError(f"LB DNS not found for branch: {branch}")

#     config = {'lb_dns': lb_dns}
#     return config

# config = load_config()

# lb_dns = config['lb_dns']
# print(lb_dns)
from typing import Optional
import yaml
import os

def load_config(branch: Optional[str] = None):
    if branch is None:
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

# Example usage:
# If BRANCH environment variable is not set, it uses 'main' as the default branch
config = load_config()
lb_dns = config['lb_dns']
print(lb_dns)
