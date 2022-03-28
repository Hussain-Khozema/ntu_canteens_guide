import pygame
import tkinter as tk
import numpy
pygame.init()
import time

kfc_food = {('halal', 'Zinger Burger'):5.3,('halal','Signature Grilled Chicken'):5.2,('halal','Original Chicken'):3.4,('halal','Spicy Chicken'):3.4,('halal','Tori Katsu Burger'):5.9,('halal','Zinger Stacker Burger'):7.2}
kfc = {'Name':'KFC','Location':(319,253),'Rating':4.6,'Food':kfc_food}

mac_food = {('halal',"McFlurry"):2.25,('halal','Big Mac'):7.65,('halal','McSpicy Burger'):5.8,('halal','McChicken Burger'):3.95,('halal','Cheeseburger'):6.2}
mac = {'Name':'McDonalds','Location':(305,279),'Rating':4.9,'Food':mac_food}

koufu_food = {('halal',"Fried Fish Fillet Noodle"):3.6,('non-halal','Chinese Chicken Rice'):3.0,('veg','Vegetarian Economic Rice'):3.5,('veg','Vegetarian Noodle'):2.5,('halal','Pasta'):4.2,('halal','Roti Prata set'):3.8,('halal','Nasi Padang'):4.5}
koufu = {'Name':'Koufu','Location':(210,624),'Rating':3.8,'Food':koufu_food}

canteen1_food = {('halal',"Crispy Chicken Don"):4.9,('non-halal','Spicy Pot'):5.0,('halal','Mixed Beef Noodle'): 4.5, ('halal','Beef Meatball Noodle'):4.5, ('non-halal','Economic Rice'): 5.0,('halal','Chicken Chop And Fries'): 5.0}
canteen1 = {'Name':'Food Court 1','Location':(564,589),'Rating':3.1,'Food':canteen1_food}

canteen2_food = {('halal',"Ayam Penyet"):4.8,('non-halal','Yong Tau Foo'):3.8, ('non-halal','Chicken Rice'):2.8,('non-halal','Roasted Pork Rice'):3.5, ('halal','Curry Omelette Rice'):5.0, ('non-halal','Chinese Dim Sum'):4.3,('non-halal','Economic Rice'): 3.5, ('non-halal','Bibimbap'): 3.3}
canteen2 = {'Name':'Food Court 2','Location':(620,480),'Rating':2.9,'Food':canteen2_food}

canteen9_food = {('halal',"Chicken Chop Rice"):5.0,('non-halal','Pork Chop Rice'):5.2,('halal','Dosa Masala'):2.5,('non-halal','Fried Rice'):3.0}
canteen9 = {'Name':'Food Court 9','Location':(799,275),'Rating':4.3,'Food':canteen9_food}

canteen11_food = {('non-halal',"Economic Rice"):4.2,('non-halal','Si Chuan Cuisine'):4.0,('non-halal','Dried Ban Mian'):3.0,('non-halal','Ban Mian Soup'):3.0,('veg','Fruits'):1.5}
canteen11 = {'Name':'Food Court 11','Location':(959,195),'Rating':4.2,'Food':canteen11_food}

canteen13_food = {('halal',"Crispy Chicken Chop"):6.0,('halal','Egg Chicken Chop'):6.0,('halal','Fish Chop'):5.0,('non-halal','Grilled Pork Don'):5.0,('non-halal','Mee Po'):3.5}
canteen13 = {'Name':'Food Court 13','Location':(566,86),'Rating':2.1,'Food':canteen13_food}

canteen16_food = {('non-halal',"Pork Ramen"):5.3,('halal','Chicken Ramen'):5.0,('halal','Beef Burger'):5.8,('halal','Chicken Chop Noodle'):4.9,('non-halal','Curry Pork Noodle'):5.0}
canteen16 = {'Name':'Food Court 16','Location':(499,165),'Rating':3.5,'Food':canteen16_food}

quad_food = {('halal',"Spicy pot noodle"):4.5,('halal','Malay Economic Rice'):4.0,('non-halal','Korean Bibimbap'):3.9,('non-halal','Kimchi Set Meal'):6.0,('non-halal','Kimchi Ramen'):4.0}
quad = {'Name':'Quad Cafe','Location':(185,361),'Rating':3.7,'Food':quad_food}

blue = [('Opp Lee Wee Nam Library',(368,241)), ('Opp Halll 3',(487,122)), ('Opp Hall 14',(662,54)), ('Opp Hall 23',(979,126)),  ('Opp Hall 10',(964,256)), ('Nanyang Heights',(739,374)),\
        ('Hall 6',(609,599)), ('Opp Hall 5',(467,783)), ('Opp Innnovation Centre',(245,726)), ('School of SPMS',(113,563)), ('Opp WKWSCI',(34,483)), ('Opp CEE',(183,252))]

red =  [('Lee Wee Nam Library',(379,254)), ('School of Biological Sciences',(137,329)), ('School of Comms Studies',(45,487)), ('Hall 7',(65,700)), ('Hall 4',(435,743)),\
        ('Hall 1',(601,729)), ('Canteen 2',(641,467)), ('Hall 8',(744,372)), ('Hall 11',(976,127)), ('Hall 23',(853,91)), ('Hall 12',(549,56))]

