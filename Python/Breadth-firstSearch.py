from collections import deque
def isSeller(person):
    return True if person.lower() == 'seller' else False
        
def breadthFirst(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while True:
        try:
            person = search_queue.popleft()
        except:
            break
        if person not in searched:
            if isSeller(person):
                print('{} is a mango seller'.format(person))
                return True
            else:
                search_queue += graph[person]
                searched.append(name)
    return False

if __name__ == "__main__":
    graph = {}
    graph['you'] = []
    graph['you'].append('Ellen')
    graph['you'].append('Amy')
    graph['you'].append('Andrew')
    graph['Ellen'] = []
    graph['Ellen'].append('Mia')
    graph['Ellen'].append('Math')
    graph['Mia'] = []
    graph['Math'] = []
    graph['Amy'] = []
    graph['Amy'].append('Seller')
    graph['Andrew'] = []
    graph['Sell'] = []
    breadthFirst('you')