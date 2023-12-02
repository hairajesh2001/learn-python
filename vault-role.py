import requests
import json

def create_vault_role(vault_url, role_name, policies, token):
    """
    Create a new Vault role.

    Parameters:
    - vault_url (str): The URL of the Vault server (e.g., "http://localhost:8200").
    - role_name (str): The name of the role to be created.
    - policies (list): List of policies to associate with the role.
    - token (str): Vault token with sufficient permissions to create roles.

    Returns:
    - response (requests.Response): The response from the Vault server.
    """

    # API endpoint for creating a role
    endpoint = f"{vault_url}/v1/auth/approle/role/{role_name}"

    # Role configuration
    role_config = {
        "policies": policies,
        # Add other role configuration as needed
    }

    headers = {
        "X-Vault-Token": token,
        "Content-Type": "application/json"
    }

    # Make a POST request to create the role
    response = requests.post(endpoint, data=json.dumps(role_config), headers=headers)

    return response

if __name__ == "__main__":
    # Set your Vault server URL
    vault_url = "http://localhost:8200"

    # Set the role name, policies, and Vault token
    role_name = "example-role"
    policies = ["policy1", "policy2"]
    vault_token = "hvs.hMpATWtK5WNGUqeMq7ngIe7R"

    # Create the Vault role
    response = create_vault_role(vault_url, role_name, policies, vault_token)

    # Check the response
    if response.status_code == 200:
        print(f"Role '{role_name}' created successfully.")
    else:
        print(f"Failed to create role. Status code: {response.status_code}")
        print(response.text)

