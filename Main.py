from ResearchPublication import ResearchPublication
from ExceptionHandler import ExceptionHandler


if __name__ == "__main__":

    research_publication = ResearchPublication()

    # get the publications from the GET API call
    valid_fields = research_publication.get_publication_keys()
    print('Below are the keys/fields present in the publication')
    print(valid_fields)
    try:
        
        # taking input for the fields that are to be projected/filtered 
        fields_to_display = input(
                        'Please enter the field/fields from the valid list shown above (if more than one then separate them using comma (,)) : ')
        fields_to_display = fields_to_display.replace(' ', '').lower().split(',')

        if not all(x in valid_fields for x in fields_to_display):
            raise ExceptionHandler('All the fields entered are not present in the valid set')  

        # take input for searching -- either author name or from data and to date
        author_name = None
        from_date = None
        to_date= None

        while True:
            try:
                search_action = int(input(
                    ''' 1. Search by author name \n 2. Search by date range (included) \n Please choose an option: '''))
                if search_action == 1:
                    # search by author name
                    loop_breaker = True
                    author_name = input('Please enter the author name to search the publication : ')
                elif search_action == 2:
                    # search by date range
                    loop_breaker = True
                    from_date = input('Please enter from date (YYYY-MM-DD) : ')
                    to_date = input('Please enter to date (YYYY-MM-DD) : ')
                    
                    # converting the date string to datetime in python
                    try:
                        from_date = datetime.datetime.strptime(from_date, '%Y-%m-%d')
                        to_date = datetime.datetime.strptime(to_date, '%Y-%m-%d')
                    except Exception:
                        raise ExceptionHandler('Invalid format entered for date- should be YYYY-MM-DD')
                else:
                    # continue to raise this exception until user enters a valid input for search_action
                    raise ExceptionHandler('Please choose from the above options only and Try again!')

                # will break the loop if user entered proper option from the given 2 options
                if loop_breaker:
                    break
            except Exception as ex:
                print(ex)
        
        # formatted data and print the publications according to the user inputs
        research_publication.print_formatted_search_data(fields_to_display,author_name,from_date,to_date)

    except Exception as ex:
        print(ex)
