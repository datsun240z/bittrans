import os.path

torrent = {'files': [
                     {'name': 'Family.Guy.S12E15.HDTV.x264-EXCELLENCE/Sample/family.guy.s12e15.hdtv.x264-excellence.sample.mp4', 'length': 3538862, 'bytesCompleted': 3538862},
                     {'name': 'Family.Guy.S12E15.HDTV.x264-EXCELLENCE/family.guy.s12e15.hdtv.x264-excellence.nfo', 'length': 1048, 'bytesCompleted': 1048},
                     {'name': 'Family.Guy.S12E15.HDTV.x264-EXCELLENCE/family.guy.s12e15.hdtv.x264-excellence.r01', 'length': 15000000, 'bytesCompleted': 15000000},
                     {'name': 'Family.Guy.S12E15.HDTV.x264-EXCELLENCE/family.guy.s12e15.hdtv.x264-excellence.r02', 'length': 15000000, 'bytesCompleted': 15000000},
                     {'name': 'Family.Guy.S12E15.HDTV.x264-EXCELLENCE/family.guy.s12e15.hdtv.x264-excellence.r00', 'length': 15000000, 'bytesCompleted':15000000},
                     {'name': 'Family.Guy.S12E15.HDTV.x264-EXCELLENCE/family.guy.s12e15.hdtv.x264-excellence.r03', 'length': 8917956, 'bytesCompleted': 8917956},
                     {'name':'Family.Guy.S12E15.HDTV.x264-EXCELLENCE/family.guy.s12e15.hdtv.x264-excellence.rar', 'length': 15000000, 'bytesCompleted': 15000000},
                     {'name': 'Family.Guy.S12E15.HDTV.x264-EXCELLENCE/family.guy.s12e15.hdtv.x264-excellence.sfv', 'length': 265, 'bytesCompleted': 265}
                    ],
           'id': 94,
           'isFinished': False} 

def is_rar(torrent):
    return True

def is_finished_and_in_rar(torrent):
    #[k for k, v in torrent['files'].items() if v < 1500000]
    return not print (torrent['files'])
    
print(torrent)
print("Value : %s" %  torrent.get('id'))
print("Value : %s" %  torrent.get('isFinished'))

#print("Value : %s" %     torrent.get('files'))
new_items = [i for i in  torrent.get('files')
                 if i["name"] ]
item_names = [name['name'] for name in new_items]

for sn in item_names:
    print(os.path.basename(sn))

#for k, v in torrent.items() if k == "id":
    #print "%s=%s" % (k, v)

