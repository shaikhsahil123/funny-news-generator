# import random module import random
import pyttsx3
import random
import time
# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty("rate", 175)   # speed of speech
engine.setProperty("volume", 1.0) # max volume

# Colored text function
def color(text, code):
    return f"\033[{code}m{text}\033[0m"

# List of subjects
subjects = [
    "Akshay Kumar",
    "Ajay Devgan", 
    "Ranveer Singh", 
    "Prabhas",
    "Allu Arjun",
    "Ram Charan", 
    "Rajinikanth", 
    "Kamal Haasan",
    "Yash", 
    "KGF Rocky Bhai", 
    "Narendra Modi", 
    "Amit Shah",
    "Virat Kohli", 
    "Rohit Sharma", 
    "Hardik Pandya", 
    "KL Rahul",
    "Sachin Tendulkar", 
    "Elon Musk", 
    "Bill Gates", 
    "Mark Zuckerberg",
    "Random School Teacher", 
    "Local Fruit Seller", 
    "College Professor",
    "Train Ticket Collector", 
    "Police Constable", 
    "Rickshaw Passenger",
    "Startup Founder", 
    "News Reporter", 
    "YouTuber", 
    "TikTok Star",
    "Random Programmer", 
    "Indian Army Soldier", 
    "Local Worker",
    "Tech Guy", 
    "Neighbour Uncle", 
    "Gym Trainer", 
    "Delivery Boy"
]

# Dictionary of locations for subjects
places_or_things = {
    "Akshay Kumar": "Juhu Beach",
    "Ajay Devgan": "Andheri Sports Complex",
    "Ranveer Singh": "Film City Goregaon",
    "Prabhas": "Hyderabad Studio",
    "Allu Arjun": "Ramoji Film City",
    "Ram Charan": "Hyderabad Film Set",
    "Rajinikanth": "Chennai R.A. Puram",
    "Kamal Haasan": "Alwarpet",
    "Yash": "Bangalore Studio",
    "KGF Rocky Bhai": "KGF Mines",
    "Narendra Modi": "Delhi Parliament Road",
    "Amit Shah": "Gandhinagar Office",
    "Virat Kohli": "Chinnaswamy Stadium",
    "Rohit Sharma": "Marine Drive",
    "Hardik Pandya": "Mumbai Cricket Ground",
    "KL Rahul": "Bengaluru Stadium",
    "Sachin Tendulkar": "Bandra West",
    "Elon Musk": "Tesla Headquarters",
    "Bill Gates": "Microsoft Campus",
    "Mark Zuckerberg": "Meta Office California",
    "Random School Teacher": "City School Building",
    "Local Fruit Seller": "Market Area",
    "College Professor": "University Campus",
    "Train Ticket Collector": "Railway Station",
    "Police Constable": "City Police Station",
    "Rickshaw Passenger": "Main Street",
    "Startup Founder": "Bangalore Tech Park",
    "News Reporter": "News Studio",
    "YouTuber": "YouTube Studio",
    "TikTok Star": "Mumbai Film Set",
    "Random Programmer": "Tech Office",
    "Indian Army Soldier": "Military Base",
    "Local Worker": "Factory Area",
    "Tech Guy": "Silicon Valley",
    "Neighbour Uncle": "Residential Area",
    "Gym Trainer": "Local Gym",
    "Delivery Boy": "Warehouse Center"
}

# List of actions
actions = [
    "shocks everyone with",
    "reveals secret of",
    "announces a new rule about",
    "fights over",
    "runs away with",
    "starts dancing on",
    "gets angry about",
    "starts selling",
    "accidentally breaks",
    "officially supports",
    "launches investigation on",
    "buys 500 kg of",
    "starts trending because of",
    "makes fun of",
    "challenges everyone for",
    "declares holiday for",
    "accidentally leaks",
    "gives lecture on",
    "complains about",
    "celebrates victory with",
    "changes dress code of",
    "tries to fix",
    "starts training for",
    "argues loudly about",
    "goes missing with"
]

# Start the headline generator loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    location = places_or_things.get(subject, "Unknown Location")

    headline = f"LIVE FROM: {location}\nBREAKING NEWS: {subject} {action} at {location}"
    
    # Print colored headline
    print("\n" + color(headline, "1;99"))  # red text
    print("\a")  # beep

    # Voice output
    engine.say(headline)
    engine.runAndWait()

    # Ask user if they want another headline
    user_input = input(color("\nDo you want another headline? (yes/no): ", "1;39")).strip().lower()
    if user_input == "no":
        break

# Goodbye message
goodbye_text = "Thanks for using the Fake News Headline Generator. Have a fun day!"
print(color("\n" + goodbye_text, "1;35"))  # green text
engine.say(goodbye_text)
engine.runAndWait()