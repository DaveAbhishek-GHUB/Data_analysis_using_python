# Import required library for JSON handling
import json

# Function to load JSON data from a file
def load_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)
    
# Load the social network data from massive_data.json
data = load_data('massive_data.json')

def get_people_you_may_know(user_id, data):
    # Create a dictionary mapping user IDs to their friends (as sets for O(1) lookup)
    user_friends = {}
    for user in data['users']:
        user_friends[user['id']] = set(user['friends'])

    # Return empty list if user_id doesn't exist
    if user_id not in user_friends:
        return []
    
    # Get the set of direct friends for the given user
    direct_friends = user_friends[user_id]
    
    # Dictionary to store potential friend suggestions and their mutual friend count
    suggestions = {}
    
    # For each direct friend of the user
    for friend in direct_friends:
        # Look at each of their friends (potential mutual connections)
        for mutual in user_friends[friend]:
            # If this person isn't the user themselves and isn't already a direct friend
            if mutual != user_id and mutual not in direct_friends:
                # Increment the count of mutual friends
                suggestions[mutual] = suggestions.get(mutual, 0) + 1

    # Sort suggestions by number of mutual friends (descending)
    sorted_suggestions = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)
    # Return just the user IDs in order of most mutual friends
    return [user_id for user_id, _ in sorted_suggestions]

# Example usage: get friend suggestions for user 10
user_id = 10
recc = get_people_you_may_know(user_id, data)
print(recc)