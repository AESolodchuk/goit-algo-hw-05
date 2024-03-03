from task_3_algorithms import boyer_moore, knut_morris, rabin_karp
import timeit
import requests

first_text = requests.get("https://drive.google.com/uc?id=18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh").text
second_text = requests.get("https://drive.google.com/uc?id=13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ").text


phraze_to_find_first_text = "Пошук – поширена дія, яка виконується в бізнес-додатках"
phraze_to_find_second_text = "Випадковим чином обирається контрольна сесія"
phrazae_to_find_improvization = "щось таке чого нема у тексті"

#Пошук у першому тексті
te_search_boyer_moore_first_text = timeit.timeit(
    lambda: boyer_moore.boyer_moore_search(first_text, phraze_to_find_first_text), number=5
)
te_search_knut_morris_first_text  = timeit.timeit(
    lambda: knut_morris.kmp_search(first_text, phraze_to_find_first_text), number=5
)
te_search_rabin_karp_first_text  = timeit.timeit(
    lambda: rabin_karp.rabin_karp_search(first_text, phraze_to_find_first_text), number=5
)

ti_search_boyer_moore_first_text  = timeit.timeit(
    lambda: boyer_moore.boyer_moore_search(first_text, phrazae_to_find_improvization),
    number=5,
)
ti_search_knut_morris_first_text  = timeit.timeit(
    lambda: knut_morris.kmp_search(first_text, phrazae_to_find_improvization), number=5
)
ti_search_rabin_karp_first_text  = timeit.timeit(
    lambda: rabin_karp.rabin_karp_search(first_text, phrazae_to_find_improvization), number=5
)

#Пошук у другому тексті
te_search_boyer_moore_second_text = timeit.timeit(
    lambda: boyer_moore.boyer_moore_search(second_text, phraze_to_find_second_text), number=5
)
te_search_knut_morris_second_text  = timeit.timeit(
    lambda: knut_morris.kmp_search(second_text, phraze_to_find_second_text), number=5
)
te_search_rabin_karp_second_text = timeit.timeit(
    lambda: rabin_karp.rabin_karp_search(second_text, phraze_to_find_second_text), number=5
)

ti_search_boyer_moore_second_text  = timeit.timeit(
    lambda: boyer_moore.boyer_moore_search(second_text, phraze_to_find_second_text),
    number=5,
)
ti_search_knut_morris_second_text  = timeit.timeit(
    lambda: knut_morris.kmp_search(second_text, phraze_to_find_second_text), number=5
)
ti_search_rabin_karp_second_text  = timeit.timeit(
    lambda: rabin_karp.rabin_karp_search(second_text, phraze_to_find_second_text), number=5
)


print("First text")
print(f"|{'Algorithm':^20} | {'Exist':^20} | {'Improvization':^20} |")
print(f"|{'-'*20} | {'-'*20} | {'-'*20} |")
print(
    f"|{'Boyer-Moore':^20} | {te_search_boyer_moore_first_text:^20.5f} | {ti_search_boyer_moore_first_text:^20.5f} |"
)
print(
    f"|{'Knut-Morris':^20} | {te_search_knut_morris_first_text:^20.5f} | {ti_search_knut_morris_first_text:^20.5f} |"
)
print(
    f"|{'Rabin-Karp':^20} | {te_search_rabin_karp_first_text:^20.5f} | {ti_search_rabin_karp_first_text:^20.5f} |"
)


print("\nSecond text")
print(f"|{'Algorithm':^20} | {'Exist':^20} | {'Improvization':^20} |")
print(f"|{'-'*20} | {'-'*20} | {'-'*20} |")
print(
    f"|{'Boyer-Moore':^20} | {te_search_boyer_moore_second_text:^20.5f} | {ti_search_boyer_moore_second_text:^20.5f} |"
)
print(
    f"|{'Knut-Morris':^20} | {te_search_knut_morris_second_text:^20.5f} | {ti_search_knut_morris_second_text:^20.5f} |"
)
print(
    f"|{'Rabin-Karp':^20} | {te_search_rabin_karp_second_text:^20.5f} | {ti_search_rabin_karp_second_text:^20.5f} |"
)