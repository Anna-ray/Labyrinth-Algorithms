from Labyrinth import *

class DFS:
    def __init__(self,start,end, chemin, visited, neighbors, grid_2d):
        self.__init__(start, end, chemin, visited, neighbors, grid_2d)

def DFS(grid_2d, goal):

    visited_nodes = []
    neighbors = []
    goal = cases_with_coordinates(goal, grid_2d.cases)
    current_case = cases[0]

    while (current_case != goal):
        # draw the first  case of searching way
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
solution = DFS(grid_2d, (cases[-1].x_case, cases[-1].y_case))

if solution:
                print("Congratulations, you solved the maze!")
                pygame.quit()
else:
                print("NO SOLUTION FOUND!")
                pygame.quit()

while run:
    pass