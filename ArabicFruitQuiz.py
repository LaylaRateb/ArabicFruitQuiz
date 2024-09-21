import random
import requests
from PIL import Image
from io import BytesIO
import time
import subprocess
import os

# create a hashmap for the fruit names
fruits = [
    {"Arabic": "مُوز mawz", "English": "banana", "Image": "https://img.freepik.com/premium-vector/illustration-vector-banana-white-background_444663-1380.jpg"},
    {"Arabic": "تُفّاح tu-faa7", "English": "Apple", "Image": "https://media.istockphoto.com/id/506670795/vector/red-apple.jpg?s=612x612&w=0&k=20&c=lF9vQ-kQPv3StsSFND4Okt1yqEO86q2XWFECgn0AqWU="},
    {"Arabic": " مِشْمِشْ mish-mish", "English": "Apricot", "Image": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.123rf.com%2Fclipart-vector%2Fapricot.html&psig=AOvVaw2nSwpe6Ki4GZEpzzReknys&ust=1714944394080000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCNit1u739IUDFQAAAAAdAAAAABAE"},
    {"Arabic": "تُوْت أَرْضِيّ toot ardee", "English": "Blueberry", "Image": "https://media.istockphoto.com/id/1334495562/vector/blueberry-with-leaves-isolated-eps10-vector-illustration.jpg?s=612x612&w=0&k=20&c=c79TRjZOCyHWCe9nQu2eWo00E3iRaC_hkdf1jOJbJDw="},
    {"Arabic": "Sham-maam or baTeekh as-far بِطِّيخ أَصْفَر", "English": "Cantaloupe", "Image": "https://www.kroger.com/product/images/large/front/0082757530000"},
    {"Arabic": "karaz كَرَز", "English": "cherry", "Image": "https://static.vecteezy.com/system/resources/previews/008/085/926/non_2x/cherry-clip-art-illustration-vector.jpg"},
    {"Arabic":  "ِJaw-zil-hind  جَوْز الهِنْدِ", "English": "coconut", "Image": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fillustrations%2Fcoconut-clipart&psig=AOvVaw24y9aqQkiRdfZiXrHd5sD0&ust=1714944896657000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOCcyOX59IUDFQAAAAAdAAAAABAE"},
    {"Arabic": "As-bar-ree آس بَرّيّ or toot-baree توت بري", "English": "cranberry", "Image":"https://media.istockphoto.com/id/1386612486/vector/lingonberries-cranberry-isolated-red-berry-fruits.jpg?s=612x612&w=0&k=20&c=lSdunFwDtItQsxIXzjl8E8BJCCcT7a5CZU0HLrQ7SCI= "},
    {"Arabic": "Tamr تَمْر or Tam-ra تَمْرَة", "English": "Date", "Image": "https://m.media-amazon.com/images/I/41SN0XTgbZL.jpg" },
    {"Arabic": "3enib عِنِب ", "English": "Grape", "Image": "https://media.istockphoto.com/id/1166277203/vector/green-bunch-of-grapes-green-grapes-cluster.jpg?s=612x612&w=0&k=20&c=0R4sZh2M4qvoCFYcBP9ldJSAqAgBpoDH-mODAB0szBk="},
    {"Arabic": "teen تِيْن ", "English": "Fig", "Image": "https://orionmagazine.org/wp-content/uploads/2021/10/figunsplash.jpg"},
    {"Arabic": "kee-wee كيوي", "English": "kiwi", "Image": "https://media.istockphoto.com/id/1396407149/vector/whole-kiwi-with-green-leaf-isolated-on-white-background-flat-vector-illustration.jpg?s=612x612&w=0&k=20&c=y0mfVfhh54lS3woUgJDJRpNJIAVYQ4b7duU7pQ0HGeM="},
    {"Arabic": "li-moon لِيمون ", "English": "Lemon", "Image": "https://thumbs.dreamstime.com/b/lemon-9953795.jpg"},
    {"Arabic": "laaym لايم", "English": "Lime", "Image": "https://img.freepik.com/premium-vector/lime-fruit-icon-vector-design_387989-332.jpg"},
    {"Arabic": "maan-jo  مانْجو ", "English": "Mango", "Image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJQC5q87wNKmou1SO03UBlR1IoSl7oUr5Vt4GbliWgsg&s"},
    {"Arabic": "Toot تُوْت ", "English": "Mulberry", "Image": "https://cdn11.bigcommerce.com/s-2drwt2az/images/stencil/original/products/19432/57417/apitjbe3g__07746.1592325376.jpg?c=2"},
    {"Arabic": "burtoqaal بُرْتُقال ", "English": "Orange", "Image": "https://pics.clipartpng.com/midle/Oranges_PNG_Clip_Art-1719.png"},
    {"Arabic": "Do-raaq دُرّاق", "English": "Peach", "Image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6Z8HBfy_RtXQSrCZS3U55QevOKmUuJWD3m1aQSLrMbQ&s"},  # fix
    {"Arabic": "anaa-naaas أناناس ", "English": "Pineapple", "Image": "https://img.freepik.com/premium-vector/yellow-pineapple-vector-element-illustration_444663-3536.jpg"},
    {"Arabic": "bar-qooq بَرْقُوْق ", "English": "Plum", "Image": "https://farmfreshfundraising.com/wp-content/uploads/2017/10/plums.jpg"},
    {"Arabic": " Toot ahmar توت الأحمر or توت العُلَّيْق toot-til-ol-laykِ", "English": "Raspberry", "Image": "https://us.123rf.com/450wm/eugenebsov/eugenebsov2104/eugenebsov210400161/167256629-raspberry-sweet-fruit-illustration-for-web-isolated-on-white-background-creative-design.jpg?ver=6"},  # fix
    {"Arabic": "rum-maan رُمّان", "English": "Pomegranate", "Image": "https://media.istockphoto.com/id/1057225114/vector/pomegranate-whole-and-a-piece-with-leaves-on-white-vector-illustration-no-gradients.jpg?s=612x612&w=0&k=20&c=Xinh22Ee7CZarKpWSRSacYRlaYOo0k_1UFxrasRqWpU="},
    {"Arabic": "Freez فْريز", "English": "Strawberry", "Image": "https://clv.h-cdn.co/assets/15/22/2560x1728/gallery-1432664914-strawberry-facts1.jpg"},
    {"Arabic": "bana-doora بَنَدورة", "English": "Tomato", "Image": "https://static.vecteezy.com/system/resources/previews/019/862/489/original/tomato-icon-clipart-vegetable-illustration-vector.jpg"},
    {"Arabic": "bit-teekh بِطّيخ", "English": "Watermelon", "Image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdVRGSCLQXZ0g2rRfLpn8cJaW1hJTm293bZg6b_hAx0Q&s"},
    {"Arabic": "Njaas or kom-math-ra  كُمَّثْرى", "English": "Pear", "Image": "https://static.vecteezy.com/system/resources/previews/005/170/812/non_2x/pear-green-with-pear-slices-and-leaves-vitamins-healthy-food-fruit-on-a-white-background-realistic-3d-illustration-vector.jpg"},
    {"Arabic": "bit-teekh بِطّيخ", "English": "Watermelon", "Image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSdVRGSCLQXZ0g2rRfLpn8cJaW1hJTm293bZg6b_hAx0Q&s"},
    {"Arabic": "Faa-ke-hatul a3-te-fa فاكهة العاطفة", "English": "Passion Fruit", "Image": "https://www.desertsun.com/gcdn/-mm-/f23271e0de29a824fcc0e90439b132dedcbb2962/c=0-45-1372-820/local/-/media/2016/08/24/PalmSprings/PalmSprings/636076501977481262-TDS-NBR-0826-Fresh-Pick-dragonfruit-passionfruit.jpg?width=1372&height=775&fit=crop&format=pjpg&auto=webp"},# fix
]

print("Welcome to the Arabic Fruit Quiz!")
print("For each question, type the English translation")

random.shuffle(fruits)
total_questions = len(fruits)
questions_asked = 0
total_score = 0

# Iterate through each fruit in the shuffled list
for fruit in fruits:
    print(fruit['Arabic'].strip())
    user_input = input("Enter fruit: ").lower().strip()

    # Check if user input matches the correct English name, case-insensitive
    if user_input == fruit['English'].strip().lower():
        print("Good Job!")
        total_score += 1
        # Display the image only if the answer is correct
        image_url = fruit["Image"]
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        image.show()

        # Close the image window after 2 seconds
        time.sleep(2)
        # Close image window using AppleScript
        subprocess.run(["osascript", "-e", 'tell application "Preview" to close every window'])

    else:
        print("Wrong!")
        print(f"The correct answer is {fruit['English']}")

    questions_asked += 1

# Display final score
if questions_asked == total_questions:
    print(f"Your Final Score is: {total_score}/{total_questions}")
    print("Thank you for Playing!")




