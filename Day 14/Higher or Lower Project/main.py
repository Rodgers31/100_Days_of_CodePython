from game_data import data
import random
from art import logo, vs
# from art


def compare(celeb1, celeb2, final_score):
    followers = input("Who has more followers? Type 'A' or 'B': ").lower()
    if followers == 'a':
        if celeb1['follower_count'] > celeb2['follower_count']:
            final_score += 1
            return final_score, celeb1
        else:
            return print(f"Sorry, that's wrong. Final score: {final_score}")
    elif followers == 'b':
        if celeb2['follower_count'] > celeb1['follower_count']:
            final_score += 1
            return final_score, celeb2
        else:
            return print(f"Sorry, that's wrong. Final score: {final_score}")
    else:
        return print(f"Sorry, that's wrong. Final score: {final_score}")


play = True
final_score = 0
correct_celeb = {}
print(logo)
while play:
    celeb_rand = random.randint(0, len(data) - 1)
    celeb2_rand = random.randint(0, len(data) - 1)

    # This code fixes bug where both random picks are equal, we will add or subtract from celeb2 making
    # sure wen don't go over the length of the data array on both sides
    if celeb_rand == celeb2_rand:
        if celeb2_rand - 1 < 0:
            celeb2_rand += 1
        elif celeb2_rand + 1 > len(data) - 1:
            celeb2_rand -= 1

    celeb1 = (data[celeb_rand])
    celeb2 = (data[celeb2_rand])
    if final_score > 0:
        print(f"You're right! Current score: {final_score}")
        celeb1 = correct_celeb

    print(f"Compare A: {celeb1['name']}, {celeb1['description']}, from {celeb1['country']}")
    print(vs)
    print(f"Against B: {celeb2['name']}, {celeb2['description']}, from {celeb2['country']}")
    try:
        score_count, celebrity = compare(celeb1, celeb2, final_score)
        if type(score_count) == int and score_count > final_score:
            final_score = score_count
            correct_celeb = celebrity
    except TypeError:
        print(f"{celeb1['name']} has {celeb1['follower_count']} million followers")
        print(f"And {celeb2['name']} has {celeb2['follower_count']} million followers")
        play = False

