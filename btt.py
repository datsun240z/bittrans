import os.path

torrents = [{'files': [
                     {'name': 'Family.Guy.S12E15.HDTV.x264-EXCELLENCE/Sample/family.guy.s12e15.hdtv.x264-excellence.sample.mp4', 'length': 3538862, 'bytesCompleted': 3538862},
                     {'name': 'Family.Guy.S12E15.HDTV.x264-EXCELLENCE/family.guy.s12e15.hdtv.x264-excellence.nfo', 'length': 1048, 'bytesCompleted': 1048},
                     {'name': 'Family.Guy.S12E15.HDTV.x264-EXCELLENCE/family.guy.s12e15.hdtv.x264-excellence.r01', 'length': 15000000, 'bytesCompleted': 15000000},
                     {'name': 'Family.Guy.S12E15.HDTV.x264-EXCELLENCE/family.guy.s12e15.hdtv.x264-excellence.r02', 'length': 15000000, 'bytesCompleted': 15000000},
                     {'name': 'Family.Guy.S12E15.HDTV.x264-EXCELLENCE/family.guy.s12e15.hdtv.x264-excellence.r00', 'length': 15000000, 'bytesCompleted':15000000},
                     {'name': 'Family.Guy.S12E15.HDTV.x264-EXCELLENCE/family.guy.s12e15.hdtv.x264-excellence.r03', 'length': 8917956, 'bytesCompleted': 8917956},
                     {'name': 'Family.Guy.S12E15.HDTV.x264-EXCELLENCE/family.guy.s12e15.hdtv.x264-excellence.rar', 'length': 15000000, 'bytesCompleted': 15000000},
                     {'name': 'Family.Guy.S12E15.HDTV.x264-EXCELLENCE/family.guy.s12e15.hdtv.x264-excellence.sfv', 'length': 265, 'bytesCompleted': 265}
                    ],
           'id': 94,
           'isFinished': False},
          {'files': [
                     {'name': 'Family.Guy.S12E15.HDTV.x264-EXCELLENCE/Sample/family.guy.s12e15.hdtv.x264-excellence.sample.mp4', 'length': 3538862, 'bytesCompleted': 3538862},
                     {'name': 'Family.Guy.S12E15.HDTV.x264-EXCELLENCE/family.guy.s12e15.hdtv.x264-excellence.nfo', 'length': 1048, 'bytesCompleted': 1048},
                     {'name': 'Family.Guy.S12E15.HDTV.x264-EXCELLENCE/family.guy.s12e15.hdtv.x264-excellence.r01', 'length': 15000000, 'bytesCompleted': 15000000},
                     {'name': 'Family.Guy.S12E15.HDTV.x264-EXCELLENCE/family.guy.s12e15.hdtv.x264-excellence.r02', 'length': 15000000, 'bytesCompleted': 15000000},
                     {'name': 'Family.Guy.S12E15.HDTV.x264-EXCELLENCE/family.guy.s12e15.hdtv.x264-excellence.r00', 'length': 15000000, 'bytesCompleted':15000000},
                     {'name': 'Family.Guy.S12E15.HDTV.x264-EXCELLENCE/family.guy.s12e15.hdtv.x264-excellence.r03', 'length': 8917956, 'bytesCompleted': 8917956},
                     {'name': 'Family.Guy.S12E15.HDTV.x264-EXCELLENCE/family.guy.s12e15.hdtv.x264-excellence.rar', 'length': 15000000, 'bytesCompleted': 15000000},
                     {'name': 'Family.Guy.S12E15.HDTV.x264-EXCELLENCE/family.guy.s12e15.hdtv.x264-excellence.sfv', 'length': 265, 'bytesCompleted': 265}
                    ],
           'id': 94,
           'isFinished': True} ]

for t in torrents:
    if t.get('isFinished', False):
        for f in t.get('files', []):
            if f['name'].endswith('.rar'):
                print (os.path.basename(f['name']))

#(any([ f['name'].endswith('.rar')
        #for f in torrent.get('files', [])])
#and
#all([ f['length'] == f['bytesCompleted']
        #for f in torrent.get('files', [])]))

#print("Value : %s" %     torrent.get('files'))
#new_items = [i for i in torrent['files'] if i["name"] ]
#new_items = [i for i in torrent['files'] if "name" in 
#item_names = [name['name'] for name in new_items]

#new_items = [ file["name"] for file in torrent["files"]]
#item_names = [ file["name"] for file in torrent["files"] if file["name"]]

#for sn in item_names:
    #print(os.path.basename(sn))

#for k, v in torrent.items() if k == "id":
    #print "%s=%s" % (k, v)
