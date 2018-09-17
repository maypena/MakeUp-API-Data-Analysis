# May Pena
# This program extracts infromation from the a Make-Up API.
# IT allows you to search for specific tags such
# as cruelty-free, vegan, etc. by the tag itself,
# the makeup brand, or by the type of product. 

tagList =  '''
            *********************************************
            *                Our Tags                   *
            *  Water free, Silicone free, Canadian      *
            *  Certclean, Dairy free, EWG Verified      *
            *  Ecocert, Fair trade, Gluten free         *
            *  Hypoallergenic, Chemical free, Natural   *
            *  No Talc, Non-GMO, Organic, Sugar free,   *
            *  Peanut free products,Vegan, alcohol free *
            *  Cruelty free, Oil free, Purpicks         *
            *********************************************
            '''

brandList = '''
            **************************************
            *           Our Brands               *
            * Colourpop, Maybelline, Covergirl,  *
            * Smashbox, Nyx, Benefit, Revlon     *
            * L'oreal, Marcelle , Glossier       *                                                                       
            **************************************
            '''
productstList = '''
            ***********************************
            *          Our Products           *
            * Blush, Bronzer , Eyebrow        *
            * Eyeliner, Eyeshadow, Foundation *
            * Lipstick, Mascara               *
            ***********************************
            '''
def intro():
    makeupArt = '''
    ( `, 
    |`._)                                            _____________
    |   |                                           |+-----------+| 
    |   |                                           ||           ||
    |___|                                           ||           ||                                          
   (_____)                                          ||           ||
   |     |                                          |L-----------j|                         
   |     |                                         / +----+---+  /     
   |     |                                        / /    /   /  /  
   |_____|                      _______________  / +----+----+ / 
  (_______)   ;;;;;;;----------/______________/ (_____________/ '''
    
    introT = '''
          ___________________________________________                  
        /\                                           \  
        \_|         Welcome To Beauty Secrets!       |
          |  This bot helps our client find out the  |
          |  type, brand, and tags of your favorite  |
          |  makeup products.                        |
          |                                          |
          | First the bot is going to ask you what   |
          | you'd like to search by, meaning brands, |
          | types, or tags.                          |     
          |                                          |
          | When looking for brands you can type in: |  
          |     nyx, e.l.f., covergirl etc.          |
          | When looking for tags you can type in:   |
          |     chemical free, oil free, organic etc.| 
          | When looking for tags you can type in:   |
          |     foundation, lipstick, blush etc.     |
          |                                          |
          |Say exit whenever you want to done!       |    
          |  ________________________________________|__ 
          \_/__________________________________________/
        '''
    print( makeupArt )
    print( introT)


'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

def getWebData( url ):
    # gets the list of lines from the Web page at URL and split it into lines
    # import the library for accessing Web URLs
    from urllib.request import urlopen
    from urllib.error import URLError

    # attempt to get the Web page
    try:
        f = urlopen( url )
        text = f.read().decode('utf-8')
    except URLError as e:
        # if error, print error message and
        # return empty list
        print( "ERROR!\n", e.reason )
        return [ ]
    
    # return the list of lines
    lines = text.split( "," )
    return lines

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

def byBrand( brand ):   
    # get file from JSON url
    link = "https://makeup-api.herokuapp.com/api/v1/products.json?brand="
    url  = link + brand.lower()
    file = getWebData( url )
        
    # Set up variables and empty list
    name  = ""
    price = ""
    ptype = ""
    tags  = ""

    # start printing box
    dashes = "-" * 120
    box    = "+" + dashes + "+"
    print( box )
    print( "|{0:70} {1:20} {2:20} {3:7}|".format( "PRODUCT", "CATEGORY", "TAGS","PRICE"))
    print( box )
    
    # Extract info from the file
    for line in file:

        # Enter information
        if line.startswith( '''"name"''' )== True:
            name = line[7:]
            name = name.strip('''"''')
        if line.startswith( '''"price"''' ) == True:
            price = line[8:]
            price = price.strip('''"''')
        if line.startswith( '''"product_type"''' ) == True:
            ptype = line[15:]
            ptype = ptype.strip('''"''')
        if line.startswith( '''"tag_list"''' ) == True:
            tags = line
            if tags == '''"tag_list":[]''':
                tags = "None"
                print( "|{0:70} {1:20} {2:20} {3:7}|".format( name, ptype, tags, price) )
                continue
            if not tags =="[]":
                end = len( line ) - 1
                tags = line[13:end]
                print( "|{0:70} {1:20} {2:20} {3:7}|".format( name, ptype, tags, price) )
                
    # Finish printing box
    print( box )
    
