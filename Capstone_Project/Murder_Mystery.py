lat = "Lorem Ipsum, this is just a practice test of a function. Also testing punctuation! " \
      "I'll probably need at least three sentences to be sure?"

murder_note = "You may call me heartless, a killer, a monster, a murderer, but I'm still NOTHING compared to " \
              "the villain that Jay was. This whole contest was a sham, an elaborate plot to shame the contestants " \
              "and feed Jay's massive, massive ego. SURE you think you know him! You've seen him smiling for " \
              "the cameras, laughing, joking, telling stories, waving his money around like a prop but off camera" \
              " he was a sinister beast, a cruel cruel taskmaster, he treated all of us like slaves, like cattle," \
              " like animals! Do you remember Lindsay, she was the first to go, he called her such horrible " \
              "things that she cried all night, keeping us all up, crying, crying, and more crying, he broke her" \
              " with his words. I miss my former cast members, all of them very much. And we had to live with him," \
              " live in his home, live in his power, deal with his crazy demands. AND FOR WHAT! DID YOU KNOW THAT " \
              "THE PRIZE ISN'T REAL? He never intended to marry one of us! The carrot on the stick was gone," \
              " all that was left was stick, he told us last night that we were all a terrible terrible " \
              "disappointment and none of us would ever amount to anything, and that regardless of who won the" \
              " contest he would never speak to any of us again! It's definitely the things like this you can feel" \
              " in your gut how wrong he is! Well I showed him, he got what he deserved all right, I showed him," \
              " I showed him the person I am! I wasn't going to be pushed around any longer, and I wasn't going" \
              " to let him go on pretending that he was some saint when all he was was a sick sick twisted man who" \
              " deserved every bit of what he got. The fans need to know, Jay Stacksby is a vile amalgamation of all " \
              "things evil and bad and the world is a better place without him."
lily_trebuchet_intro = "Hi, I'm Lily Trebuchet from East Egg, Long Island. I love cats, hiking, and curling " \
                       "up under a warm blanket with a book. So they gave this little questionnaire to use for " \
                       "our bios so lets get started. What are some of my least favorite household chores? Dishes," \
                       " oh yes it's definitely the dishes, I just hate doing them, don't you? Who is your " \
                       "favorite actor and why? Hmm, that's a hard one, but I think recently I'll have to go " \
                       "with Michael B. Jordan, every bit of that man is handsome, HANDSOME! Do you remember " \
                       "seeing him shirtless? I can't believe what he does for the cameras! Okay okay next " \
                       "question, what is your perfect date? Well it starts with a nice dinner at a delicious" \
                       " but small restaurant, you know like one of those places where the owner is in the " \
                       "back and comes out to talk to you and ask you how your meal was. My favorite form of " \
                       "art? Another hard one, but I think I'll have to go with music, music you can feel in " \
                       "your whole body and it is electrifying and best of all, you can dance to it! Okay final " \
                       "question, let's see, What are three things you cannot live without? Well first off, " \
                       "my beautiful, beautiful cat Jerry, he is my heart and spirit animal. Second is pasta, " \
                       "definitely pasta, and the third I think is my family, I love all of them very much " \
                       "and they support me in everything I do. I know Jay Stacksby is a handsome man and all " \
                       "of us want to be the first to walk down the aisle with him, but I think he might " \
                       "truly be the one for me. Okay that's it for the bio, I hope you have fun watching the show!"
myrtle_beech_intro = "Salutations. My name? Myrtle. Myrtle Beech. I am a woman of simple tastes. I enjoy reading," \
                     " thinking, and doing my taxes. I entered this competition because I want a serious " \
                     "relationship. I want a commitment. The last man I dated was too whimsical. He wanted " \
                     "to go on dates that had no plan. No end goal. Sometimes we would just end up wandering " \
                     "the streets after dinner. He called it a \"walk\". A \"walk\" with no destination. Can " \
                     "you imagine? I like every action I take to have a measurable effect. When I see a movie," \
                     " I like to walk away with insights that I did not have before. When I take a bike ride, " \
                     "there better be a worthy destination at the end of the bike path. Jay seems frivolous " \
                     "at times. This worries me. However, it is my staunch belief that one does not make and " \
                     "keep money without having a modicum of discipline. As such, I am hopeful. I will now " \
                     "list three things I cannot live without. Water. Emery boards. Dogs. Thank you for the " \
                     "opportunity to introduce myself. I look forward to the competition."
