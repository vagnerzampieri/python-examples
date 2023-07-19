GRAFO = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}

def person_is_seller(name):
    return name[-1] == "m"

# Big O: O(V+E)
def search(name):
  # 1. Create a queue, you can create with deque from collections
  queue_search = []
  # 2. Add all your neighbors to the queue
  queue_search += GRAFO["you"]
  print(f'queue_search {queue_search}')
  verifieds = []

  # 3. Create a loop while the queue is not empty
  while queue_search:
      # 4. Pop the first element of the queue
      person = queue_search.pop(0)

      # 5. Check if the person is not verified
      if not person in verifieds:
        # 6. Check if the person is a mango seller
        if person_is_seller(person):
            print(f"{person} is a mango seller!")
            return True
        else:
            # 7. If not, add the person's neighbors to the queue
            queue_search += GRAFO[person]
            print(f'queue_search add new neighbor {queue_search}')
            # 8. Add the person to the verifieds list
            verifieds.append(person)
  return False

search("you")