# Netbox plugin related import
from importlib.metadata import metadata
from netbox.plugins import PluginConfig

metadata = metadata('netbox_proxbox')

class ProxboxConfig(PluginConfig):
    name = metadata.get('Name').replace('-', '_')
    verbose_name = metadata.get('Summary')
    description = metadata.get('Description')
    version = metadata.get('Version')
    author = metadata.get('Author')
    author_email = metadata.get('Author-email')
    base_url = "proxbox"
    required_settings = []
    default_settings = {
        'proxmox': [
            {
                'domain': 'proxbox.example.com',    # May also be IP address
                'http_port': 8006,
                'user': 'root@pam',
                'password': 'Strong@P4ssword',
                'token': {
                    'name': 'proxbox',
                    'value': 'PASTE_YOUR_TOKEN_HERE'
                },
                'ssl': False
            }
        ],
        'netbox': {
            'domain': 'netbox.example.com',     # May also be IP address
            'http_port': 80,
            'token': 'PASTE_YOUR_TOKEN_HERE',
            'ssl': False,
            'settings': {
                'virtualmachine_role_id' : 0,
                'node_role_id' : 0,
                'site_id': 0
            }
        }
    }

config = ProxboxConfig
