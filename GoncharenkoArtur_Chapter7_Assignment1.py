import re

#  This splits a paragraph into sentences while handling numbers at the beginning.
def split_sentences(paragraph):
    sentence_pattern = r'(?<!\d)[.!?] +'
    sentences = re.split(sentence_pattern, paragraph.strip())
    return [s.strip() for s in sentences if s]

# Displays each sentence and prints the total count.
def display_sentences(sentences):
    print("\nExtracted Sentences:")
    for i, sentence in enumerate(sentences, 1):
        print(f"{i}. {sentence}")
    print(f"\nTotal sentences: {len(sentences)}")

# Main program
if __name__ == "__main__":
    paragraph = input("Enter a paragraph: ")
    sentences = split_sentences(paragraph)
    display_sentences(sentences)
