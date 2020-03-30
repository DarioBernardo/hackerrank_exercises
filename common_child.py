"""
Common child problem

https://www.hackerrank.com/challenges/common-child/


"""

s1 = "SHINCHAN"
s2 = "NOHARAAA"

cache = {}


def is_char_in_string(c, s):
    if len(s) == 0:
        return -1

    search_hash = "{}#{}".format(c, s)
    cached_result = cache.get(search_hash, None)
    if cached_result is not None:
        return cached_result

    for index, temp_c in enumerate(s):
        if c == temp_c:
            cache[search_hash] = index
            return index

    return -1


common_child_cache = {}


# Complete the commonChild function below.
def commonChild(s1, s2):
    # print("Testing {} vs {}".format(s1, s2))

    if s1 == s2:
        return len(s1)

    search_hash = "{}#{}".format(s1, s2)
    cached_result = common_child_cache.get(search_hash, None)
    if cached_result is not None:
        return cached_result

    if len(s1) == 0 or len(s2) == 0:
        return 0

    solution_list = [0]
    for i1, c1 in enumerate(s1):
        i2 = is_char_in_string(c1, s2[0:len(s2)])
        if i2 != -1:
            best_subset_solution = commonChild(s1[i1 + 1:len(s1)], s2[i2 + 1:len(s2)])
            solution_list.append(best_subset_solution + 1)

    max_subchild_lenght = max(solution_list)
    common_child_cache[search_hash] = max_subchild_lenght
    return max_subchild_lenght


max_sol = commonChild(s1, s2)
print(max_sol)
assert max_sol == 3

s3 = "WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS"
s4 = "FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC"
max_sol = commonChild(s3, s4)
print(max_sol)
assert max_sol == 15


s5 = "LZNGFTIHZHJSQGQQYICYKYAPAFJMYXIRFHFISJZJAVHMQLPBFXSPEEQAUJIIVSVLCRVHSMIGXQIVOOAFHIQOAOJBOTGJUPXEPQZFJSNLVDHCXMDRPPGTUNBIMARYQXUTMQVGOVZDYSCBCHRTTAYEIFFNAGFDFGEFJNAXKWUYNFPETFYTHRLEICJEFDFHJFADZFBRABLMDYNGIBXHGWDOWIFLWUKFVFUIITQGFRCGUYFZINJYIGXCKNPVDPMUKTVOIBSIUUDQDWXTJAIGVSFROIGSEOWNZAWDRIZFLFQAYQKETDOYLUOHSVUYOJLDCJNIWDOFBRLWXQSCCTDEQHGHUXCHTCFSZRTRESSXNVOXFAHSWUAVJXMHCKRCOYVENGGBSXXYPEPUAQFNNCRVFQQDFCBPNTTNISDVORWBJBBCVVNLYUTTSBPRXSKYFEKOMIZCGNSQHZYVCHHILQLGCLIKTNCLQUOUAXFNHJPIZYBYWSVMGUVAGXANTEZHSDUDBVVCAGCPKJAQXIOQOCTNNOOFUYZEGGPAEQGRRDREZUSVTKCQAZQDZAEIIGOCJPMQXRHRFQTCBNEMSAPSSLHXJVDBCSGQVUPGNCZKTFEBRIKWKSYXWRAHGNGYLLXFKJOUNXKDRWMBVOZGEOBAYYNFDNHHWFVPOKWUFLZTZUCMLGFVUWFXSVYYUBGRHAUWHBQSNIHENTXADZCCZZZPOPESVYCROMUBJPDGBGUHBSMUQSYGEHUCRDACDYJIPYBLPXQUOLSELHBBBYQHKIOVFMSXANOMKMOXNPTGZSVHMCAEFSCNMCPHFUHOMNRNEQBOSLMAHJAMSMQMGKTLVKBVTSUDDWKXHHIIAFVNMQIHVVEPACCEVVECWOBVZVTWWMDIKYZAGZJOLQCINZZVZFNJGTCXXVLRAGJQFDMYMNKQDWNCLRTPYCCXEQFGKQWQSSYXNGELLNMAKNPIKFNKUIDCRUTWSTRKIHUAOGMPXOBQTFFAQMKG"
s6 = "BLCRCQQMXZCBACBDSFGIQDKFFHGPOGSZLHLXNZSSXRGVKIGNABASNFZDHVJOAINPZEZNDWOWSEJGMOVPPXHBERDJXLJSPAQDKNQEJMTBMVTPRXOCHYPKMDGRIHUPBQWZBNIXJBPTFYRMIUNXLVKPIRLLGJVGBIBIGDRIWGKEIKKYGCCFHCTEVNJPWFCFPDOXQDYGHRRNXTFQRGCTITBUEPHPEIXQMYSKLYQXZWVRWDBYLJRBOWRAHRWUJWZKEGBCEHVTKJERFIJVWWVSRVNIDHYVEYIWAPHYSIKCBDBDWXAWXEHRFMHCQNHTBYOFYJBIKJGUDIMQKNFCKMWNGVROISVLPZZCRUKHBWPSHRBSERBQOJXFTKSDDCRBIACQMHIOQBNESXTNURRXONVMNGZBMBDZDBWGXMFNCJWVUICKVQHUDDMVHNHRAHRDHOITKDDRRMFSQFZSLAASQSKJTVWTOSWQSPEARPEWADMMNSPCZTMKGVQOBGOBMGICUZNBEBZBFDRPFJPLCJOUTZBNJAKTTMQPQVQOGVHIBNWFXOQWSMUSCBBCZURZOYRHSTKIFUXWROLBQBLYEDXQHKXYZNWVDCRAABKUBAPCPLKPZRQWNSWRCLNGDYLICBQAPPFNIDNCRMZEJJNNSUDDMAAOJPDQZPBRYKMVACVMTNNPQZBWHYALBHLDAYTJGJOWXQYVQQVNHLJXVVEXIPHEZZCKLKXNKLAYSHPSWWBPOQXZJYNFWBYVMMTMKFWJVPGHTGXCMBKTBWIXQJAMGVNRALOCACXIICCVEWKKSFDBMPRJUEYCHROEDXTKYJYSGVITYMVSAAEVKDAEDXWDBSHFTXDCDRTLCCFAKWSBNTPUSXIGTSXOVPIMVURDXOGBOOQAHISZBKADCRXVSJSICXWQNMQGCCPTHWHKFKDXUGARNLREDXZIROXZTXPAVOGORNCVXGAMFVJUKLGPHSZKVVMRMFXLYUZNDUYOIIHJCKDWQXNCIYNG"
max_sol = commonChild(s5, s6)
print(max_sol)
assert max_sol == 321
print("DONE!")
