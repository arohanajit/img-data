import requests as requests
import urllib.request as url
import os
import warnings

class Api:
    def __init__(self):
        """ All the requirements may differ function to function
            so I have decided to add them as arguments in functions
            itself
        """
        pass

    def pexels(self, query, api_key, count):

        self.__make_dataset(query)

        query_url = query.replace(' ','+')
        pexels_auth = {"Authorization":api_key}
        url = 'https://api.pexels.com/v1/search?per_page=80&query={}'.format(query_url)

        result = self.__request(url,pexels_auth)
        if count>result['total_results']:
            print("{} found out of {} queried".format(result['total_results'], count))
            count = result['total_results']
        else:
            print("{} Total Images available".format(result['total_results']))

        img = 1
        while(img<count):
            data = result
            for i in range(len(data['photos'])):
                img_data = requests.get(data['photos'][i]['src']['medium']).content
                with open("dataset/{}/pexels{}.jpg".format(query,str(img)),'wb+') as f:
                    f.write(img_data)
                img+=1
                if img%50==0:
                    print(img," done.")
                if img==count+1:
                    f.close()
                    break
  
            if 'next_page' in list(data.keys()):
                result = self.__request(data['next_page'],pexels_auth)

        print("Completed.")


    def unsplash(self, query, api_key, count):
        warnings.warn("Warning: Not having a production level API can limit the usage of API to 300-500 images per query.")


        self.__make_dataset(query)
        img_query = query.replace(' ','+')
        url = 'https://api.unsplash.com/search/photos?page={}&query={}&client_id={}'.format(1,img_query,api_key)
        result = self.__request(url)

        total_page = result['total_pages']
        if count>total_page:
            print("{} found out of {} queried".format(total_page, count))
            count = total_page
        else:
            print("{} Total Images available".format(total_page))

        img = 1
        for i in range(1,total_page+1):
            url = 'https://api.unsplash.com/search/photos?page={}&query={}&client_id={}'.format(i,img_query,api_key)
            r = self.__request(url)
            for j in range(len(r['results'])):
                data = requests.get(r['results'][j]['urls']['regular']).content
                with open("datasets/{}/unsplash{}.jpg".format(query,str(img)),'wb+') as f:
                    f.write(data)
                img+=1

                if img%50==0:
                    print(img," done.")

                if img==count+1:
                    f.close()
                    break
            if img==count+1:
                f.close()
                break
        
        print("Completed.")





    def __request(self, url, header=None):
        try:
            result = requests.get(url, timeout=15, headers=header)
            return result.json()
        except requests.exceptions.RequestException:
            print("Request failed check your internet connection")
            self.request = None
            exit()

    def __make_dataset(self, query):
        if 'dataset' not in os.listdir():
            os.mkdir('dataset')

        if query not in os.listdir('dataset/'):
            os.mkdir('dataset/{}'.format(query))



a = Api()
a.unsplash('Hello','iPRl31TlR_5aO_6pFl6UqjuMJTP_Vvxou-KFNBR-hW4',10)

