from Labyrinth import *

class IDFS:
 def __init__(self,DFS_WITH_LIMITE):
        self.DFS_WITH_LIMITE = DFS_WITH_LIMITE

def IDFS(grid2d, but):
            sol_for_limit = []
            found = False
            limit = 0
            while found == False:
                sol_for_limit.append(DFS_WITH_LIMITE(grid2d, but, limit)[0])
                found = DFS_WITH_LIMITE(grid2d, but, limit)[1]
                limit += 1
                print("For limit number", limit, " :", sol_for_limit)
            return sol_for_limit


def DFS_WITH_LIMITE(grid_2d, goal, limite):
   visited_nodes = []
   neighbors = []
   found = False
   neighbors_of_neighbors = []
   goal= cases_with_coordinates(goal, grid_2d.cases)
   current_case = (cases[0], 0)

   while (current_case[0] != goal and current_case[1] <= limite):

       pygame.draw.rect(window, TAUPE, (current_case[0].x_case + 10, current_case[0].y_case + 10, width_case - 20, width_case - 20))
       pygame.display.update()


       visited_nodes.append(current_case[0])

       if current_case[0].up != (0, 0) and cases_with_coordinates(current_case[0].up, cases) not in visited_nodes and cases_with_coordinates(
               current_case[0].up, cases) not in neighbors:
           neighbors_of_neighbors.insert(0, (cases_with_coordinates(current_case[0].up, cases), current_case[1] + 1))
           neighbors.insert(0, cases_with_coordinates(current_case[0].up, cases))

       if current_case[0].right != (0, 0) and cases_with_coordinates(current_case[0].right, cases) not in visited_nodes and cases_with_coordinates(
               current_case[0].right, cases) not in neighbors:
           neighbors_of_neighbors.insert(0, (cases_with_coordinates(current_case[0].right, cases), current_case[1] + 1))
           neighbors.insert(0, cases_with_coordinates(current_case[0].right, cases))

       if current_case[0].left != (0, 0) and cases_with_coordinates(current_case[0].left, cases) not in visited_nodes \
               and cases_with_coordinates(current_case[0].left, cases) not in neighbors:
           neighbors_of_neighbors.insert(0, (cases_with_coordinates(current_case[0].left, cases), current_case[1] + 1))
           neighbors.insert(0, cases_with_coordinates(current_case[0].left, cases))

       if current_case[0].down != (0, 0) and cases_with_coordinates(current_case[0].down, cases) not in visited_nodes \
               and cases_with_coordinates(current_case[0].down, cases) not in neighbors:
           neighbors_of_neighbors.insert(0, (cases_with_coordinates(current_case[0].down, cases), current_case[1] + 1))
           neighbors.insert(0, cases_with_coordinates(current_case[0].down, cases))



       if current_case[0] == cases[0]:
        current_case = neighbors_of_neighbors[0]
        neighbors_of_neighbors.remove(neighbors_of_neighbors[0])
        neighbors.remove(neighbors[0])

       else:
        intermediate = current_case
        if intermediate in neighbors:
           neighbors_of_neighbors.remove(intermediate)
        current_case = neighbors_of_neighbors[0]
        neighbors_of_neighbors.remove(current_case)
        neighbors.remove(current_case[0])

   time.sleep(0.3)

   if current_case[0] == goal:
       visited_nodes.append(current_case[0])
       found = True

   sol = []

   for v in visited_nodes:
       sol.append((v.x_case, v.y_case))

   return sol, found

class DFS:
    def __init__(self, start, end, chemin, visited, neighbors, grid_2d):
        self.__init__(start, end, chemin, visited, neighbors, grid_2d)

def DFS(grid_2d, goal):

    visited_nodes = []
    neighbors = []
    goal = cases_with_coordinates(goal, grid_2d.cases)
    current_case = cases[0]

    while (current_case != goal):

        pygame.draw.rect(window, TAUPE, (current_case.x_case + 10, current_case.y_case + 10, width_case - 20, width_case - 20))
        pygame.display.update()

        print("CURRENT CASE COORDINATES ARE:")
        print(current_case.x_case, current_case.y_case)
        print("MOVES CASES COORDINATES:", "UP:"+str(current_case.up), "DOWN:"+str(current_case.down), "RIGHT:"+str(current_case.right), "LEFT:"+ str(current_case.left))

        visited_nodes.append(current_case)

        if current_case.up != (0, 0) and cases_with_coordinates(current_case.up, cases) not in visited_nodes \
                and cases_with_coordinates(current_case.up, cases) not in neighbors:
            neighbors.insert(0, cases_with_coordinates(current_case.up, cases))
            print(" UP MOVE !")
        if current_case.right != (0, 0) and cases_with_coordinates(current_case.right, cases) not in visited_nodes \
                and cases_with_coordinates(current_case.right, cases) not in neighbors:
            neighbors.insert(0, cases_with_coordinates(current_case.right, cases))
            print(" RIGHT MOVE !")
        if current_case.left != (0, 0) and cases_with_coordinates(current_case.left, cases) not in visited_nodes \
                and cases_with_coordinates(current_case.left, cases) not in neighbors:
            neighbors.insert(0, cases_with_coordinates(current_case.left, cases))
            print(" LEFT MOVE !")
        if current_case.down != (0, 0) and cases_with_coordinates(current_case.down, cases) not in visited_nodes \
                and cases_with_coordinates(current_case.down, cases) not in neighbors:
            neighbors.insert(0, cases_with_coordinates(current_case.down, cases))
            print(" DOWN MOVE !")



        if current_case == cases[0]:
            current_case = neighbors[0]
            neighbors.remove(neighbors[0])
        else:
            intermediate = current_case
            if intermediate in neighbors:
                neighbors.remove(intermediate)
            current_case = neighbors[0]
            neighbors.remove(current_case)

        time.sleep(0.3)

        print("THE VISITED NODES ARE:")
        liste = []
        for i in visited_nodes:
            liste.append((i.x_case,i.y_case))


        print(liste)
        print("***************!****************")

    return visited_nodes



new_laby = labyrinth(25, 25, 25, 25, 30)
solution = IDFS(grid_2d, (cases[-1].x_case, cases[-1].y_case))

if solution:
                print("Congratulations, you solved the maze!")
                pygame.quit()
else:
                print("NO SOLUTION FOUND!")
                pygame.quit()

while run:
    pass






