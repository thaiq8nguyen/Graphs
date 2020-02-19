import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

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

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i + 1}")
        # Create friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        
        random.shuffle(possible_friendships)
        print("----")
        print(possible_friendships)
        print("----")

        # Grab the first N parts from the list and create those friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])
        
        # avg_friendships = total_friendships / num_users
        # total_friendships = avg_friendships * num_users
        # N = avg_friendships * num_users // 2


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        def bfs(starting_vertex, destination_vertex):
        
            # 1. Create an empty queue and push a path to the starting vertex_id
            q = Queue()
            q.enqueue([starting_vertex])
            # 2. Create a set to store visited vertices
            visited = set()
            # 3. While the queue is not empty
            while q.size() > 0:
                # 4. dequeue the first path
                last_path = q.dequeue()
                # 5. Grab the last vertex from the path
                last_vertex = last_path[-1]
                # 6. If that vertex has not been visited:
                if last_vertex not in visited:
                    # 7. Check if it's the destination
                    if last_vertex == destination_vertex:

                        # 8. If so:
                        # 9. Return path
                        return last_path
                    # 9. Mark is as visited
                    visited.add(last_vertex)
                    # 10. Add a path to its neighbors to the back of the queue
                    for v in self.friendships[last_vertex]:

                        # 11. Copy the path
                        new_path = [*last_path]

                    # 12. Append the neighbor to the back of the queue
                        new_path.append(v)
                        q.enqueue(new_path)
        
        for u in self.users:
            visited[u] = bfs(user_id,u)

        # Breath first search guarantees a shortest path
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    # print(sg.users)
    connections = sg.get_all_social_paths(1)
    print(connections)
