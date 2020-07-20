#list

a=[1,2,3,4]
b=1,2,3,4
c=list(b)

print(a)  #[1,2,3,4]
print(c)  #[1,2,3,4]
print(a[0])  #1
print(a[0]+a[2])  #4

print(a+c) #1,2,3,4,1,2,3,4
a[1:2]=["another","level"]
print(a)   #[1, 'another', 'level', 3, 4]

d=[1,2,[3,4,[5,6]]]
print(d[2][1])  #4

cities=['Seoul','Busan','New York','Washinton','Tokyo','Rio','Vancouver']
print(cities[1:5:2]) #['Busan','Washinton'] #slicing

#deleting
del cities[0:2]
print(cities)

print("numbers"+str(a[0:2])) #must convert a into string

num1=[2,0,4,8]
#appending
num1.append(7)
print(num1)

#sorting
s1=sorted(num1)
print(s1)   #[0, 2, 4, 7, 8]  same result as: num1.sort() >> print(num1)
print(num1)   #[2, 0, 4, 8, 7]

#reverse
num1.reverse()

artists=["billy","below","ariana","justin"]
print(artists.index("billy"))

artists.remove("justin")
print(artists)
print(artists.append("taylor"))
print(artist.pop())
print(artists.count())
