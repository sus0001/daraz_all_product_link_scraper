import re
import os
import yaml
import random
import itertools


class TryExcept:
    """
    A class that provides try-except functionality for retrieving element attributes and inner text.

    Methods:
    - text(element): Retrieves the inner text of an element or returns "N/A" if the element has no inner text.
    - attribute(element, attr): Retrieves the value of 
    """
    async def text(self, element):        
        try:
            elements = (await (await element).inner_text()).strip()
        except AttributeError:
            elements = "N/A"        
        return elements

    async def attributes(self, element, attr):        
        try:
            elements = await (await element).get_attribute(attr) 
        except AttributeError:
            elements = "N/A"
        return elements
    

def verifyDarazURL(url):
    """
    Check if the URL belongs to a Daraz website.

    Args:
    - url (str): The URL to check.

    Returns:
    - bool: True if the URL is not a Daraz website, False otherwise.
    """
    daraz_pattern = re.search("""^https://www.daraz.(com.np|lk|pk|com.bd)/+""", url)
    if daraz_pattern == None:
        return True
    else:
        return False


async def check_domain(url):
    """
    Check the domain of a URL and return the country it belongs to.

    Args:
    - url (str): The URL to check.

    Returns:
    - str: The name of the country the domain belongs to (Nepal, Sri Lanka, Bangladesh, or Pakistan).

    """
    
    pattern = re.search(r"(.np|.bd|.lk|.pk)", url) 
    domain_lists = {
        'np': 'Nepal',
        'lk': 'Sri Lanka',
        'bd': 'Bangladesh',
        'pk': 'Pakistan',
    }
    try:
        country =pattern.group(1).replace(".", '')
    except AttributeError:
        country = None
    return domain_lists[country]
    
                

def flat(d_lists):  
    """
    Flatten a multi-dimentional list.

    Args:
    - d_lists (list): A multi-dimensional list.

    Returns:
    - list: A flattened version of the input list.
    """  
    return list(itertools.chain(*d_lists))


def yamlMe(selectors):
    """
    Loads a YAML file containing CSS selectors and their corresponding data fields, and returns the loaded data as a dictionary.

    Args:
    - selectors (str): The name of the YAML file to load.

    Returns:
    - dict: A dictionary containing CSS selectors and their corresponding data fields.
    """
    with open(f"scrapers\\{selectors}.yaml") as file:
        sel = yaml.load(file, Loader = yaml.SafeLoader)
        return sel


def userAgents():
   """
   Loads a text file containing a list of user agent strings, and returns a random choice from the list.

   Returns:
   - str: A randomly chosen user agent string.
   """
   with open(f"{os.getcwd()}\\tools\\user-agents.txt") as f:
    agents = f.read().split("\n")
    return random.choice(agents)
   
   