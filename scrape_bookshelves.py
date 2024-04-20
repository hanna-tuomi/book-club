import pandas as pd

# test usernames 
username = "137373049-hanna"
ashley_user = "127764095-pocket-of-spoons"

def get_all_books(username):

    # set up the loop parameters
    stop_flag = 0
    page_start = 1
    book_shelf = []

    while stop_flag == 0:
        
        # get the url for the next page
        url = f"https://www.goodreads.com/review/list/{username}?page={page_start}&per_page=20"
        
        # get the pages books
        books = pd.read_html(url, displayed_only=False, extract_links="all")[1]
        
         # clean the df
         
         # select the columns of interest 
         # want 
         
         # get rid of entry text
        
        
        book_shelf.append(books)
        
        # if the page does not have more than 100 books it is the last page
        if len(books) < 20:
            stop_flag = 1
            
        # iterate to the next page
        page_start += 1

    # create the bookshelf 
    book_shelf_df = pd.concat(book_shelf)
    
    return(book_shelf_df)


df = get_all_books(username)
df.to_csv(f"{username}_bookshelf.csv")
print(df.head())