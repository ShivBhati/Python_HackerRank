# Create a list which shows the side of the cuboid but the sum of all three side should not be equal to the Input variable "n".



def cuboid(x,y,z,n):
    list= []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if (i+j+k != n):
                    list.append([i,j,k])
    print(sorted(map(list)))
                    
                


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    a = 0
    