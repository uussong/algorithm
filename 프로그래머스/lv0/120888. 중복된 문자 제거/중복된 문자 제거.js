function solution(my_string) {
    my_string = my_string.split('')
    return my_string.filter((element, index) => my_string.indexOf(element) === index).join('')
}