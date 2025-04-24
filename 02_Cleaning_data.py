import json

def load_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)
    

def clean_data(data):
    data['users'] = [user for user in data['users'] if user['name'].strip()]
    data['users'] = [user for user in data['users'] if user['friends'] != [] and user['liked_pages'] != []]
    for user in data['users']:
        user['friends'] = list(set(user['friends']))

    # Remove duplicate pages
    unique_pages = {}
    for page in data['pages']:
        unique_pages[page['id']] = page
    data['pages'] = list(unique_pages.values())
    return data

data = load_data('uncleaned_data.json')
cleaned_data = clean_data(data)
json.dump(cleaned_data, open('cleaned_data.json', 'w'), indent=4)
print("Data cleaned and saved to cleaned_data.json")