gregg_t_fishy_intro = "A good day to you all, I am Gregg T Fishy, of the Fishy Enterprise fortune. I am 37 " \
                      "years young. An adventurous spirit and I've never lost my sense of childlike wonder. " \
                      "I do love to be in the backyard gardening and I have the most extraordinary time when" \
                      " I'm fishing. Fishing for what, you might ask? Why, fishing for compliments of course!" \
                      " I have a stunning pair of radiant blue eyes. They will pierce the soul of anyone who" \
                      " dare gaze upon my countenance. I quite enjoy going on long jaunts through garden paths" \
                      " and short walks through greenhouses. I hope that Jay will be as absolutely interesting " \
                      "as he appears on the television. I find that he has some of the most curious tastes in " \
                      "style and humor. When I'm out and about I quite enjoy hearing tales that instill in my " \
                      "heart of hearts the fascination that beguiles my every day life. Every fiber of my being " \
                      "scintillates and vascillates with extreme pleasure during one of these charming anecdotes " \
                      "and significantly pleases my beautiful personage. I cannot wait to enjoy being on A " \
                      "Brand New Jay. It certainly seems like a grand time to explore life and love."


def get_sentences_in_text2(text):
    sentence_count = 0
    word_count = 0

    string = text.replace(".", "+")
    string2 = string.replace("!", "+")
    string3 = string2.replace("?", "+")
    sentences_in_text = string3.split("+")

    for sentence in sentences_in_text:
        n = len(sentence.split())
        if n > 0:
            sentence_count += 1
        word_count += 1

    if sentence_count > 0:
        avg = word_count / sentence_count

    return avg


def get_sentences_in_text(text):
    string = text.replace(".", "+")
    string2 = string.replace("!", "+")
    string3 = string2.replace("?", "+")
    sentences_in_text = string3.split("+")
    words_in_sentence = []
    word_count = 0
    sentence_count = 0

    for sentence in sentences_in_text:
        words_in_sentence.append(sentence.split())

    for sentence in words_in_sentence:
        if len(sentence) > 0:
            sentence_count += 1
            word_count += len(sentence)

    avg = word_count / sentence_count
    return avg

    # print("{}, Total word count is {}.".format(name, word_count))
    # print("{}, Total sentence count is {}.".format(name, sentence_count))
    # print("{}, Average sentence length: {}".format(name, avg))


# print("Refactored Version:")
# get_sentences_in_text(lat)
# get_sentences_in_text(murder_note)
# get_sentences_in_text(lily_trebuchet_intro)
# get_sentences_in_text(myrtle_beech_intro)
# get_sentences_in_text(gregg_t_fishy_intro)


def get_avg_sentence_length(text):
    # establish punctuation
    punctuation = ".!?"

    # create list of every word in type using .split()
    words = text.split()
    # establish counters
    total_word_count = 0
    sentence_count = 0

    # checks every word and counts, if last index item of word is in punctuation,
    # we know it's the end of a sentence, and count.
    for word in words:
        total_word_count += 1
        if word[-1] in punctuation:
            sentence_count += 1

    # calculate average
    avg = total_word_count / sentence_count
    return avg
    # print("{}, Total words: {}".format(name, total_word_count))
    # print("{}, Number of Sentences: {}".format(name, sentence_count))
    # print("{}, Average words per sentence: {}".format(name, avg))


# print("Old Version:")
# get_avg_sentence_length("Test", lat)
# get_avg_sentence_length("Murder Note", murder_note)
# get_avg_sentence_length("Lily", lily_trebuchet_intro)
# get_avg_sentence_length("Myrtle", myrtle_beech_intro)
# get_avg_sentence_length("Gregg", gregg_t_fishy_intro)

def prepare_text(text):
    string1 = text.replace(",", "+")
    string2 = string1.replace(".", "+")
    string3 = string2.replace("!", "+")
    string4 = string3.replace("?", "+")
    string5 = string4.replace("\"", "+")
    string6 = string5.strip()
    string7 = string6.lower()
    string8 = string7.replace("+", "")
    words = string8.split()
    return words


