from login import login
import searcher
import csv


def main():
    api = login()
    query = input("Termino para buscar:  ")
    count = input("¿Cuantos tuits quieres?:  ")
    # Vamos a buscar los tweets y crear una de lista de listas sobre a que luego podemos iterar para armar el documento final
    tweet_results = []
    last_id = -1
    while len(tweet_results) < int(count):
        search = searcher.search_tweets(api, query, last_id)
        last_id = searcher.find_last_id
        for tweet in search:
            time_text_user_fav = []
            time_text_user_fav.append(tweet.created_at)
            time_text_user_fav.append(tweet.full_text.replace('\n', ' '))
            time_text_user_fav.append(tweet.user.screen_name)
            time_text_user_fav.append(tweet.favorite_count)
            time_text_user_fav.append(tweet.retweet_count)
            tweet_results.append(time_text_user_fav)

    with open("results_{}.csv".format(query), "a+", encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["TimeStamp", "Texto", "Usuario", "Likes", "Retweets"])
        for row in tweet_results:
            writer.writerow(row)


if __name__ == "__main__":
    main()
