import pickle
import pandas as pd

anime = pickle.load(open('C:/Users/Super_Computer/ProjectIR-backend/resources/anime_data.pkl', 'rb'))
title = pickle.load(open('C:/Users/Super_Computer/ProjectIR-backend/resources/ani_title.pkl', 'rb'))
synopsis = pickle.load(open('C:/Users/Super_Computer/ProjectIR-backend/resources/ani_synopsis.pkl', 'rb'))


def query_scoring(query):
    score_t = title.transform(query)
    score_s = synopsis.transform(query)
    sum_score = score_t + score_s
    tf = pd.DataFrame({'bm25-score': list(sum_score),
                       'mal_id': list(anime['mal_id']),
                       'images': list(anime['images']),
                       'title': list(anime['title']),
                       'type': list(anime['type']),
                       'genres': list(anime['genres']),
                       'score': list(anime['score']),
                       'scored_by': list(anime['scored_by']),
                       'members': list(anime['members']),
                       'favorites': list(anime['favorites']),
                       'synopsis': list(anime['synopsis']),
                       'studios': list(anime['studios'])
                       }).nlargest(columns='bm25-score', n=20)
    tf['rank'] = tf['bm25-score'].rank(ascending=False)
    tf = tf.drop(columns='bm25-score', axis=1)
    tf = tf.to_dict('record')
    return tf


def get_ani_list():
    # user_id = 14
    # user_df = rating.copy().loc[rating['user_id'] == user_id]
    # user_df = make_user_feature(user_df)
    # anime_rec = predict(user_df, 10, anime, rating)
    bound = len(anime)
    tf = pd.DataFrame({'mal_id': list(anime['mal_id']),
                       'images': list(anime['images']),
                       'title': list(anime['title']),
                       'type': list(anime['type']),
                       'genres': list(anime['genres']),
                       'score': list(anime['score']),
                       'scored_by': list(anime['scored_by']),
                       'members': list(anime['members']),
                       'favorites': list(anime['favorites']),
                       'synopsis': list(anime['synopsis']),
                       'studios': list(anime['studios'])
                       }).nlargest(columns='mal_id', n=bound)
    tf = tf.to_dict('record')
    return tf