"""
Sherlock considers a string to be valid if all characters of the string appear the same number of times.
It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters
will occur the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.
"""


in_string = [
    "ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd",
    "aaaaabc",
    "abcdefghhgfedecba"
             ]
expected_output = ["YES", "NO", "YES"]


def isValid(s):
    char_map = {}
    for c in s:
        c_freq = char_map.get(c, 0)
        c_freq += 1
        char_map[c] = c_freq


    """
    aaabbbdddd
    {a: 3, b:3 d:4}
    """

    frequencies_counter = {}
    for key, value in char_map.items():
        freq_count = frequencies_counter.get(value, 0)
        freq_count += 1
        frequencies_counter[value] = freq_count

    """
    frequencies_counter = {3: 2, 1: 1}   {111: 5, 1: 1}
    
    """

    if len(frequencies_counter) == 1:
        return "YES"

    if len(frequencies_counter) > 2:
        return "NO"

    freqs_array = []
    counts_array = []
    for freq, count in frequencies_counter.items():
        freqs_array.append(freq)
        counts_array.append(count)

    """
    freqs_array = [3 1]
    counts_array = [2 1]
    """

    """
    CASES: 
    I can remove one word and still be valid. Therefore,
    it is valid only if :
     1 - the count of at least one element in the counts array is 1 (I can remove only one word there) 
    AND 
     2 - the difference between the frequencies is 1 
    AND 
     3 - the frequency of the different element is just 1 (I can remove it and that's it)
    """
    if (freqs_array[0] == counts_array[0] == 1) or (freqs_array[1] == counts_array[1] == 1):
        return "YES"

    if abs(freqs_array[0] - freqs_array[1]) == 1 and (counts_array[0] == 1 or counts_array[1] == 1):
        return "YES"

    return "NO"


for s, o in zip(in_string, expected_output):
    res = isValid(s)
    print(res)
    # assert res == o
