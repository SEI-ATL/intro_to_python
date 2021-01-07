"""
function tripler(array) {
    const result = [];

    for (let i = 0; i < array.length; i++) {
        let num = array[i]; // 3
        let multiple = num * 3; // 9
        result.push(multiple); // [3, 6, 9]
    }
    
    return result;
}

console.log(tripler([1,2,3]))
console.log(tripler([4, 1, 7]));
"""

def tripler(array):
    result = []

    for i in range(len(array)):
        num = array[i]
        multiple = num * 3
        result.append(multiple)

    return result

print(tripler([1,2,6,7,8,9]))