'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

def byTag( tag ):   
    # get file from JSON url
    link = "https://makeup-api.herokuapp.com/api/v1/products.json?product_tags="
    tag = tag.lower()
    if tag.find( " " ) == -1:
        url  = link + tag
        file = getWebData( url )
    else:
        newT = tag.split()
        tag = newT[0] + "%20" + newT[1]
        url  = link + tag     
        file = getWebData( url )
        
    # Set up variables and empty list
    brand = ""
    name  = ""
    price = ""
    ptype = ""
    tags  = ""
    
    # start printing box
    dashes = "-" * 120
    box    = "+" + dashes + "+"
    print( box )
    print( "|{0:30} {1:65} {2:15} {3:7}|".format( "BRAND", "PRODUCT", "CATEGORY", "PRICE" ))
    print( box )
    
    # Extract info from the file
    for line in file:

        # Enter information
        if line.startswith( '''"brand"''' )== True:
            brand = line[8:]
            brand = brand.strip('''"''')
        if line.startswith( '''"name"''' )== True:
            name = line[7:]
            name = name.strip('''"''')
        if line.startswith( '''"price"''' ) == True:
            price = line[8:]
            price = price.strip('''"''')
        if line.startswith( '''"product_type"''' ) == True:
            ptype = line[15:]
            ptype = ptype.strip('''"''')
            print( "|{0:30} {1:65} {2:15} {3:7}|".format( brand, name, ptype, price) )
                
    # Finish printing box
    print( box )
    
'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

def byType( type ):   
    # get file from JSON url
    link = "https://makeup-api.herokuapp.com/api/v1/products.json?product_type="
    url  = link + type.lower()
    file = getWebData( url )
        
    # Set up variables and empty list
    brand = ""
    name  = ""
    tags  = ""
    price = ""
    
    # start printing box
    dashes = "-" * 155
    box    = "+" + dashes + "+"
    print( box )
    print( "|{0:30} {1:100} {2:15} {3:7}|".format( "BRAND", "PRODUCT", "TAGS", "PRICE" ))
    print( box )
    
    # Extract info from the file
    for line in file:

        # Enter information
        if line.startswith( '''"brand"''' )== True:
            brand = line[9:]
            brand = brand.strip('''"''')
        if line.startswith( '''"name"''' )== True:
            name = line[8:]
            name = name.strip('''"''')
        if line.startswith( '''"price"''' ) == True:
            price = line[8:]
            price = price.strip('''"''')
        if line.startswith( '''"tag_list"''' ) == True:
            tags = line
            if tags == '''"tag_list":[]''':
                tags = "None"
                print( "|{0:30} {1:100} {2:15} {3:7}|".format( brand, name, tags, price) )
                continue
            if not tags =="[]":
                end = len( line ) - 1
                tags = line[13:end]
                print( "|{0:30} {1:100} {2:15} {3:7}|".format( brand, name, tags, price) )
            
                
    # Finish printing box
    print( box )    

'''----------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''
  __  __          _____ _   _ 
 |  \/  |   /\   |_   _| \ | |
 | \  / |  /  \    | | |  \| |
 | |\/| | / /\ \   | | | . ` |
 | |  | |/ ____ \ _| |_| |\  |
 |_|  |_/_/    \_\_____|_| \_|
                              
'''
     
def main():
    # Print intro 
    intro()

    # Speak with user
    while True:
        search = input("What would you like to search by? [ brand or tag or type ] ")
        search = search.lower()
        if search == "brand":
            print( brandList ) 
            brand = input("What brand would you like to look at? ")
            print()
            byBrand( brand )
            print()
            
        elif search == "tag":
            print( tagList ) 
            tag = input("What tag would you like to look at? ")
            print()
            byTag( tag )
            print()

        elif search == "type":
            print( productstList )
            type = input("What type of makeup would you like to look at? ")
            print()
            byType( type )
            print()

        elif search == "exit":
            print( "Thanks for coming!" )
            break

main()
