"""
Social media connections can serve as a means of recognizing relationships among a group of people. These relationships can be represented as an undirected graph where edges join related people. A group of n social media friends is uniquely numbered from 1 to friend_nodes. The group of friends is expressed as a graph with friend_edges undirected edges, where each pair of best_friends is directly connected by an edge. A trio is defined as a group of three best friends. The friendship score for a person in a trio is defined as the number of best friends that person has outside of the trio. The friendship sum for a trio is the sum of trio's friendship scores.

Given friendship connection data, create an undirected graph and determine the minimum friendship sum for all trios of best friends in the group. If no such trio exists, return -1
"""

def social_media_connections(friends_from, friends_to):
    # no graph object in python so we use dict
    graph = {} # {1: {2, 3}, 2: {1, 3, 4}, 3: {1, 2, 4}, 4: {2, 3, 5}, 5: {4}}

    friend_groups = set()
    """
    A python Set is a unordered and mutable collection of unique elements written in curlys.
    Any immutable data type can be used inside a set (str, int). add()
    set_of_numbers = {1, 2, 3, 4}
    """

    min_friends_sum = -1

    for i, j in zip(friends_from, friends_to): # loops through each pair of input arrays (arr1[0], arr2[0])
        graph[i], graph[j] = graph.get(i, set()), graph.get(j, set()) # key values {int: {set}}
        graph[i].add(j) # add() won't add dupes
        graph[j].add(i)

    for person in graph: # start with a person: 1
        friends = graph[person] # find the friends of that person: {2, 3}
        for friend in friends: # for each of the friends
            import pdb; pdb.set_trace()
            friend_friends = graph[friend] # Find the friends of the friend: {1, 3, 4}
            shared_friends = friend_friends.intersection(friends)
            """
            At this point:
                - 1 is friends with 2 and 3
                - 2 is friends with 1, 3 and 4
            3 is a mutual friend of 1 and 2, making 1, 2, and 3 a trio
            """
            if shared_friends:
                for shared_friend in shared_friends:
                    trio = tuple(sorted([person, friend, shared_friend]))
                    """
                    Create a sorted tuple of the 3 friends: (1,2,3)
                    """
                    if trio not in friend_groups:
                        friend_groups.add(trio)
                        friends_sum = (len(friends) + len(friend_friends) + len(graph[shared_friend])) - 6
                        """

                        Degree centrality is a count of how many edges it has
                        """
                        if min_friends_sum == -1:
                            min_friends_sum = friends_sum
                        else:
                            min_friends_sum = min(min_friends_sum, friends_sum)
    return print(min_friends_sum)


if __name__ == "__main__":
    social_media_connections([1,1,2,2,3,4], [2,3,3,4,4,5]) # Returns 2
    social_media_connections([1,2,2,3,4,5], [2,4,5,5,5,6]) # Returns 3
    social_media_connections([1], [2]) # Returns -1 