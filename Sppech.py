import speech_recognition as sr
import pyttsx3 
import pywhatkit
import wikipedia
import datetime
import time
import os
import openai
import google.generativeai as genai
import pyautogui
from plyer import notification
import requests
from bs4 import BeautifulSoup
import speedtest
from plyer import call
genai.configure(api_key="AIzaSyBaBkE8xHWPN2T5KmpbZ5kls4n4ibWh0HM")

r = sr.Recognizer()
# Function to convert text to speech
def speak(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Function to listen and recognize speech
def listen():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = r.listen(source,timeout=60)
            text = r.recognize_google(audio).lower()
            print("You said:", text)
            return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        speak("Sorry, I couldn't understand that.please repeat")
        return ""
    except sr.RequestError:
        print("Speech recognition service is unavailable.")
        return ""
    except Exception as e:
        print("Error:", str(e))
        return ""

def google_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")  # Correct model name
        if 'write' in prompt.lower():
            prompt=prompt+" "+'in short'
            response = model.generate_content(prompt)
        else:
            response=model.generate_content(prompt, generation_config={"max_output_tokens": 50})
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def type_text(text):
    pyautogui.write(text,interval=0.05)
    pyautogui.press('enter')

# Function to send WhatsApp message
def send_whatsapp():
    speak("tell the person to who u want to send message")
    d={"mummy":9865120930,"daddy":8248953272,"tamilarasan":9384154339}
    name = listen().replace(" ", "")
    phone_number=d.get(name)
    phone_number=f"+91{phone_number}"
    speak("What message would you like to send?")
    message = listen()

    if not message:
        speak("I didn't hear your message. Please try again.")
        return

    speak(f"Scheduling message '{message}' to {phone_number} ")
    
    try:
        #pywhatkit.sendwhatmsg(phone_number, message, hour, minute, wait_time=10)
        pywhatkit.sendwhatmsg_instantly(phone_number, message)
        speak("Message scheduled successfully.")
    except Exception as e:
        speak("There was an error sending the message.")
        print("Error:", e)

def get_ipl_score():
    import requests
    import json

    #api_key = "1b9cfb09-fc37-4072-9b6d-196be1114b87"  # Replace with your actual API key
    url = "https://api.cricapi.com/v1/currentMatches?apikey=1b9cfb09-fc37-4072-9b6d-196be1114b87&offset=0"

    # Fetch data from API
    response = requests.get(url)
    #print(response)
    datas = response.json()
    #print("datas is",datas)
    # Debug: Print full API response (optional)
    # print(json.dumps(data, indent=2))

    if datas.get("status") != "success":
        print("Error fetching IPL scores.")
    else:
        #matches = datas.get("data", [])
        if "data" in datas:
            matches = datas["data"]
            #print("matches is",matches)
        else:
            print("Key 'data' not found in response")
        ipl_matches = [match for match in matches if match.get("matchType") == "t20"]

        print("ipl mathches is",ipl_matches)
        if not ipl_matches:
            print("No live IPL matches found.")
            speak("No live IPL matches found.")
        else:
            match = ipl_matches[0]

            team1, team2 = match["teams"]
            venue = match["venue"]
            status = match["status"]

            print(f"\n🏏 {match['name']}")
            print(f"📍 Venue: {venue}")
            print(f"📢 Status: {status}")

            # Check if scores are available
            if "score" in match and len(match["score"]) >= 2:
                team1_score = match["score"][0].get("r", "N/A")  # Runs
                team1_wickets = match["score"][0].get("w", "N/A")  # Wickets
                team1_overs = match["score"][0].get("o", "N/A")  # Overs

                team2_score = match["score"][1].get("r", "N/A")
                team2_wickets = match["score"][1].get("w", "N/A")
                team2_overs = match["score"][1].get("o", "N/A")
                notification.notify(
                    title="IPL Score",
                    message=f"{team1}:{team1_score}\n {team2}:{team2_score}",
                    timeout=10
                )
                print(f"{team1}: {team1_score}/{team1_wickets} ({team1_overs} overs)")
                speak(f"{team1} score is {team1_score} and wicket taken is{team1_wickets} and completed ({team1_overs} overs)")
                print(f"{team2}: {team2_score}/{team2_wickets} ({team2_overs} overs)")
                speak(f"{team2} score is{team2_score} and wicket taken is {team2_wickets} and completed ({team2_overs} overs)")
                
            else:
                print("🔴 Score not available yet.")
                speak("Score not available yet.")


def make_call(number):
    call.makecall(tel=number)

# def get_news():
    """Fetches news articles based on user input category."""
    api_key = "d5a01ee91308496398321b1da94c9767"
    base_url = "https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey=" + api_key
    
    categories = ["business", "entertainment", "health", "science", "sports", "technology"]
    
    speak("Which category do you want news from? Business, Entertainment, Health, Science, Sports, or Technology?")
    category = input("Enter news category: ").strip().lower()
    
    if category not in categories:
        speak("Invalid category. Please choose from the given options.")
        return
    
    url = base_url.format(category)
    print(f"Fetching {category} news...")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        news_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        speak("There was an error retrieving the news.")
        return
    
    if news_data.get("status") != "ok":
        speak("Sorry, I couldn't fetch the news.")
        return
    
    articles = news_data.get("articles", [])
    
    if not articles:
        speak("No news articles found.")
        return
    
    speak("Here are the top news headlines.")
    for i, article in enumerate(articles[:5]):  # Limit to 5 articles
        title = article.get("title", "No title available")
        news_url = article.get("url", "No URL available")
        
        print(f"{i+1}. {title}")
        speak(title)
        print(f"Read more: {news_url}\n")
        speak("Press 1 to continue, 2 to stop: ")
        user_input = input("Press 1 to continue, 2 to stop: ").strip()
        if user_input == "2":
            break
    
    speak("That's all for now!")

# Function to process commands after activation
def commands():
    try:
        while True:
            text = listen()

            if 'jarvis' in text:
                speak("What help do you need?")
                
                while True:
                    my_text = listen()
                    
                    if not my_text:  # Skip if empty
                        continue

                    if "stop" in my_text or "exit" in my_text or "quit" in my_text:
                        speak("Okay, exiting the program. Goodbye sir!")
                        exit()

                    elif 'play' in my_text:
                        song = my_text.replace('play', '').strip()
                        speak(f'Playing {song}')
                        pywhatkit.playonyt(song)

                    elif 'date' in my_text:
                        today = datetime.date.today().strftime("%Y-%m-%d")
                        speak(f"Today's date is {today}")

                    elif 'time' in my_text:
                        timenow = datetime.datetime.now().strftime('%H:%M')
                        speak(f"The time is {timenow}")

                    elif 'who is' in my_text:
                        try:
                            person = my_text.replace('who is', '').strip()
                            info = wikipedia.summary(person, sentences=1)
                            speak(info)
                        except wikipedia.exceptions.DisambiguationError:
                            speak(f"Multiple results found for {person}. Please be more specific.")
                        except wikipedia.exceptions.PageError:
                            speak(f"Sorry, I couldn't find any information on {person}.")
                        except Exception:
                            speak("An error occurred while searching Wikipedia.")

                    

                    elif 'whatsapp' in my_text:
                        send_whatsapp()
                    elif 'open' in my_text:
                        import os
                        apps = {
                                "chrome": "start chrome",
                                "notepad": "notepad",
                                "calculator": "calc",
                                "command prompt": "cmd",
                                "word": "start winword",
                                "excel": "start excel",
                                "powerpoint": "start powerpnt",
                            }
                        app = my_text.replace('open', '').strip().lower()
                        speak('opening app'+app)
                        os.system(apps[app])
                        if app=="notepad" or "word":
                            speak("what you want to write")
                            new_text=listen()
                            pro=google_gemini(new_text)
                            type_text(pro)
                    elif 'what' in my_text:
                        my_text=my_text.replace('google','')
                        pywhatkit.search(my_text)  # Opens Google search
                        speak(f"Here is what I found for {my_text} on the web.")
                        
                    elif "screenshot" in my_text:
                        import time
                        speak("taking screen shot sir")
                        screenshot = pyautogui.screenshot()
                        filename = f"C:\\Users\\sanja\\OneDrive\\Pictures\\Screenshots\\screenshot_{int(time.time())}.png"
                        screenshot.save(filename)
                    elif "ipl" in my_text:
                        print(f"Recognized text: {my_text}")
                        speak("fetching sir")
                        get_ipl_score()
                    elif 'click my photo' in my_text:
                        import time 
                        pyautogui.press("win")  
                        time.sleep(1)  
                        pyautogui.typewrite("Camera") 
                        time.sleep(1)
                        pyautogui.press("enter") 
                        time.sleep(3)  
                        speak("smile please")
                        pyautogui.press("enter")  
                        time.sleep(1)
                        pyautogui.click(x=700, y=500)  
                        speak("photo taken sir")

                    elif "gemini" in my_text:
                        speak("Say what you want")
                        message = listen()

                        if message:
                            response = google_gemini(message)
                            speak(response)
                        else:
                            speak("I didn't hear anything.")
                    elif 'internet speed' in my_text:
                        wifi = speedtest.Speedtest()
                        wifi.get_best_server()  # Selects the best nearby server
                        speak("please wait sir")
                        speak("Testing Download Speed...")
                        print("Testing Download Speed...")
                        download_net = wifi.download() / 1048576  # Convert to Mbps
                        time.sleep(1)
                        speak("Testing Upload Speed...")
                        print("Testing Upload Speed...")
                        upload_net = wifi.upload() / 1048576  # Convert to Mbps
                        print(f"Upload Speed: {upload_net:.2f} Mbps")
                        speak(f"your Upload Speed is: {upload_net:.2f} Mbps")
                        print(f"Download Speed: {download_net:.2f} Mbps")
                        speak(f"your Download Speed is: {download_net:.2f} Mbps")
                    elif "game" in my_text:
                        import random
                        speak("lets play rock paper scissors")
                        i=0
                        me=0
                        comp=0
                        while(i<5):
                            i+=1
                            choose=["rock","paper","scissor"]
                            comp_choose=random.choice(choose)
                            my_choose=listen().lower()
                            if (my_choose=="rock"):
                                if (comp_choose=="rock"):
                                    speak("Rock")
                                    print(f"score myscore:{me} compscore:{comp}")
                                    speak(f"your score is {me}")
                                    speak(f"my score is {comp}")
                                elif (comp_choose=="paper"):
                                    speak("paper")
                                    comp+=1
                                    print(f"score myscore:{me} compscore:{comp}")
                                    speak(f"your score is {me}")
                                    speak(f"my score is {comp}")
                                elif (comp_choose=="scissor"):
                                    speak("scissor")
                                    me+=1
                                    print(f"score myscore:{me} compscore:{comp}")
                                    speak(f"your score is {me}")
                                    speak(f"my score is {comp}")
                            elif (my_choose=="paper"):
                                if (comp_choose=="rock"):
                                    speak("Rock")
                                    me+=1
                                    print(f"score myscore:{me} compscore:{comp}")
                                    speak(f"your score is {me}")
                                    speak(f"my score is {comp}")
                                elif (comp_choose=="paper"):
                                    speak("paper")
                                    print(f"score myscore:{me} compscore:{comp}")
                                    speak(f"your score is {me}")
                                    speak(f"my score is {comp}")
                                elif (comp_choose=="scissor"):
                                    speak("scissor")
                                    comp+=1
                                    print(f"score myscore:{me} compscore:{comp}")
                                    speak(f"your score is {me}")
                                    speak(f"my score is {comp}")
                            elif (my_choose=="scissor"):
                                if (comp_choose=="rock"):
                                    speak("Rock")
                                    comp+=1
                                    print(f"score myscore:{me} compscore:{comp}")
                                    speak(f"your score is {me}")
                                    speak(f"my score is {comp}")
                                elif (comp_choose=="paper"):
                                    speak("paper")
                                    me+=1
                                    print(f"score myscore:{me} compscore:{comp}")
                                    speak(f"your score is {me}")
                                    speak(f"my score is {comp}")
                                elif (comp_choose=="scissor"):
                                    speak("scissor")
                                    print(f"score myscore:{me} compscore:{comp}")
                                    speak(f"your score is {me}")
                                    speak(f"my score is {comp}")
                        if comp>me:
                            speak("i am the winner")
                        elif comp==me:
                            speak("match is draw")
                        else:
                            speak("you are the winner")
                
                    # elif "news" or "info" in my_text:
                    #     import json
                    #     import requests
                    #     get_news()
                    elif "phone call" in my_text:
                        no="9865120930"
                        make_call(no)
                    elif "shutdown" in my_text:
                        import os
                        import time

                        delay = 30  # Delay in seconds before shutdown
                        print(f"System will shut down in {delay} seconds...")
                        time.sleep(delay)
                        os.system(f"shutdown /s /t 0")




                              
                        

    except KeyboardInterrupt:
        speak("Goodbye!")
    except Exception as e:
        print("Error:", str(e))

# Start the assistant
speak("Welcome to Jarvis. Say 'Jarvis' to activate sir.")
commands()
