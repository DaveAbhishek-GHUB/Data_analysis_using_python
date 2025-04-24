import json

def load_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

data = load_data('simple_data.json')

def display_users(data):
    print("\n========== USER INFORMATION ==========")
    print("=" * 40)
    for user in data['users']:
        print(f"User ID   : {user['id']}")
        print(f"Name      : {user['name']}")
        print(f"Friends   : {', '.join(str(friend) for friend in user['friends'])}")
        print("=" * 40)

def display_pages(data):
    print("\n========== PAGE INFORMATION ==========")
    print("=" * 40)
    for page in data['pages']:
        print(f"Page ID   : {page['id']}")
        print(f"Name      : {page['name']}")
        print("=" * 40)


display_users(data)
display_pages(data)