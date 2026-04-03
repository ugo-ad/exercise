import secrets
import string

ff = "ghp_3efoCY6uc7FynUYA8EwRLhjvmPFxizHKVNVbNN70"
def generate_random_github_token():
    # GitHub Personal Access Tokens start with 'ghp_' followed by 40 random characters
    prefix = "ghp_"
    # Generate 40 random alphanumeric characters
    random_part = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(40))
    return prefix + random_part

# Example usage
token = generate_random_github_token()
print(token)