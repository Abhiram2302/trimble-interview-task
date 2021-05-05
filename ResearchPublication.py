
import requests
import json
import sys
import pandas as pd
import datetime
from ExceptionHandler import ExceptionHandler
from Utils import Utils

class ResearchPublication:
    URL = 'http://api.plos.org/search?q=title:DNA'

    def __init__(self):
        self.publications = self.__get_publications()

    def __get_publications(self):
        #perform reties in case of connection issues and gets the data 
        raw_data = Utils.get_with_retry(ResearchPublication.URL)
        publications = raw_data['response']['docs']
        return publications

    def get_publication_keys(self):
        #returns valid keys for the publication object
        valid_fields = list(self.publications[0].keys())
        return valid_fields

    def __get_author_search(self,author_name):
        publications_output = []
        for publication in self.publications:
            # check if the author name is present in the list of authors of the publication
            if author_name in list(publication['author_display']):
                publications_output.append(publication)
        return publications_output

    def __get_date_search(self,from_date,to_date):
        publications_output = []
        for publication in self.publications:
            # convert the date string obtained from the api response to datetime 
            pub_date_str = datetime.datetime.strptime(publication['publication_date'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d')
            pub_date = datetime.datetime.strptime(pub_date_str, '%Y-%m-%d')

            # comparision between the datetime fields is possible 
            # checking if the published date of the publication is within the date range provided as inputs
            if from_date<=pub_date<=to_date:
                publications_output.append(publication)  
        return publications_output
        

    def __print_data(self,fields_to_display):
        # initializing the total score to be calculated to 0
        total_score = 0
        publications_output = self.publications
        # looping through all the publications one by one
        for i in range(len(publications_output)):

            # storing the keys as we are removing some of them from dictionary
            key_copy = tuple(publications_output[i].keys())  

            #looping through all the keys in the publication object
            for key in key_copy:
                # if key is 'score' then calculation the total score
                # by adding the score to the total_score variable
                if key == 'score':
                    total_score += float(publications_output[i][key])

                # checking if the key is present in the fields_to_display 
                if key not in fields_to_display:
                    # if key is not required to be projected then deleting the key from the object
                    del publications_output[i][key]

        # data frame is initialized with the final search result data
        df = pd.DataFrame(publications_output)

        # incremented the index to start the index from 1 but not 0 --> df has its index starting value defaulted to 0
        df.index = df.index + 1

        # naming the index for better readability
        df.index.name = 's.no'
        
        # printing the df/table 
        print(df)

        # printing the total scores for the search result
        print(f'Total Scores : {total_score}')

        # printing the avg score for the search result
        print(f'Average Scores : {total_score/len(publications_output)}')

    def print_formatted_search_data(self,fields_to_display,author_name,from_date,to_date):
        if author_name is not None:
            self.publications = self.__get_author_search(author_name)
        elif from_date is not None and to_date is not None:
            self.publications = self.__get_date_search(from_date,to_date)
        
        if len(self.publications) == 0:
            raise ExceptionHandler('No publications found for your search')

        if author_name is not None:
            print(f'List of publications whose author is {author_name}')
        elif from_date is not None and to_date is not None:
            print(f'List of publications whose published date is from {from_date} to {to_date}')

        self.__print_data(fields_to_display)
        