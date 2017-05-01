from .settings import *

# Update SITE infos to use the common port 80 to publish the webapp
SITE_FIXED = {
    'name': "Retropie Manager",
    'ip': None, # If 'None' find the ip automatically. Use a string to define another ip/hostname
    'port': '8000', # If 'None' no port is added to hostname, so the server have to be reachable from port 80
}

# Production path to the Recalbox logs file
RECALBOX_LOGFILE_PATH = "/opt/emulationsystem/configs/all/emulationstation/es_log.txt"

# Use packaged assets
ASSETS_PACKAGED = True
