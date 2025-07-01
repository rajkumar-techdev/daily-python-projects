from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk

nltk.download('punkt')

def summarize_text(text,sentence_count=3):
    parser=PlaintextParser.from_string(text,Tokenizer("english"))
    summarizer=LsaSummarizer()
    summary=summarizer(parser.document,sentence_count)

    print("\n Summary")
    for sentence in summary:
        print("-",sentence)


def main():
    print("=== Text Summarizer ===")
    print("Paste your long text below(press Enter twice to finish):  ")

    lines=[]
    while True:
        line=input()
        if line ==" ":
            break

        lines.append(line)

    full_text="\n".join(lines)
    summarize_text(full_text)

main()


