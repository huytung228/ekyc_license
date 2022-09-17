from truepy import License
import warnings
warnings.filterwarnings("ignore")
from datetime import datetime

def verify_license():
    # Load the certificate
    with open('certificate.pem', 'rb') as f:
        certificate = f.read()

    # Load the license
    with open('license.key', 'rb') as f:
        license = License.load(f, b'LicensePassword')
        
    try:
        license.verify(certificate)
        return datetime.now() <= license.data.not_after
    except:
        return False

if __name__ == "__main__":
    print(verify_license())