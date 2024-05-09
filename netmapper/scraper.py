import requests
from bs4 import BeautifulSoup
import json
import re
import tldextract
storage_loc = "./storage/webstor_surface.json" #This will be the final storage for all linking 
storage_loc_list = "./storage/webstor_surface_list.json" #This will contain a list of all domains this program will avoid (Already scanned)
storage_ping_queue = "./storage/webstor_queue.json" #This will contain a list of all domains the program will check (To be scanned)


start_scan = "http://protosparky.uk"


###############################################################

def scrape_and_filter_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code  200)
    if response.status_code ==  200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script tags, noscript tags, style tags, and svg tags
        for tag in soup(['script', 'noscript', 'style', 'svg']):
            tag.decompose()
        
        # Remove inline styles
        for tag in soup.find_all(True):
            if 'style' in tag.attrs:
                del tag['style']
        
        # Remove class and id attributes
        for tag in soup.find_all(True):
            if 'class' in tag.attrs:
                del tag['class']
            if 'id' in tag.attrs:
                del tag['id']
        
        return str(soup)
        
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

def read_json(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print("Json file not found ", str(e))
        return None
#############################################
def write_json(data, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print("Json file not found ", str(e))
#############################################


def extract_valid_links(html_string):
    # Create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(html_string, 'html.parser')
    
    # Find all 'a' tags
    links = soup.find_all('a')
    
    # Initialize a list to hold valid links
    valid_links = []
    
    # Iterate over each link
    for link in links:
        href = link.get('href')
        
        # Check if the link is not None and does not start with a slash (/), indicating it's a local link
        if href and not href.startswith('/'):
            # Use a regular expression to match links starting with 'http', 'https', or 'www'
            if re.match(r'(http|https|www)', href):
                valid_links.append(href)
    
    return valid_links

def get_base_domain(url):
    # Extract information from URL
    extracted_info = tldextract.extract(url)    
    # Construct the base domain name
    base_domain = f"{extracted_info.subdomain}.{extracted_info.domain}.{extracted_info.suffix}"    
    return base_domain



def setup():
    if(read_json(storage_loc) == None):
        #setup storage
        stor = {}
        write_json(stor, storage_loc)
    if(read_json(storage_loc_list) == None):
        #setup storage
        stor = []
        write_json(stor, storage_loc_list)

    if(read_json(storage_ping_queue) == None):
        #setup storage
        stor = []
        write_json(stor, storage_ping_queue)

    synchronous_ping_setup()


def synchronous_ping_setup():
    #check if something is in queue
    starting_queue = read_json(storage_ping_queue)
    if(len(starting_queue) == 0):
        #start pinging from start scan as there are no links in queue
        links = extract_valid_links(scrape_and_filter_website(start_scan))
        #check if links are already scanned
        for current_link in links:
            if(check_scanned_link(current_link)):
                #Shove in queue
                starting_queue.append(current_link)
        write_json(starting_queue,storage_ping_queue)

        #add starting link to surface webstor
        current_surface_storage = read_json(storage_loc) 
        current_surface_storage[start_scan] = []
        for current_link in links:
            current_surface_storage[start_scan].append(current_link)


def synchronous_ping():
    queue = read_json(storage_ping_queue)
    for current_link in queue:
        print("scanning current link: " + current_link)
        #iterate trough links

        #add base url to scanned links
        baseurl = get_base_domain(current_link)
        scanned_links = read_json(storage_loc_list)
        scanned_links.append(baseurl)

        #scan link




def check_scanned_link(link):
    #Returns true if link is not in the scanned list
    scanned_list = read_json(storage_loc_list)
    simple_lnk = get_base_domain(link)
    if(simple_lnk in scanned_list):
        return False
    else:
        return True


setup() #setup and run code