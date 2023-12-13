import subprocess
import os
import json


def generate_self_signed_certificate(domain, out_dir):
    # Generate a self-signed certificate using OpenSSL
    # Create the folder out_dir and subfolders
    os.makedirs(out_dir, exist_ok=True)

    subprocess.run([
        'openssl', 'req', '-x509', '-nodes', '-newkey', 'rsa:2048',
        '-keyout', os.path.join(out_dir, 'privkey.pem'),
        '-out', os.path.join(out_dir, 'fullchain.pem'),
        '-subj', '/CN={}'.format(domain),
        '-days', '365'
    ], check=True)


if __name__ == "__main__":
    f = open("certbot.json")
    config = json.load(f)
    prod_domain = config['domain']
    f.close()

    # Set your development domain
    dev_domain = "localhost"

    # Set the output directory for the generated certificate
    output_dir = f'conf/live/{prod_domain}'

    # Generate the self-signed certificate
    generate_self_signed_certificate(dev_domain, output_dir)
