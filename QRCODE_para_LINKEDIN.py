import pyqrcode
import png
from pyqrcode import QRCode

# URL para a qual o QR Code deve apontar
linkedin_url = "www.linkedin.com/in/glauco-runha-piccolo-figlioli-087912306"

# Criar o QR Code a partir da URL
qr = pyqrcode.create(linkedin_url)

# Salvar o QR Code como arquivo PNG
# O parâmetro 'scale' controla o tamanho do QR Code (maior valor significa maior tamanho)
qr.png('linkedin_qr_code.png', scale=8)

print("QR Code gerado e salvo como 'linkedin_qr_code.png'")

