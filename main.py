import speech_recognition as sr
import pyttsx3

from gpt_api import GPT


class Assistant:
    def __init__(self):
        self.r = sr.Recognizer()
        self.engine = pyttsx3.init()

        self.gpt = GPT()

        self.engine.setProperty('rate', 200)
        self.engine.setProperty('value', 0.9)

    def listen(self):
        while True:
            with sr.Microphone() as source:
                print('говорите')
                audio = self.r.listen(source)  

            try:
                text = self.r.recognize_google(audio, language='ru_RU')
                yield text
            except sr.UnknownValueError:
                print('error')
            except sr.RequestError:
                print('server ERROR')

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def run(self):
        for task in self.listen():
            if 'информация' in task:
                self.say("Я бот спомощник лялялял")
            else:
                answer = self.gpt.request(task)
                self.say(answer)

if __name__ == '__main__':
    sara = Assistant()
    sara.run()
