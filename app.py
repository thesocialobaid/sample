import random
import time 

quotes = [ 
"why do we fall? so we can learn to pick ourselves up. - Batman Begins",
"The night is darkest just before the dawn. - The Dark Knight", 
"It's not who I am underneath, but what I do that defines me. - Batman Begins",
"Some men just want to watch the world burn. - The Dark Knight",
"You either die a hero, or you live long enough to see yourself become the villain. - The Dark Knight",
"Madness, as you know, is like gravity. All it takes is a little push. - The Dark Knight",
"I'm Batman. - Batman",
] 

if __name__ == "__main__": 
    while True: 
        print(random.choice(quotes)) 
        time.sleep(5)