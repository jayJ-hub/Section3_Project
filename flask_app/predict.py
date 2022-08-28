
##save in 2Darray
import numpy as np

import pickle
#import id, secret
from auth import client_id,client_secret

#authorization to access spotify API
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 

def process_input(user_input):
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    #import model
    with open(f'model.pkl', 'rb') as pickle_file:
        pickle_list = pickle.load(pickle_file)
    model = pickle_list[0]
    X = pickle_list[1]

    #receive input (song name -> uri)
    search_str = user_input
    input_uri = sp.search(search_str)['tracks']['items'][0]['uri']

    # (test) input_uri = 'spotify:track:0Svkvt5I79wficMFgaqEQJ'


    #pull attributes from spotify
    ##pull audio from uri
    attr = sp.audio_features(input_uri)


    attr_list = [
        attr[0]['acousticness'], attr[0]['danceability'], attr[0]['energy'], attr[0]['instrumentalness'],
        attr[0]['liveness'], attr[0]['loudness'], attr[0]['speechiness'], attr[0]['tempo'],attr[0]['valence']
        ]

    arr = np.array(attr_list).reshape(1, -1)

    #predict with model using attributes
    predict = model.predict(arr)[0]

    #show output
    print(f'predicted popularity is {predict:.2f}/100')
    return f'predicted popularity is {predict:.2f}/100'