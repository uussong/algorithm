const solution = (my_string, num1, num2) => {
    my_string = my_string.split('')
    const str1 = my_string[num1]
    my_string[num1] = my_string[num2]
    my_string[num2] = str1
    
    return my_string.join('')
}
