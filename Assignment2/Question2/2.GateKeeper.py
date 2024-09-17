from PIL import Image
import time

current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10
print(generated_number)    


image = Image.open("C:/Users/Acer/Downloads/Assignment 2/chapter1.jpg")
pixels = image.load()


for i in range(image.size[0]):
    for j in range(image.size[1]):
        r, g, b = pixels[i, j]
        newR = min(255, r + generated_number)
        newG = min(255, g + generated_number)
        newB = min(255, b + generated_number)
        pixels[i, j] = (newR, newG,newB)


image.save("rajan.png")

sumOfRed = 0
for i in range(image.size[0]):
    for j in range(image.size[1]):
        r, g, b = pixels[i, j]
        sumOfRed += r

print("Sum of Red number is " + str(sumOfRed))
