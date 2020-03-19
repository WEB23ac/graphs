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
        friendship_count = (num_users * avg_friendships) // 2

        for i in range(friendship_count):
            friend_1 = random.randrange(1, num_users)
            print('friend_1', friend_1)
            friend_2 = random.randrange(1, num_users)
            print('friend_2', friend_2)

            self.add_friendship(friend_1, friend_2)
        # for user_id in self.users:

        #     for friend_id in range(user_id+1, self.last_id+1):
        #         possible_friendships.append((user_id, friend_id))

        # random.shuffle(possible_friendships)

        # # Create friendships where n = avg_friendships * num_users ///2
        # # avg_friendships = total_friendships / num_users
        # for i in range(num_users * avg_friendships // 2):
        #     friendship = possible_friendships[i]
        #     self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}
        queue = []
        queue.append([user_id])

        for friend in self.friendships[user_id]:
            path = [user_id, friend]
            queue.append(path)

        while len(queue) > 0:
            curr_path = queue.pop(0)
            curr_user = curr_path[-1]
            if not curr_user in visited:
                for friend in self.friendships[curr_user]:
                    new_path = curr_path.copy()
                    new_path.append(friend)
                    queue.append(new_path)
                visited[curr_user] = curr_path

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
