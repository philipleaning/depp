#face_recognition tutorial

import face_recognition
#image = face_recognition.load_image_file("your_file.jpg")
#face_locations = face_recognition.face_locations(image)
print("it worked")


known_image = face_recognition.load_image_file("jon1.jpg")
unknown_image = face_recognition.load_image_file("notJon.jpg")

biden_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
print(results)