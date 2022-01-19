#tank

#input validation and sorting
def getinput():
  
  number = input("type in here ")
  valid = False
  while not valid:
    #return true when both are ture
    if number.isnumeric() and len(number) == 2:
      if int(number[0]) < 8 and int(number[1]) < 8:
          valid=True
      else:
          print("Invalid")
          number = input("Please enter again ")
    
    else:
      print("Invalid")
      number = input("Please enter again ")

  return number

#create a board by 8 and 8
w,h=8,8
#fill everywhere with 0
#0 represents there is no tank
Matrix=[[0 for x in range (w)]for y in range (h)]
#Matrix is y mojar
#1 represents there is a tankfound

#set where are the tanks
Matrix[2][7] = 1
Matrix[3][7] = 1
Matrix[7][7] = 1
Matrix[5][7] = 1
Matrix[2][6] = 1

Matrix[3][1] = 1
Matrix[1][4] = 1
Matrix[3][2] = 1
Matrix[1][5] = 1
Matrix[3][6] = 1


def A():
  #tell the user something
  print("welcome")
  print("There are 10 tanks on a 8x8 board")
  print("By entering the grid ref you can look at that square")
  print("If you find all the 10 tanks within 50 tries, you win")
  print("enter the no of roll first and then no of column")
  print("For example, to look at 3,4, enter 34")
  
  finish = False
  #attempts count
  count = 0
  #tank count
  tankfound = 0
  while not finish:
    #1 more attempt
    count = count+1
    #get the input
    grid = getinput()
    r = grid[0]
    c = grid[1]
    #if there is a tank
    if Matrix[int(r)][int(c)] == 1:
      print("You found a tank")
      #add up to no of tanks found
      tankfound = tankfound+1
      Matrix[int(r)][int(c)] = 0
      #if all the tanks are found
      if tankfound == 10:
        #you win
        finish = True
        print("You found all of the tanks!")
      #there are more
      else:
        print("There are {} more tanks to be found" .format(10-tankfound))
    #if you reach the limite
    elif count == 50:
      print("You have reached the max attempts. Game Over")
      print("There are {} more tanks to be found" .format(10-tankfound))
    else:
      print("There is no tank at gird {},{}" .format(r,c))
      print("There are {} more tanks to be found" .format(10-tankfound))
      print("try again")
  print("")
  #when u win the game
  print("You win")
  print("You used {} attempts" .format(count))


#main 
#runnnn!!!!!
A()

    




