from voice_recog import voice_recognition_google
from web_interface import web_test
from face_recog import frame_capture,label_read


if __name__ == "__main__":
    labels = label_read()
    name = frame_capture(labels)
    if name == 'devarsh':
        text = voice_recognition_google(name)
        web_test(text)
