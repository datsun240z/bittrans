from transmission import Transmission
# pip install transmission-fluid

client = Transmission(host='192.168.0.111', port=9099, username='admin', password='password')

session = client('session-get')
print (session['rpc-version'])
print (session['rpc-version-minimum'])
print (session['version'])

def is_rar(torrent):
    return True

def is_finished_and_in_rar(torrent):
    #[k for k, v in torrent['files'].items() if v < 1500000]
    return not print (torrent['files'])

    
# When no ids are given, grabs from all torrents
torrents = client('torrent-get', ids=94, fields=['id', 'isFinished', 'files'])['torrents']
print(torrents)
torrent_ids = [torrent['id'] for torrent in torrents if is_finished_and_in_rar(torrent)]
print(torrent_ids)

#client('torrent-remove', ids=torrent_ids)
#files = [torrent['files'] for torrent in torrents if is_rar(torrent)]
