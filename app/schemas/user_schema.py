def user_serializer(user) -> dict: 
    return {
        'id' : str(user['_id']), 
        'name' : str(user['name']),
        'role' : str(user['role'])
    }

def users_serializer(users) -> list:
    return [user_serializer(user) for user in users]