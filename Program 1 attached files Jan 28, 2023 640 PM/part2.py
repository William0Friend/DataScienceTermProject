
# your code below
import os
import glob

#go to program's directory
#change to flowers directory
# 3 lines to check check you are in the right directory
print("Checking te directory...")
print(os.getcwd())
print(os.listdir())
# cd into the flowers directory
flowers = os.chdir('flowers/flowers')
# check that the 5 flower subdirectories are present
print(os.getcwd())
#declare up here for scope
flower_types  = []
subdirs = []
#get every subdirectory in flowers/flowers
# loop through each subdirectory
for folder in glob.glob('*'):
    subdirs.append(folder)
    print("Folder: {}".format(folder))
    # innitialize i
    i = 1
    # copy sudirectories to another list with beter name
    flower_types.append(folder)  
    os.chdir(folder)
    # loop through each img in the subdirectory
    for image in glob.glob('*.png'):
        #print("Image:{}".format(image))
        #still needs leading zeros 
        num_digits = 7
        #result = "{:0{}d}".format(count, num_digits)
        #print(result)
        #print("Before Rename:{}".format(image))
        #newImage = os.rename(image, f"{folder}_{i}.png")
        #print("After:{}".format(newImage))
        newImage2 = os.rename(image, '{}_{:06d}.png'.format(folder, i))
        print("Was changed:{}".format(newImage2))
        #os.rename(image, f"{flower_types}_{i}.png")
        #result = "{}_{:0{}d}".format(flower_types,i, num_digits)
        # increment by 1
        i += 1
    #go back into flowers directory
    os.chdir('..')
print(subdirs)      



from math import sqrt
def dist(point):
    x, y = point
    return sqrt(x**2 + y**2)
def kClosest(points, k):
    points.sort(key=dist)
    return points[:k]

def question_ten_alt(points, k):
    from heapq import heapify,heappop
    from math import sqrt
    closest = []
    distances = []
    x1,x2,y1,y2,euclidean_distance = 0,0,0,0,0
    origin = [[0,0]] 
    for i in points:
        x1 = i[0]
        y1 = i[1]
        x2 = origin[0][0]
        y2 = origin[0][1]
        euclidean_distance = sqrt((x1-x2)**2 + (y1-y2)**2)
        distances.append([euclidean_distance,i])
        heapify(distances)
    for i in range(k):
        closest.append(heappop(distances)[1])
    return print(closest)





#classes = ['chamomile', 'tulip', 'rose', 'sunflower', 'daisy']


#for cls in classes:
#   path = os.path.join('./data/', cls)
#    i = 1
#    for filename in glob.glob(os.path.join(path, '*.jpg')):
#        os.rename(filename, os.path.join(path, '{}_{:06d}.jpg'.format(cls, i)))
#        i += 1