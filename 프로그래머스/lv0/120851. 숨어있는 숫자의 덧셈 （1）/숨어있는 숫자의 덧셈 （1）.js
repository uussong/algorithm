const solution = my_string => my_string.split("").reduce((acc, cur) => !isNaN(cur) ? acc + parseInt(cur) : acc, 0)
