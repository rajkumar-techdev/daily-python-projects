from googletrans import Translator

def translator_text():
    translator=Translator()

    text=input("Enter text to translate: ")
    target_lang=input("Translate to (e.g 'hi' for hindi, 'te' for telugu,'fr' for french)")


    try:
        translated=translator.translate(text,dest=target_lang)
        print(f"Translated ({translated.src} => {target_lang})")
        print(translated.text)

    except Exception as e:
        print("Error: ",e)

translator_text()
