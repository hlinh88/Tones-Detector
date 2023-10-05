import os
from tonesCollection import TonesCollection

path = os.getcwd() + "/Songs"

os.chdir(path)

count_total = grave_total = hook_total = tilde_total = acute_total = dot_total = unmarked_total = 0


def check_word(passed_lyric):
    global grave_total, hook_total, tilde_total, acute_total, dot_total, unmarked_total, count_total
    grave_count = hook_count = tilde_count = acute_count = dot_count = 0
    for word in passed_lyric:
        is_unmarked = True
        for character in word:
            if character in TonesCollection.grave:
                # print(f"Dấu huyền: {word}")
                is_unmarked = False
                grave_count += 1
                grave_total += 1
                break
            elif character in TonesCollection.hook:
                # print(f"Dấu hỏi: {word}")
                is_unmarked = False
                hook_count += 1
                hook_total += 1
                break
            elif character in TonesCollection.tilde:
                # print(f"Dấu ngã: {word}")
                is_unmarked = False
                tilde_count += 1
                tilde_total += 1
                break
            elif character in TonesCollection.acute:
                # print(f"Dấu sắc: {word}")
                is_unmarked = False
                acute_count += 1
                acute_total += 1
                break
            elif character in TonesCollection.dot:
                # print(f"Dấu nặng: {word}")
                is_unmarked = False
                dot_count += 1
                dot_total += 1
                break

        # if is_unmarked:
        #     print(f"Dấu ngang: {word}")

    unmarked_count = len(passed_lyric) - (grave_count + hook_count + tilde_count + acute_count + dot_count)
    unmarked_total += unmarked_count

    count_total += len(passed_lyric)

    count_result = {
        "Dấu huyền": grave_count,
        "Dấu hỏi": hook_count,
        "Dấu ngã": tilde_count,
        "Dấu sắc": acute_count,
        "Dấu nặng": dot_count,
        "Dấu ngang": unmarked_count
    }
    return count_result


lyrics = []
songs = []
for file in os.listdir():
    songs.append(file)
    if file.endswith(".txt"):
        file_path = f"{path}/{file}"
        with open(file_path, 'r') as f:
            lyrics.append(f.read().lower())
        f.close()

num_of_songs = len(songs)

for item in range(num_of_songs):
    lyric_split = lyrics[item].split()
    result = check_word(lyric_split)
    print(f"{songs[item]} \n"
          f"Length: {len(lyric_split)} words \n" 
          f"{result} \n")

print(f"Tổng: \n"
      f"Dấu huyền: {grave_total} ({round(grave_total / count_total * 100, 2)}%) \n"
      f"Dấu hỏi: {hook_total} ({round(hook_total / count_total * 100, 2)}%) \n"
      f"Dấu ngã: {tilde_total} ({round(tilde_total / count_total * 100, 2)}%) \n"
      f"Dấu sắc: {acute_total} ({round(acute_total / count_total * 100, 2)}%) \n"
      f"Dấu nặng: {dot_total} ({round(dot_total / count_total * 100, 2)}%) \n"
      f"Dấu ngang: {unmarked_total} ({round(unmarked_total / count_total * 100, 2)}%) \n")
