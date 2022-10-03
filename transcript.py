import subprocess
# from ibm_watson import SpeechToTextV1
# from ibm_watson.websocket import RecognizeCallback, AudioSource
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import speech_recognition as sr

command = 'ffmpeg -i hello.mkv -ab 160k -ar 44100 -vn audio2.wav'
subprocess.call(command, shell = True)

def main():

    sound = 'audio2.wav'

    r = sr.Recognizer()

    with sr.AudioFile(sound) as source:
        r.adjust_for_ambient_noise(source)

        print('Converting audio file to Text...')

        audio = r.listen(source)

        try:
            print('Converted audio is : \n ' + r.recognize_google(audio))

        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()
