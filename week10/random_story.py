from typing import TextIO

def generate_context(story: list, all_context: dict, current_context: list, context_length: int) -> None:
    """Modify all_context to include all possible new contextes based on current_context,
    and context_length from the list of words story."""

    i = 0
    while i + context_length < len(story):
        if story[i:i+context_length] == current_context:
            next_word = story[i+context_length]
            if tuple(current_context) not in all_context:
                all_context[tuple(current_context)] = []
            if next_word in all_context[tuple(current_context)]:
                i += 1
                continue
            all_context[tuple(current_context)].append(next_word)
            generate_context(story, all_context, current_context[1:] + [next_word], context_length)
        i += 1

def generate_random_story(training_file: TextIO, context_length: int, num_words: int) -> str:
    """Return a randomly generated story with num_words words based on a context
    of context_length words from the text in training_file."""

    story = training_file.read().split()

    all_context = {}
    generate_context(story, all_context, story[0:context_length], context_length)

    # TODO: generate the story
    print(all_context)

if __name__ == "__main__":
    generate_random_story(open("training_file.txt", "r"), 2, 10)