def prepare_text_alt(text):
    punctuation = ",.!?\"\'"
    words = text.split()
    words_sorted = []

    for word in words:

        if word[0] and word[-1] not in punctuation:
            word = word.lower()
            words_sorted.append(word)

        elif word[0] in punctuation:
            if word[-1] in punctuation:
                word = word[1:-1]
                word = word.lower()
                words_sorted.append(word)
            else:
                word = word[1:]
                word = word.lower()
                words_sorted.append(word)

        elif word[-1] in punctuation:
            word = word[:-1]
            word = word.lower()
            words_sorted.append(word)

    return words_sorted


def build_frequency_table(corpus):
    frequency_table = {}

    for word in corpus:
        if word not in frequency_table.keys():
            frequency_table[word] = 1
        elif word in frequency_table.keys():
            frequency_table[word] += 1
    # Tested to ensure individual word counts added up to total word count:
    # values = frequency_table.values()
    # total_words = 0
    # for value in values:
        # total_words += value
    # return total_words

    return frequency_table


def ngram_creator(text_list):

    pairs = []
    for el in range(0, len(text_list) - 1):
        pairs.append(text_list[el] + ' ' + text_list[el + 1])
    return pairs


def frequency_comparison(table1, table2):
    appearances = 0
    mutual_appearances = 0
    for key in table1:
        if key in table2:
            if table1[key] > table2[key]:
                appearances += table1[key]
                mutual_appearances += table2[key]
            else:
                appearances += table2[key]
        else:
            appearances += table1[key]
    for key in table2:
        if key not in table1:
            appearances += table2[key]
    # conditional for comparing identical lists
    if appearances > 0:
        frequency = mutual_appearances / appearances

    return frequency


def percent_difference(val1, val2):
    if val1 > 0 and val2 > 0:
        difference = abs((val1 - val2) / (val1 + val2) / 2)
    return difference


def find_text_similarity(sample1, sample2):
    sentence_length_difference = percent_difference(sample1.average_sentence_length, sample2.average_sentence_length)
    sentence_length_similarity = abs(1 - sentence_length_difference)

    word_count_difference = frequency_comparison(sample1.word_count_frequency, sample2.word_count_frequency)
    word_count_similarity = abs(1 - word_count_difference)

    ngram_difference = frequency_comparison(build_frequency_table(sample1.ngram),
                                            build_frequency_table(sample2.ngram))
    ngram_similarity = abs(1 - ngram_difference)
    # ngram_similarity = abs(1 - ngram_difference)
    similarity = (sentence_length_similarity + word_count_similarity + ngram_similarity) / 3

    return similarity


class TextSample:

    def __init__(self, text, author):
        self.raw_text = text
        self.author = author
        self.prepared_text_alt = prepare_text_alt(self.raw_text)
        self.prepared_text = prepare_text(self.raw_text)
        self.average_sentence_length = get_sentences_in_text2(self.raw_text)
        self.word_count_frequency = build_frequency_table(self.prepared_text)
        self.ngram = ngram_creator(self.prepared_text)

    def __repr__(self):
        # TEST
        return str(self.author) + "\n" + "Prepped text : \n" + str(self.prepared_text_alt) + "\n" + "Word count : \n" + str(self.word_count_frequency) + "\n" + "Ngrams : \n" + str(self.ngram)
        return str(self.author) + ": \n" + str(self.prepared_text_alt) + "\n" + str(self.word_count_frequency) + "\n" + str(self.ngram)
        # return str(self.author) + ": \nSimilarity: " + str(find_text_similarity(murder_sample, self))


murder_sample = TextSample(murder_note, "Murder Note")
print(murder_sample)
lily_sample = TextSample(lily_trebuchet_intro, "Lily")
print(lily_sample)
myrtle_sample = TextSample(myrtle_beech_intro, "Myrtle")
# print(myrtle_sample)
gregg_sample = TextSample(gregg_t_fishy_intro, "Gregg")
# print(gregg_sample)

print("TEST:")
print(murder_sample.author + ", \nSimilarity: " + str(find_text_similarity(murder_sample, murder_sample)))
print(lily_sample.author + ", \nSimilarity: " + str(find_text_similarity(murder_sample, lily_sample)))
print(myrtle_sample.author + ", \nSimilarity: " + str(find_text_similarity(murder_sample, myrtle_sample)))
print(gregg_sample.author + ", \nSimilarity: " + str(find_text_similarity(murder_sample, gregg_sample)))

# print(frequency_comparison(murder_sample.word_count_frequency, murder_sample.word_count_frequency))

