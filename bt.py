import os.path
import sys
from transmission import Transmission
# pip install transmission-fluid
from subprocess import call

client = Transmission(host='192.168.0.111', port=9099, username='admin', password='password')

session = client('session-get')

# When no ids are given, grabs from all torrents
#torrents = client('torrent-get', ids=94, fields=['id', 'isFinished', 'files'])['torrents']
torrents = client('torrent-get', fields=['id', 'isFinished', 'files'])['torrents']
#torrent_ids = [torrent['id'] for torrent in torrents if is_finished_and_in_rar(torrent)]
#rarfile.UNRAR_TOOL = "/c/Program\ Files\ \(x86\)/Unrar/UnRAR.exe"
torrent_ids = []

for t in torrents:
    if t.get('isFinished', False):
        for f in t.get('files', []):
            if f['name'].endswith('.rar'):
                fn = f['name']
                #call(["UnRAR", "lb", fn])
                call(["UnRAR", "x", fn])
                torrent_ids.append(t.get('id', []))

client('torrent-remove', ids=torrent_ids)
sys.exit(1)
