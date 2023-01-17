import pickle
import pandas as pd

anime = pickle.load(open('C:/Users/Super_Computer/ProjectIR-backend/resources/anime_data.pkl', 'rb'))
title = pickle.load(open('C:/Users/Super_Computer/ProjectIR-backend/resources/ani_title.pkl', 'rb'))
synopsis = pickle.load(open('C:/Users/Super_Computer/ProjectIR-backend/resources/ani_synopsis.pkl', 'rb'))
rating = pickle.load(open('C:/Users/Super_Computer/ProjectIR-backend/resources/rating_1000p.pkl', 'rb'))


def query_scoring(query):
    score_t = title.transform(query)
    score_s = synopsis.transform(query)
    sum_score = score_t + score_s
    tf = pd.DataFrame({'bm25-score': list(sum_score),
                       'mal_id': list(anime['mal_id']),
                       'title': list(anime['title']),
                       'type': list(anime['type']),
                       'genres': list(anime['genres']),
                       'score': list(anime['score']),
                       'favorites': list(anime['favorites']),
                       'synopsis': list(anime['synopsis']),
                       'studios': list(anime['studios']),
                       'image': list(anime['images']),
                       'url': list(anime['url'])
                       }).nlargest(columns='bm25-score', n=20)
    tf['rank'] = tf['bm25-score'].rank(ascending=False)
    tf = tf.drop(columns='bm25-score', axis=1)
    tf = tf.to_dict('record')
    return tf


def get_ani_list():
    bound = len(anime)
    tf = pd.DataFrame({'mal_id': list(anime['mal_id']),
                       'title': list(anime['title']),
                       'type': list(anime['type']),
                       'genres': list(anime['genres']),
                       'score': list(anime['score']),
                       'favorites': list(anime['favorites']),
                       'synopsis': list(anime['synopsis']),
                       'studios': list(anime['studios']),
                       'image': list(anime['images']),
                       'url': list(anime['url'])
                       }).nlargest(columns='mal_id', n=bound)
    tf = tf.to_dict('record')
    return tf


def list_bookmark(book):
    res = []
    score = []
    for i in book:
        temp = anime[anime['mal_id'] == i['ani_id']].to_dict('records')[0]
        res.append(temp)
    res.sort(key=lambda i: i['score'], reverse=True)
    return res