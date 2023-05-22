//logic to get calculaor to work
let arr = []
let arrend = []
let str = ''
let total = 0
//enter first num
arr.push(1)
arr.push(2)
//press + sign
arrend.push(arr.join(''))
arrend.push('+')
arr=[]
//enter second number
arr.push(2)
arr.push(1)
//press =
arrend.push(arr.join(''))
total = eval(arrend.join(''))

console.log(arr, arrend, total)
console.log(arrend.slice(-1))
