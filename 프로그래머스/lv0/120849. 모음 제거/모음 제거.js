const solution = my_string => {
    const vowels = ['a', 'e', 'i', 'o', 'u']
    for(let vowel of vowels) {
        my_string = my_string.replaceAll(vowel, '')   
    }
    return my_string
}