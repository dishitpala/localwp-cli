"""Python script to access local by flywheel site shell.

Run:
    python PATH-TO-LOCAL_SSH_FILE
"""

import json
import os

# Mac Username.
mac_user = '<username>'

# Sites json path.
sites_json_path = '/Users/{mac_user}/Library/Application Support/Local/sites.json'.format(mac_user=mac_user)
# Sites SSH Entry path.
ssh_entry_path = '/Users/{mac_user}/Library/Application Support/Local/ssh-entry'.format(mac_user=mac_user)

# Check if files exist.
if not os.path.exists(sites_json_path) or not os.path.exists(ssh_entry_path):
    print(u"\u001b[31;1m%s\u001b[0m Visit: \u001b[30;1m\u001b[4m%s\u001b[0m\u001b[0m" % ('Files not exist!', 'https://github.com/dishitpala') )
    exit()

# Head with styling and colors.
print(u"\n\u001b[30;1m%s\u001b[0m" % ('=' * 40) )
print(u"\u001b[31;1m%s\u001b[0m" % ' LOCAL BY FLYWHEEL CLI' )
print(u"\u001b[30;1m%s\u001b[0m\n" % ('=' * 40) )

# Open sites.json file.
sites_json = open( sites_json_path, mode='r' )
# Load JSON.
sites = json.load( sites_json )

# Key is position and value is site ID.
sites_mapping = {}

# Display all sites.
for index, site in enumerate(sites):
    # Site positions in sites.json file.
    sites_mapping[(index + 1)] = site
    print(u"\u001b[30;1m%d.\u001b[0m \u001b[37;1m%s\u001b[0m" % ((index + 1), sites[site]['name'].upper()))

print('')

try:
    # Enter int value for accessing the specific site.
    site_selected = int(input( u'\u001b[36;1mEnter site ID to access site shell: \u001b[0m' ))

except KeyboardInterrupt:

    # Exit if interrupted by keyboard.
    print(u"\n\n\u001b[38;5;214m%s\u001b[0m\n" % 'Okay Bye')
    exit()

except ValueError:

    # Exit if invalid value.
    print(u"\n\u001b[38;5;214m%s\u001b[0m\n" % 'Error: Non intiger value entered!')
    exit()

# Validation.
if site_selected in sites_mapping.keys():
    # create ssh entry path for site.
    ssh_entry = os.path.join(ssh_entry_path, sites_mapping[site_selected] + '.sh').replace(' ','\ ')

    # success.
    print(u'\n\u001b[32;1m%s\u001b[0m \u001b[30;1m%s\u001b[0m\n' % ('Success:', ssh_entry))

    # Execute command.
    os.system(ssh_entry)

else:
    # Exit if invalid value.
    print(u"\n\u001b[38;5;214m%s\u001b[0m\n" % 'Error: Site ID you mentioned not present in local!')
    exit()