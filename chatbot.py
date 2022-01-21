while True:
    question = input(" Ask any question ")
    question = question.lower()
    if question in ['hi']:
        print("hello")
    elif question in ['how are you?']:
        print("i m very good")
        g = input("what about you : ")
    elif question in ['are you working?']:
        print("yes! i m working")
    elif question in ['what is your name?']:
        print("my name is chat_bot")
        name = input("what is your name")
        print("nice name")
    elif question in ["what is covid19"]:
        print("(COVID-19)is an infectious disease caused by severe acuterespiratory syndrome coronavirus2(SARS-CoV-2)")
        break
    else:
        print("i don't understand")