canteenlist = [kfc,mac,koufu,canteen1,canteen2,canteen9,canteen11,canteen13,canteen16,quad]


class user_input():
    def initialise(self,text):
        self.text = text
        self.answer = ''
        self.screen = tk.Tk()
        self.textbox = None
        self.answer = None
        heading = tk.Label(self.screen,text = self.text).grid(row=0)
        self.textbox = tk.Entry(self.screen)
        self.textbox.grid(row=0, column=1)
        tk.Button(self.screen, text='Submit',command = self.get_price).grid(row=0, column=5)
        #Start the GUI
        self.screen.mainloop()
        return self.answer

    def get_price(self):
        global answer
        self.answer = self.textbox.get()
        self.screen.destroy()
        return self.answer
    
class button():
    def __init__(self, color, x,y,width,height, text='',image = None):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.image = image
        return

    def draw(self,screen,text_colour,text_size):
        if self.image == None:
            pygame.draw.rect(screen, self.color, (self.x,self.y,self.width+2,self.height))
            pygame.display.update()
            insert_text(screen,self.text,'arial',text_size,text_colour,self.x+1,self.y)
            return self
        else:
            screen.blit(pygame.transform.scale(self.image, (self.width,self.height)), (self.x,self.y))
            insert_text(screen,self.text,'arial',text_size,text_colour,self.x+1,self.y)
            return self

    def isClicked(self, mousepos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if (mousepos[0] > self.x) and (mousepos[0] < self.x + self.width):
            if (mousepos[1] > self.y) and (mousepos[1] < self.y + self.height):
                return True
        return False   


def insert_text(screen,text,font,size,colour,x_pos,y_pos):
    pygame.init()
    text_font = pygame.font.SysFont(font, size)
    text=text_font.render(text, True, colour)
    screen.blit(text,(x_pos,y_pos))
    return text.get_rect()

def bubble_sort(vec):
    l = len(vec)
    loop = False # Check whether we do any changes when we go through one loop
    for i in range(l):
        for j in range(l - i- 1):
            if vec[j] > vec[j+1]:
                temp =vec[j+1]
                vec[j+1] = vec[j]
                vec[j] = temp
                loop = True
        if not loop:#break the loop if we don't do any changes in 1 loop
                break
    return vec

def back_exit_clicked(screen):
    image_exit = pygame.image.load('exit.png')
    text_back = button((255,255,255),430,730,200,60,'',image_exit).draw(screen,(0,0,0),40)
    insert_text(menu_screen,'Back','arial',50,(255,255,255),480,730)
    text_quit = button((255,255,255),730,730,200,60,'',image_exit).draw(screen,(0,0,0),40)
    insert_text(menu_screen,'Exit','arial',50,(255,255,255),790,730)
    text_quit2 = button((211,211,211),900,730,0,0,'').draw(screen,(0,0,0),50)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return False 
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousepos = pygame.mouse.get_pos()
                if text_back.isClicked(mousepos):
                    display_menu(coordinates,price,food)
                    return True
                elif text_quit.isClicked(mousepos):
                    return False
                

#Main menu
def display_menu(coordinates,price,food):
    menu_screen = pygame.display.set_mode((1400,800))
    image_map = pygame.image.load('map.png')
    image_background = pygame.image.load('background1.png')
    image_bus = pygame.image.load('bus.png')
    image_update = pygame.image.load('update.png')
    image_canteen = pygame.image.load('canteen1.png')
    image_button = pygame.image.load('button.png')
    image_button1 = pygame.image.load('button1.png')
    image_location = pygame.image.load('location_bg.png')
    image_submit = pygame.image.load('submit_button.png')
    image_distance = pygame.image.load('distance.png')
    image_rank = pygame.image.load('rank.png')
    image_money = pygame.image.load('money.png')
    image_food = pygame.image.load('food.png')
    image_exit = pygame.image.load('exit.png')
    image_logo = pygame.image.load('ntulogo.png')
    menu_screen.blit(pygame.transform.scale(image_background, (1400, 800)), (0, 0))
    menu_screen.blit(pygame.transform.scale(image_logo, (150, 150)), (150, 25))
    menu_screen.blit(pygame.transform.scale(image_canteen, (110, 110)), (530, 220))
    menu_screen.blit(pygame.transform.scale(image_map, (100, 100)), (535, 370))
    menu_screen.blit(pygame.transform.scale(image_update, (100, 100)), (535, 590))
    menu_screen.blit(pygame.transform.scale(image_bus, (110, 110)), (535, 460))
    menu_screen.blit(pygame.transform.scale(image_distance, (100, 100)), (730, 210))
    menu_screen.blit(pygame.transform.scale(image_rank, (100, 100)), (730, 330))
    menu_screen.blit(pygame.transform.scale(image_money, (100, 100)), (730, 480))
    menu_screen.blit(pygame.transform.scale(image_food, (90, 90)), (730, 610))
    text_guide = insert_text(menu_screen,'NTU Food and Beverage Guide','bahnschrift',60,(255,255,255),350,40)
    
    text_canteens =     button((255,165,0),60,200,465,160,'',image_button).draw(menu_screen,(255,255,255),50)
    insert_text(menu_screen,'Display all canteens','arial',55,(0,0,0),85,240)
    
    text_transport =    button((255,165,0),60,480,465,100,'',image_button).draw(menu_screen,(255,255,255),50)
    insert_text(menu_screen,'Getting there','arial',55,(0,0,0),140,490)
    
    text_updateinfo =   button((255,165,0),60,590,465,100,'',image_button).draw(menu_screen,(255,255,255),50)
    insert_text(menu_screen,'Update canteen info','arial',55,(0,0,0),85,605)

    
    if coordinates == None:
            text_coordinates  = button((255,255,255),60,370,465,100,'',image_button).draw(menu_screen,(255,255,255),50)
            insert_text(menu_screen,'Get location coordinates','arial',50,(0,0,0),70,385)
    else:
        text_coordinates  = button((255,165,0),60,370,465,100,'',image_button).draw(menu_screen,(255,255,255),50)
        insert_text(menu_screen,'Location: (x- {}, y- {})'.format(coordinates[0],coordinates[1]),'arial',50,(0,0,0),63,385)
        
    if price == None:
        text_price =        button((211,211,211),850,480,365,80,'',image_button1).draw(menu_screen,(0,0,0),60)
        insert_text(menu_screen,'Search by price','arial',50,(0,0,0),890,490)
    else:
        text_price =        button((211,211,211),850,480,365,80,'',image_button1).draw(menu_screen,(0,0,0),60)
        insert_text(menu_screen,'Price: ${} - ${}'.format(price.split('-')[0],price.split('-')[1]),'arial',50,(0,0,0),860,490)
        
    text_distance =         button((211,211,211),850,220,365,80,'',image_button1).draw(menu_screen,(0,0,0),60)
    insert_text(menu_screen,'Sort by distance','arial',50,(0,0,0),880,230)
    text_rank =             button((211,211,211),850,350,365,80,'',image_button1).draw(menu_screen,(0,0,0),60)
    insert_text(menu_screen,'Sort by rank','arial',50,(0,0,0),900,360)
    if food == None:
        text_food =         button((211,211,211),850,600,365,80,'',image_button1).draw(menu_screen,(0,0,0),60)
        insert_text(menu_screen,'Search food','arial',50,(0,0,0),905,610)
    else:
        text_food =         button((211,211,211),850,600,365,80,'',image_button1).draw(menu_screen,(0,0,0),60)
        insert_text(menu_screen,'Food: {}'.format(food),'arial',50,(0,0,0),860,610)
    text_submit_food =      button((255,165,0),1230,610,150,50,'',image_submit).draw(menu_screen,(0,0,0),60)
    insert_text(menu_screen,'Submit','arial',40,(0,0,0),1250,610)
    text_submit_price =     button((255,165,0),1230,490,150,50,'',image_submit).draw(menu_screen,(0,0,0),60)
    insert_text(menu_screen,'Submit','arial',40,(0,0,0),1250,490)
    text_exit =             button((211,211,211),555,700,200,60,'',image_exit).draw(menu_screen,(0,0,0),60)
    insert_text(menu_screen,'Exit','arial',50,(255,255,255),620,700)
    pygame.display.update()
    return text_canteens,text_coordinates,text_price,text_distance,text_rank,text_food,text_submit_food,text_submit_price,text_exit,text_updateinfo,text_transport,menu_screen
    

#Display getting coordinates   
def get_user_location():
    pygame.init()
    coordinates_screen = pygame.display.set_mode((1400,800))
    image = pygame.image.load('ntucampus.png')
    image2 = pygame.image.load('location_bg.png')
    coordinates_screen.blit(pygame.transform.scale(image, (1000, 800)), (0, 0))
    coordinates_screen.blit(pygame.transform.scale(image2, (400, 800)), (1001, 0))
    text_guide = insert_text(coordinates_screen,'NTU F&B Guide','arial',60,(0,0,128),1020,100)
    click_location = insert_text(coordinates_screen,'Click on your location','arial',40,(0,0,128),1030,200)
    coordinates = insert_text(coordinates_screen,'Your coordinates: ','arial',35,(0,0,128),1070,300)
    pygame.display.update()
    
    #get coordinates
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousepos = pygame.mouse.get_pos()
                if mousepos[0]<=1000:
                    mark = insert_text(coordinates_screen,'x','arial',30,(0,0,0),mousepos[0]-5,mousepos[1]-20)
                    coordinates = insert_text(coordinates_screen,('X:{} , Y:{}'.format(mousepos[0],mousepos[1])),'arial',35,(0,0,0),1100,400)
                    exiting = insert_text(coordinates_screen,'exiting...','arial',35,(0,0,0),1120,500)
                    pygame.display.update()
                    return mousepos

#Display all canteens
def display_all_canteens(screen,coordinates,price,food):
    screen.fill((211,211,211))
    image = pygame.image.load('display_distance.png')
    screen.blit(pygame.transform.scale(image, (1400, 800)), (0, 0))
    i = 50
    insert_text(screen,'Name','arial',20,(0,0,0),30,10)
    insert_text(screen,'Rating','arial',20,(0,0,0),130,10)
    insert_text(screen,'Location','arial',20,(0,0,0),220,10)
    insert_text(screen,'Food','arial',20,(0,0,0),350,10)
    #display all canteens
    for canteen in canteenlist:
        name = '{}'.format(canteen['Name'])
        location = '{}'.format(canteen['Location'])
        rating = '{}'.format(canteen['Rating'])
        insert_text(screen,name,'arial',15,(0,0,0),30,i)
        insert_text(screen,rating,'arial',15,(0,0,0),135,i)
        insert_text(screen,location,'arial',15,(0,0,0),220,i)
        food_x_first = 350
        food_x_second = 350
        food_count = 0
        for foods in canteen['Food']:
            food_text = ('{} ({}) : ${}'.format(foods[1],foods[0],canteen['Food'][foods]))
            if food_count<=4:
                position = insert_text(screen,food_text,'arial',15,(0,0,0),food_x_first,i)
                food_x_first = food_x_first + position[2] + 20
            else:
                position = insert_text(screen,food_text,'arial',15,(0,0,0),food_x_second,i+30)
                food_x_second = food_x_second + position[2] + 20
            food_count += 1
        i = i +70
    
    return back_exit_clicked(screen)




#Updating Information
def get_food_result(): 
    global result
    canteen = variable_canteen.get()
    food_type = variable_type.get()
    food_name = food_text.get()
    food_cost = food_price.get()
    result = ('{},{},{},{}'.format(canteen,food_type,food_name,food_cost)).split(',')
    master.destroy()
    return result

def add_food_screen(): #Adding food screen
    global variable_canteen,food_text,food_price,master,variable_type
    canteen_list = []
    for canteen in canteenlist:
         canteen_list.append(canteen['Name'])
    master = tk.Tk()
    #canteen dropdown
    variable_canteen = tk.StringVar(master)
    variable_canteen.set("Chooose canteen") # default value
    canteen_menu = tk.OptionMenu(master, variable_canteen, *canteen_list)
    canteen_menu.grid(row= 0,column = 0,sticky = tk.NE)

    variable_type = tk.StringVar(master)
    variable_type.set("Chooose food type") # default value
    food_type = tk.OptionMenu(master, variable_type, 'halal','veg','non-halal')
    food_type.grid(row =0,column = 3)
    #food textfield
    food_text = tk.Entry(master,textvariable = tk.StringVar(),width = 40)
    food_text.insert(0,'Enter food here')
    food_text.grid(row= 0,column = 4)
    
    #price textfield
    food_price = tk.Entry(master,textvariable = tk.StringVar(),width = 20)
    food_price.insert(0,'Enter price here')
    food_price.grid(row= 0,column = 5)
    
    #submit button
    tk.Button(master, text='Submit', command = get_food_result).grid(row=0, column=6)
    master.mainloop()
    return result

def get_rating_result():
    global result
    canteen = variable.get()
    new_rating = rating_entry.get()
    result = ('{},{}'.format(canteen,new_rating)).split(',')
    master.destroy()
    return result

def update_rating_screen(): #Updating Rating screen
    global variable,rating_entry,master
    master = tk.Tk()
    canteen_list = []
    for canteen in canteenlist:
        canteen_list.append(canteen['Name'])
    variable = tk.StringVar(master)
    variable.set("Chooose canteen") # default value
    canteen_menu = tk.OptionMenu(master, variable, *canteen_list)
    canteen_menu.grid(row= 0,column = 0,sticky = tk.NE)

    rating_entry = tk.Entry(master,textvariable = tk.StringVar(),width = 20)
    rating_entry.insert(0,'Enter new rating: ')
    rating_entry.grid(row= 0,column = 1)

    tk.Button(master, text='Submit', command = get_rating_result).grid(row=0, column=5)
    master.mainloop()
    return result

def updatingFood(inputList):
  for eachCanteen in canteenlist:
    if eachCanteen['Name'] == inputList[0]:
      eachCanteen['Food'][str(inputList[1]),str(inputList[2])] = float(inputList[3])
      return eachCanteen['Food']

def updatingRating(inputList):
  for eachCanteen in canteenlist:
    if eachCanteen['Name'] == inputList[0]:
      eachCanteen['Rating'] = float('{:.1f}'.format((float(inputList[1]) + eachCanteen['Rating']) / 2))
      return eachCanteen['Rating']
    
def display_updateinfo(screen):
    screen.fill((211,211,211))
    image = pygame.image.load('display_distance.png')
    image_button = pygame.image.load('button.png')
    screen.blit(pygame.transform.scale(image, (1400, 800)), (0, 0))
    insert_text(screen,'Update Information','arial',70,(0,0,0),400,100)
    addfood_button = button((255,165,0),500,300,300,40,'',image_button).draw(screen,(0,0,255),40)
    insert_text(screen,'Add Food','arial',40,(0,0,0),570,298)
    updaterating_button = button((255,165,0),500,400,300,40,'',image_button).draw(screen,(0,0,255),40)
    insert_text(screen,'Give Rating','arial',40,(0,0,0),560,396)
    random_button = button((211,211,211),1000,600,0,0,'',None).draw(screen,(0,0,255),40)
    pygame.display.update()
    while True:
        mousepos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if addfood_button.isClicked(mousepos):
                    result = add_food_screen()
                    screen.fill((211,211,211))
                    screen.blit(pygame.transform.scale(image, (1400, 800)), (0, 0))
                    updatingFood(result)
                    insert_text(screen,'{} has been added to {}'.format(result[2],result[0]),'arial',40,(0,0,0),400,400)
                    return back_exit_clicked(screen)
                elif updaterating_button.isClicked(mousepos):
                    result = update_rating_screen()
                    newrating = updatingRating(result)
                    screen.fill((211,211,211))
                    screen.blit(pygame.transform.scale(image, (1400, 800)), (0, 0))
                    insert_text(screen,'Rating for {} has been updated.'.format(result[0]),'arial',40,(0,0,0),400,350)
                    insert_text(screen,'New rating is: {}'.format(newrating),'arial',40,(0,0,0),500,450)
                    return back_exit_clicked(screen)


#Sort by rank
def sort_by_rank(canteenlist):
    canteen = [i for i in canteenlist]
    rating = [i['Rating'] for i in canteen]
    sorted_rating = [i for i in rating]

    #Sort by using bubble algorithm
    sorted_rating = bubble_sort(sorted_rating)
    sorted_rating.reverse()
    
    results = {}
    
    #Sort the key from highest rating to lowest rating
    for i in range(len(rating)):
        index = rating.index(sorted_rating[i])
        temp = canteen[index]
        results.update({temp['Name']:(temp['Rating'], temp['Location'])})
        rating.pop(index)
        canteen.pop(index)
    return results

def display_sortedrank(screen,coordinates,price,food):
    #food_result = {'McDonalds': (4.9, (305, 279))}
    food_result = sort_by_rank(canteenlist)
    screen.fill((211,211,211))
    image = pygame.image.load('display_distance.png')
    screen.blit(pygame.transform.scale(image, (1400, 800)), (0, 0))
    insert_text(screen,'Canteens sorted by Rank','arial',60,(0,0,0),400,10)
    insert_text(screen,'Name','arial',40,(0,0,0),300,80)
    insert_text(screen,'Rating','arial',40,(0,0,0),600,80)
    insert_text(screen,'Location coordinates','arial',40,(0,0,0),900,80)
    height = 130
    for key in food_result:
        insert_text(screen,key,'arial',40,(0,0,0),300,height)
        insert_text(screen,str(food_result[key][0]),'arial',40,(0,0,0),620,height)
        insert_text(screen,str(food_result[key][1]),'arial',40,(0,0,0),950,height)
        height = height + 60
    return back_exit_clicked(screen)



#Sort by Distance
def distance_a_b(location_a, location_b): #Define function to calculate distance between 2 points
    #Change the type of variable into array
    location_a = numpy.array(location_a)
    location_b = numpy.array(location_b)

    delta = (location_a - location_b)
    #Calculate the distance
    distance = numpy.math.sqrt(numpy.dot(delta,delta))
    return distance

def sort_distance(user_location, canteenlist): #Define function to  sort distance from closest to farthest
    canteen = [i for i in canteenlist]
    #Creating a list of distance from user_location
    distance = [distance_a_b(user_location, i['Location']) for i in canteen]
    sorted_distance = [i for i in distance]

    #Perform bubble sort algorithm on the values
    sorted_distance = bubble_sort(sorted_distance)
    
    results = {}
    
    #sort the canteens name from the closest to the furthest from user location
    for i in range(len(distance)):
        index = distance.index(sorted_distance[i])
        temp = canteen[index]
        results.update({temp['Name']:(temp['Rating'], temp['Location'], distance[index])})
        distance.pop(index)
        canteen.pop(index)
        
    return results

def display_sordteddistance(screen,coordinates,price,food):
    #food_result = {'McDonalds': (4.9, (305, 279), 153.83757668398187}
    food_result = sort_distance(coordinates, canteenlist)
    image = pygame.image.load('display_distance.png')
    screen.blit(pygame.transform.scale(image, (1400, 800)), (0, 0))
    insert_text(screen,'Canteens sorted by Distance','arial',60,(0,0,0),400,10)
    insert_text(screen,'Name','arial',40,(0,0,0),220,80)
    insert_text(screen,'Rating','arial',40,(0,0,0),480,80)
    insert_text(screen,'Location','arial',40,(0,0,0),680,80)
    insert_text(screen,'Distance from user','arial',40,(0,0,0),880,80)
    height = 130
    for key in food_result:
        insert_text(screen,key,'arial',40,(0,0,0),220,height)
        insert_text(screen,str(food_result[key][0]),'arial',40,(0,0,0),500,height)
        insert_text(screen,str(food_result[key][1]),'arial',40,(0,0,0),670,height)
        insert_text(screen,'{:.2f} metres'.format(food_result[key][2]*3),'arial',40,(0,0,0),900,height)
        height = height + 60
    return back_exit_clicked(screen)  


#Search by Price
def search_by_price(priceRange, inputList):
    #output = {'KFC': [4.6, (319, 253), ('halal', 'Signature Grilled Chicken', 5.2), ('halal', 'Zinger Burger', 5.3)]
    try:
        result_Dict = {}
        for eachCanteen in inputList:
            canteenFood = eachCanteen['Food']
            canteenLocation = eachCanteen['Location']
            result_list = []
            count = 0
            for key0, key1 in canteenFood:
                if float(priceRange.split('-')[0]) <= canteenFood[key0,key1] <= float(priceRange.split('-')[1]):
                    canteenRating = eachCanteen['Rating']
                    canteenLocation = eachCanteen['Location']
                    if not canteenRating in result_list:
                        result_list.append(canteenRating)
                    if not canteenLocation in result_list:
                        result_list.append(canteenLocation)
                    result_list.append((key0,key1,canteenFood[key0,key1]))
                    count +=1
            if count>0:
                canteenName = eachCanteen['Name']
                result_Dict[canteenName] = result_list
        
        #Sort the key from lowest price to highest price
        for i in result_Dict:
            vec = result_Dict[i][2:]
            sorted_vec = []
            vec_price = [j[2] for j in vec]
            sorted_vec_price = [j for j in vec_price]
            sorted_vec_price = bubble_sort(sorted_vec_price)
          
            for j in range(len(vec)):
                index = vec_price.index(sorted_vec_price[j])
                sorted_vec.append(vec[index])
                vec_price.pop(index)
                vec.pop(index)
            result_Dict[i] = [result_Dict[i][0],result_Dict[i][1]]+sorted_vec

        return result_Dict
    except:
        print('Invalid Input')
        
def display_sortedprice(screen,coordinates,price,food):
    #food_result = {'KFC': [4.6, (319, 253), ('halal', 'Signature Grilled Chicken', 5.2), ('halal', 'Zinger Burger', 5.3)]
    food_result = search_by_price(price, canteenlist)
    image = pygame.image.load('display_distance.png')
    screen.blit(pygame.transform.scale(image, (1400, 800)), (0, 0))
    if len(food_result) == 0:
        insert_text(screen,'No food in the the price range: ${} - ${}'.format(price.split('-')[0],price.split('-')[1]),'arial',60,(0,0,0),200,400)
    else:
        insert_text(screen,'Food sorted by Price: ${} - ${}'.format(price.split('-')[0],price.split('-')[1]),'arial',60,(0,0,0),380,10)
        insert_text(screen,'Name','arial',30,(0,0,0),30,100)
        insert_text(screen,'Rating','arial',30,(0,0,0),150,100)
        insert_text(screen,'Location','arial',30,(0,0,0),300,100)
        insert_text(screen,'Food','arial',30,(0,0,0),470,100)
        height = 150
        for key in food_result:
            food_x_first = 470
            food_x_second = 470
            food_count = 0
            insert_text(screen,key,'arial',20,(0,0,0),30,height)
            insert_text(screen,str(food_result[key][0]),'arial',20,(0,0,0),160,height)
            insert_text(screen,str(food_result[key][1]),'arial',20,(0,0,0),300,height)
            for i in range(len(food_result[key][2:])):
                food_text = ('{} ({}) : ${}'.format(food_result[key][i+2][1],food_result[key][i+2][0],food_result[key][i+2][2]))
                if food_count<=3:
                    position = insert_text(screen,food_text,'arial',15,(0,0,0),food_x_first,height)
                    food_x_first = food_x_first + position[2] + 20
                    food_count += 1
                else:
                    position = insert_text(screen,food_text,'arial',15,(0,0,0),food_x_second,height+25)
                    food_x_second = food_x_second + position[2] + 20
            height = height + 60
    return back_exit_clicked(screen)



#Search by food
def search_by_food(foodName, inputList):
    #output = {'KFC': [4.6, (319, 253), ('halal', 'Zinger Burger', 5.3)}
    foodName = foodName.lower()
    try:
        result_Dict = {}
        for eachCanteen in inputList:
         canteenFood = eachCanteen['Food']
         result_list = []
         count = 0
         for key0, key1 in canteenFood:
           if foodName in key1.lower():
             canteenRating = eachCanteen['Rating']
             canteenLocation = eachCanteen['Location']
             if not canteenRating in result_list:
               result_list.append(canteenRating)
               result_list.append(canteenLocation)
             result_list.append((key0,key1,canteenFood[key0,key1]))
             count +=1
         if count>0:
           canteenName = eachCanteen['Name']
           result_Dict[canteenName] = result_list
        return result_Dict
    except:
        print('Invalid Input')
        
def display_searchfood(screen,coordinates,price,food):
    food_result = search_by_food(food,canteenlist)     #sample result = {'KFC': [4.6, (319, 253), ('halal', 'Zinger Burger', 5.3)}
    image = pygame.image.load('display_distance.png')
    screen.blit(pygame.transform.scale(image, (1400, 800)), (0, 0))
    if len(food_result) == 0:
        insert_text(screen,'No results found for: {}'.format(food),'arial',60,(0,0,0),400,400)
    else:
        insert_text(screen,'Name','arial',40,(0,0,0),30,100)
        insert_text(screen,'Rating','arial',40,(0,0,0),150,100)
        insert_text(screen,'Location','arial',40,(0,0,0),300,100)
        insert_text(screen,'Food','arial',40,(0,0,0),470,100)
        insert_text(screen,'Showing results for: {}'.format(food),'arial',60,(0,0,0),400,10)
        height = 180
        for key in food_result:
            food_x_first = 470
            food_x_second = 470
            food_count = 0
            insert_text(screen,key,'arial',20,(0,0,0),30,height)
            insert_text(screen,str(food_result[key][0]),'arial',20,(0,0,0),170,height)
            insert_text(screen,str(food_result[key][1]),'arial',20,(0,0,0),300,height)
            for i in range(len(food_result[key][2:])):
                food_text = ('{} ({}) : ${}'.format(food_result[key][i+2][1],food_result[key][i+2][0],food_result[key][i+2][2]))
                if food_count<=4:
                    position = insert_text(screen,food_text,'arial',15,(0,0,0),food_x_first,height)
                    food_x_first = food_x_first + position[2] + 20
                else:
                    position = insert_text(screen,food_text,'arial',15,(0,0,0),food_x_second,height+30)
                    food_x_second = food_x_second + position[2] + 20
                food_count += 1
            height = height + 50
    return back_exit_clicked(screen)





#Getting There
def display_gettingthere(screen,coordinates,canteen_name):
    image = pygame.image.load('display_distance.png')
    screen.blit(pygame.transform.scale(image, (1400, 800)), (0, 0))
    distance_user, stop_user, bus_type, stop_canteen, n, distance_canteen, canteenname,canteenlocation = (transport(coordinates,canteen_name))
    if n==0:
        instruction = 'Walk {:.2f} m to {}. There is no need to take bus'.format(3*distance_a_b(coordinates, canteenlocation),canteen_name['Name'])
        insert_text(screen,instruction,'arial',40,(0,0,0),300,400)
    else:
        insert_text(screen,'Directions to {}'.format(canteen_name['Name']),'centuryschoolbook',60,(0,0,0),300,50)
        insert_text(screen,'1) Walk {:.0f} m to bus stop: {}'.format(distance_user, stop_user),'arial',40,(0,0,0),300,200)
        insert_text(screen,'2) Take the {} bus'.format(bus_type),'arial',40,(0,0,0),300,300)
        insert_text(screen,'3) Alight after {} stops at: {}'.format(n,stop_canteen),'arial',40,(0,0,0),300,400)
        insert_text(screen,'4) Walk {:.0f} m to {}'.format(distance_canteen, canteenname),'arial',40,(0,0,0),300,500)
    return back_exit_clicked(screen)
    
def display_transport(screen,coordinates):
    image = pygame.image.load('display_distance.png')
    screen.blit(pygame.transform.scale(image, (1400, 800)), (0, 0))
    image_button1 = pygame.image.load('button.png')
    insert_text(screen,'Where would you like to go','centuryschoolbook',50,(0,0,0),323,70)
    kfc_button = button((255,165,0),300,200,300,40,'',image_button1).draw(screen,(0,0,255),40)
    insert_text(screen,'KFC','arial',40,(0,0,0),420,198)
    mac_button = button((255,165,0),300,300,300,40,'',image_button1).draw(screen,(0,0,255),40)
    insert_text(screen,'McDonalds','arial',40,(0,0,0),370,298)
    koufu_button = button((255,165,0),300,400,300,40,'',image_button1).draw(screen,(0,0,255),40)
    insert_text(screen,'Koufu','arial',40,(0,0,0),410,398)
    canteen1_button = button((255,165,0),300,500,300,40,'',image_button1).draw(screen,(0,0,255),40)
    insert_text(screen,'Food Court 1','arial',40,(0,0,0),360,498)
    canteen2_button = button((255,165,0),300,600,300,40,'',image_button1).draw(screen,(0,0,255),40)
    insert_text(screen,'Food Court 2','arial',40,(0,0,0),360,598)
    canteen9_button = button((255,165,0),700,200,300,40,'',image_button1).draw(screen,(0,0,255),40)
    insert_text(screen,'Food Court 9','arial',40,(0,0,0),760,198)
    canteen11_button = button((255,165,0),700,300,300,40,'',image_button1).draw(screen,(0,0,255),40)
    insert_text(screen,'Food Court 11','arial',40,(0,0,0),750,298)
    canteen13_button = button((255,165,0),700,400,300,40,'',image_button1).draw(screen,(0,0,255),40)
    insert_text(screen,'Food Court 13','arial',40,(0,0,0),750,398)
    canteen16_button = button((255,165,0),700,500,300,40,'',image_button1).draw(screen,(0,0,255),40)
    insert_text(screen,'Food Court 16','arial',40,(0,0,0),750,498)
    quad_button = button((255,165,0),700,600,300,40,'',image_button1).draw(screen,(0,0,255),40)
    insert_text(screen,'Quad Cafe','arial',40,(0,0,0),760,598)
    random_button = button((211,211,211),1000,600,0,0,'',image_button1).draw(screen,(0,0,255),40)
    pygame.display.update()
    while True:
        mousepos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False
                pygame.quit()  
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if kfc_button.isClicked(mousepos):
                    return display_gettingthere(screen,coordinates,kfc)
                if mac_button.isClicked(mousepos):
                    return display_gettingthere(screen,coordinates,mac)
                if koufu_button.isClicked(mousepos):
                    return display_gettingthere(screen,coordinates,koufu)
                if canteen1_button.isClicked(mousepos):
                    return display_gettingthere(screen,coordinates,canteen1)
                if canteen2_button.isClicked(mousepos):
                    return display_gettingthere(screen,coordinates,canteen2)
                if canteen9_button.isClicked(mousepos):
                    return display_gettingthere(screen,coordinates,canteen9)
                if canteen11_button.isClicked(mousepos):
                    return display_gettingthere(screen,coordinates,canteen11)
                if canteen13_button.isClicked(mousepos):
                    return display_gettingthere(screen,coordinates,canteen13)
                if canteen16_button.isClicked(mousepos):
                    return display_gettingthere(screen,coordinates,canteen16)
                if quad_button.isClicked(mousepos):
                    return display_gettingthere(screen,coordinates,quad)
                
def closest_bus_stop(bus_stop_list, location):
    user_distance = [distance_a_b(location, i[1]) for i in bus_stop_list]
    temp = [distance_a_b(location, i[1]) for i in bus_stop_list]
    temp = bubble_sort(temp)
    distance = 3*temp[0]
    stop = bus_stop_list[user_distance.index(temp[0])][0]
    return distance, stop

def number_of_stop(bus_stop_list,canteenlocation, user_stop):
    name_vec = [i[0] for i in bus_stop_list]
    distance, canteen_stop = closest_bus_stop(bus_stop_list, canteenlocation)
    if name_vec.index(canteen_stop) >= name_vec.index(user_stop):
        n = name_vec.index(canteen_stop) - name_vec.index(user_stop)
    else:
        n = len(name_vec) + name_vec.index(canteen_stop) - name_vec.index(user_stop)
    return distance, canteen_stop, n 
    
def transport(userlocation, canteen):
    canteenlocation = canteen['Location']
    canteenname = canteen['Name']
    distance_blue_user, blue_stop_user = closest_bus_stop(blue, userlocation)
    distance_red_user, red_stop_user = closest_bus_stop(red, userlocation)
    distance_blue_canteen, blue_stop_canteen, n_blue = number_of_stop(blue,canteenlocation, blue_stop_user)
    distance_red_canteen, red_stop_canteen, n_red = number_of_stop(red,canteenlocation, red_stop_user)
    if n_blue > n_red:
        n, distance_user, distance_canteen, bus_type, stop_user, stop_canteen = n_red, distance_red_user, distance_red_canteen, 'red', red_stop_user, red_stop_canteen
    elif n_red > n_blue:
        n, distance_user, distance_canteen, bus_type, stop_user, stop_canteen = n_blue, distance_blue_user, distance_blue_canteen, 'blue', blue_stop_user, blue_stop_canteen
    else:
        if distance_blue_user > distance_red_user:
            n, distance_user, distance_canteen, bus_type, stop_user, stop_canteen = n_red, distance_red_user, distance_red_canteen, 'red', red_stop_user, red_stop_canteen
        else:
            n, distance_user, distance_canteen, bus_type, stop_user, stop_canteen = n_blue, distance_blue_user, distance_blue_canteen, 'blue', blue_stop_user, blue_stop_canteen
    return distance_user, stop_user, bus_type, stop_canteen, n, distance_canteen, canteenname,canteenlocation


#initialise
text_canteens,text_coordinates,text_price,text_distance,text_rank,text_food,text_submit_food,text_submit_price,text_exit,text_updateinfo,text_transport,menu_screen = display_menu(None,None,None)
price = None
food = None
coordinates = None
run = True
while run:
    pygame.display.update()
    mousepos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False
            pygame.quit()  
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if text_canteens.isClicked(mousepos):
                if display_all_canteens(menu_screen,coordinates,price,food) == False:
                    pygame.quit()
                    run = False

            elif text_exit.isClicked(mousepos):
                pygame.quit()
                run = False
            
            elif text_coordinates.isClicked(mousepos):
                pygame.quit()
                coordinates = get_user_location()
                time.sleep(2)
                pygame.quit()
                text_canteens,text_coordinates,text_price,text_distance,text_rank,text_food,text_submit_food,text_submit_price,text_exit,text_updateinfo,text_transport,menu_screen = display_menu(coordinates,price,food)
                
            elif text_price.isClicked(mousepos):
                price = user_input().initialise("Enter price range (eg 1-5): ")
                display_menu(coordinates,price,food)
                
            elif text_submit_price.isClicked(mousepos):
                if price!=None:
                    if display_sortedprice(menu_screen,coordinates,price,food) == False:
                        pygame.quit()
                        run = False

                
            elif text_food.isClicked(mousepos):
                food = user_input().initialise("Enter the food you want to search: ")
                display_menu(coordinates,price,food)
                
            elif text_submit_food.isClicked(mousepos):
                if food!=None:
                    if display_searchfood(menu_screen,coordinates,price,food) == False:
                        pygame.quit()
                        run = False

            elif text_distance.isClicked(mousepos):
                if coordinates!= None:
                    if display_sordteddistance(menu_screen,coordinates,price,food) == False:
                        pygame.quit()
                        run = False

            elif text_rank.isClicked(mousepos):
                if display_sortedrank(menu_screen,coordinates,price,food) == False:
                    pygame.quit()
                    run = False

            elif text_updateinfo.isClicked(mousepos):
                if display_updateinfo(menu_screen) == False:
                    pygame.quit()
                    run = False

            elif text_transport.isClicked(mousepos):
                if coordinates!= None:
                    if display_transport(menu_screen,coordinates) == False:
                        pygame.quit()
                        run = False
                    
                


        
