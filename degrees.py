import csv
import sys
sys.setrecursionlimit(10**8)
from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}

#frontier
#frontier = set()
frontier = []

#checked
checked = []
mchecked=[]

#relation
relations = []
relation = []

#Sause
repeat = []
smovie = []
movdict = {}
sorce = 0

i=0


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"


    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
    #print(1)
    global i
    global sorce
    i=i+1
    #print(i)
    if i==1:
        #print("==========================================================================================")
        sorce = source

    sid = source
    tid = target
    #print(source)
    #print(target)
    #print(sorce)

    #return pathfound

    #frontier.add(sid)
    global frontier
    global checked
    global mchecked
    global relation
    global repeat
    repeat.clear()
    global smovie
    #print("here")
    flagis = True
    frontir = 0
    #smovie.clear()
    #smovie = list(people[source]["movies"])
    #print("Actor: ", people[sid]["name"])
    #print("Movies: ")
    #for a in list(people[sid]["movies"]):
    #    print(movies[a]["title"])
    """for a in smovie:
        if a not in repeat:
            repeat.append(a)
    smovie.clear()
    smovie = repeat.copy()
    """
    #print("out")

    for a in list(people[source]["movies"]):
        if a not in mchecked:
            starinmov = list(movies[a]["stars"])
            for b in starinmov:
                if b == tid:
                    relation.insert(0, [a, b])
                    if sorce != source:
                        mchecked.clear()
                        #flagis = True
                        shortest_path(sorce, source)
                        #print("=========================================================")
                        #print(relation)
                        #print("returned - > ", relation)
                        return relation
                    else:
                        #print("****************************found**********************************")
                        #flagis = False
                        #print("...")
                        return relation
            mchecked.append(a)
            for b in starinmov:
                if b not in checked:
                    frontier.extend(starinmov)
                    #print(frontier)
            starinmov.clear()
    #print("++++++++++++++++++++++++++++++++++++++++++++++++")
    frontir = frontier[0]
    checked.append(frontier[0])
    #print("Poping -> ", frontier[0])
    frontier.pop(0)
    #print("after poping -> ", frontier)
    shortest_path(frontir, target)
    #print(".")
    return relation



"""
    if flagis:
        for sta in frontier:
            if sta not in repeat:
                repeat.append(sta)
        frontier.clear()
        frontier = repeat.copy()

        for a in frontier:
            if a not in checked:
                #if tid not in frontier:     #remove
                print("in")
                frontir = frontier[0]
                checked.append(frontir)
                print("poping --> ", frontir)
                frontier.pop(0)
                print(frontir)
                shortest_path(frontir, target)
        print("Loop is over")
"""
"""
                # relation.append(sid)
                print("Checkers+++++++++++++++++++++++++++++++++=")
                if(len(relation)!=0):
                    print(relation)
                    print("---------------------------------------")
                    return relation
                else:
                    print("Directly related")
                    print("---------------------------------------------")
                    return relation
                    # relation.append(frontir)
                    # return True
                # relation = shortest_path(frontir, target)

                # relation.append(sid)
                # print(relations)
                # return relation
                print(11111111111111111111111111111111111)
            else:
                print("*********************found*******************************************************************")
                relation.append(sid)
                if (sorce != sid):
                    frontier.clear()
                    checked.clear()
                    mchecked.clear()
                    smovie.clear()
                    # smovie = []
                    shortest_path(sorce, sid)
                    return relation
                else:
                    # change flag later so that true makes function to return list instead of printing it
                    print("Same------------------------------------------------------------------------------------------------------------------")
                    return relation
"""#return relation
"""
    for a in smovie:
        if a not in mchecked:
            print("Movie name: ", movies[a]["title"])
            #frontier=frontier.union(starinmov)
            #print(starinmov)
            mchecked.append(a)
            repeat.clear()
            #print("Before raw frontier: ", frontier)
            
            #frontier = list(dict.fromkeys(frontier))
            #print("After raw frontier: ", frontier)
            #print("checked ==> ", checked)
            for sta in frontier:
                if sta in checked:
                    frontier.remove(sta)
                    print("removed ", sta)
                #print(frontier)
            #print("After raw frontier: ", frontier)
            #frontier.difference_update(checked)
            #checked.append(sid)
            repeat.clear()
            for sta in checked:
                if sta not in repeat:
                    repeat.append(sta)
            checked.clear()
            checked = repeat.copy()
            #print("After raw frontier: ", frontier)
            #frontier.remove(sid)
            #frontir = list(frontier)
            #frontir = []
            #frontir = frontier
            #print("refined frontier: ", frontier)
            if len(frontier)!=0:
                if tid not in frontier:
                    print("in")
                    frontir = frontier[0]
                    checked.append(frontir)
                    print("poping --> ", frontir)
                    frontier.pop(0)
                    checker = shortest_path(frontir, target)
                    if checker:
                        #relation.append(sid)
                        print(relation)
                        print("---------------------------------------")
                        return relation
                        #relation.append(frontir)
                        #return True
                    #relation = shortest_path(frontir, target)

                    #relation.append(sid)
                    #print(relations)
                    #return relation
                    print(11111111111111111111111111111111111)
                else:
                    print("*********************found*******************************************************************")
                    relation.append(sid)
                    if(sorce != sid):
                        frontier.clear()
                        checked.clear()
                        mchecked.clear()
                        #smovie = []

                        shortest_path(sorce,sid)
                        return True
                    else:
                        #change flag later so that true makes function to return list instead of printing it
                        print("Same------------------------------------------------------------------------------------------------------------------")
                        return True
                    #return True
            else:
                print("None???")
                return None
    print("For loop is over")
    return False
    """



    #print(sid)
    
    #raise NotImplementedError


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
