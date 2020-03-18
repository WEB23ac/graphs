import random


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # * Write a loop that calls create user the right amount of times

        # Create friendships
        # To create N friendships
        # create a list with all possible friendship cobminations
        # Shuffle the list, then grab the first N elements from the list

        # Add users
        for i in range(num_users):
            self.add_user(f'User {i+1}')

        possible_friendships = []

        for user_id in self.users:
            for friend_id in range(user_id+1, self.last_id+1):
                possible_friendships.append((user_id, friend_id))

        random.shuffle(possible_friendships)

        # Create friendships where n = avg_friendships * num_users ///2
        # avg_friendships = total_friendships / num_users
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

        # Create friendships

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        queue = []
        queue.append([user_id])

        # * helper function to get a user_id friends
        # def get_friends(friendships, user_id):
        #     friends = friendships[user_id]
        #     return friends
        for friend in self.friendships[user_id]:
            path = [user_id, friend]
            queue.append(path)

        while len(queue) > 0:
            curr_path = queue.pop(0)
            curr_user = curr_path[-1]
            # print(f'current user is {curr_user}')
            # print('visited', visited)
            if not curr_user in visited:
                for friend in self.friendships[curr_user]:
                    # print(f'finding {user_id}s friend, {friend}')
                    new_path = curr_path.copy()
                    new_path.append(friend)
                    # print(f'the new path is {new_path}')
                    queue.append(new_path)
                visited[curr_user] = curr_path

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    for user in sg.users:
        print('sg.users user', user)
    # print('users in graph', sg.users)
    connections = sg.get_all_social_paths(1)
    print(connections)
