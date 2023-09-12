import pyttsx3


def get_word_pronunciation(word):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # 设置语速，可根据需要进行调整
    engine.setProperty('volume', 0.8)  # 设置音量，可根据需要进行调整
    engine.say(word)
    engine.runAndWait()

if __name__=='__main__':

    word = 'one of the dictionary'
    get_word_pronunciation(word)