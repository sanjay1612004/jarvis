import cv2
import face_recognition
import pyttsx3
def speak(command):
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()
def face_rec():
    known_face_encodings = []
    known_face_names = []

    known_person1_image = face_recognition.load_image_file("images/adani.jpg")
    known_person1_face_encoding = face_recognition.face_encodings(known_person1_image)[0]
    known_face_encodings.append(known_person1_face_encoding)

    known_face_names.append("Adani")

    known_person2_image = face_recognition.load_image_file("images/ambani.jpeg")
    known_person2_face_encoding = face_recognition.face_encodings(known_person2_image)[0]
    known_face_encodings.append(known_person2_face_encoding)
    known_face_names.append("Ambani")

    known_person3_image = face_recognition.load_image_file("images/mahindera.jpg")
    known_person3_face_encoding = face_recognition.face_encodings(known_person3_image)[0]
    known_face_encodings.append(known_person3_face_encoding)
    known_face_names.append("Mahindera")

    known_person4_image = face_recognition.load_image_file("images/ratantata.png")
    known_person4_face_encoding = face_recognition.face_encodings(known_person4_image)[0]
    known_face_encodings.append(known_person4_face_encoding)
    known_face_names.append("Ratan Tata")

    video_capture = cv2.VideoCapture(0)

    while True:
        ret,frame = video_capture.read()

        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame,face_locations)

        for (top,right,bottom,left),face_encoding in zip(face_locations,face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings,face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                if name=="Ambani":
                    speak(f" this is {name} and he is the owner of reliance")
                elif name=="Adani":
                    speak(f" this is {name} and he is the owner of adani group")
                elif name=="Mahindera":
                    speak(f" this is {name} and he is the owner of mahindera group")
                elif name=="Ratan Tata":
                    speak(f" this is {name} and he is the owner of tata group")

            cv2.rectangle(frame,(left,top),(right,bottom),(0,255,0),2)
            cv2.putText(frame,name,(left,top-10),cv2.FONT_HERSHEY_SIMPLEX,0.75,(0,255,0),2)

        cv2.imshow("Video",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    face_rec()