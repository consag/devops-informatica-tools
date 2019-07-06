source ../devops_informatica/bin/activate
echo "$(date) - Creating certificates..."
python create_certs.py
echo "$(date) - Creating a file with encrypted content..."
python encrypt_data.py
echo "$(date) - Decrypting encrypted file..."
python decrypt_data.py

