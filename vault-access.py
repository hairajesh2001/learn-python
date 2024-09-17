<<<<<<< HEAD
#!/usr/bin/env python
import hvac
import  operators

# Initialize the Vault client
client = hvac.Client(url='https://your-vault-server-url', token='your-access-token')

# Example: Writing a secret to Vault
secret_data = {'username': 'admin', 'password': 'secretpassword'}
client.write('secret/myapp/mysecrets', **secret_data)

# Example: Reading a secret from Vault
result = client.read('secret/myapp/mysecrets')
if result and 'data' in result:
    secret = result['data']
    print("Retrieved secret:", secret)
else:
    print("Secret not found.")

# Example: Using AppRole authentication
client = hvac.Client(url='https://your-vault-server-url')
client.auth_approle('your-role-id', 'your-secret-id')

# Now you can perform operations that require authentication

# Example: Renewing the token
renewed_token = client.renew_self()
print("Renewed token:", renewed_token)
=======
import hvac

# Vault server address
vault_url = 'http://localhost:8200'

# Initialize the Vault client
client = hvac.Client(url=vault_url)

# Authenticate to Vault (use your authentication method/token)
client.token = 'hvs.hMpATWtK5WNGUqeMq7ngIe7R'

# Example: Write a secret to Vault
def write_secret(path, data):
    response = client.secrets.kv.v2.create_or_update_secret(
        path=path,
        secret=data
    )
    return response

# Example: Read a secret from Vault
def read_secret(path):
    response = client.secrets.kv.v2.read_secret_version(path=path)
    return response['data']['data'] if response else None

# Example: List secrets at a particular path
def list_secrets(path):
    response = client.secrets.kv.v2.list_secrets(path=path)
    return response['data']['keys'] if response else None

# Example: Delete a secret from Vault
def delete_secret(path):
    response = client.secrets.kv.v2.delete_metadata_and_all_versions(path=path)
    return response

# Example usage
path = 'secret/data/my_secret'
data = {'username': 'user123', 'password': 'pass123'}

# Write secret
write_response = write_secret(path, data)
print(f"Write Response: {write_response}")

# Read secret
read_data = read_secret(path)
print(f"Read Data: {read_data}")

# List secrets at a path
list_response = list_secrets('secret/data')
print(f"List Response: {list_response}")

# Delete secret
delete_response = delete_secret(path)
print(f"Delete Response: {delete_response}")

>>>>>>> aaae8f0507475449e338ee049cf60ca350aedb46
