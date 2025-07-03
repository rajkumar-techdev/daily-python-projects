import requests

def get_meaning(word):
    url=f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response=requests.get(url)

    if response.status_code==200:
        data=response.json()
        meanings=data[0]["meanings"]

        print(f"\n Meaning of {word}")
        for meaning in meanings:
            part_of_speech=meaning["partOfSpeech"]
            definitions=meaning["definitions"]
            for i , definition in enumerate(definitions[:3],1):#Show upto 3 definitions
                print(f"{i},({part_of_speech}) {definition['definition']}")

    else:
        print("Word not found,Please check the spelling")

def main():
    print("=== English Dictionary ===")
    word=input("Enter a word:").strip().lower()
    get_meaning(word)

main()