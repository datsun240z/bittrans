import os.path
from transmission import Transmission
# pip install transmission-fluid

client = Transmission(host='192.168.0.111', port=9099, username='admin', password='password')

session = client('session-get')
#print (session['rpc-version'])
#print (session['rpc-version-minimum'])
#print (session['version'])

# When no ids are given, grabs from all torrents
#torrents = client('torrent-get', ids=94, fields=['id', 'isFinished', 'files'])['torrents']
torrents = client('torrent-get', fields=['id', 'isFinished', 'files'])['torrents']
#torrent_ids = [torrent['id'] for torrent in torrents if is_finished_and_in_rar(torrent)]

for t in torrents:
    if t.get('isFinished', False):
        for f in t.get('files', []):
            if f['name'].endswith('.rar'):
                print (os.path.basename(f['name']))

