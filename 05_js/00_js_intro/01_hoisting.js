// console.log(a) // undefined
// var a = 10
// console.log(a)


// // JS가 이해한 코드
// var a // 선언 + 초기화
// console.log(a)
// a = 10
// console.log(a)

// ----------------------- //
// console.log(b)
// let b = 10
// console.log(b)

// // 마찬가지로 아래와 같은 과정을 거친다.
// let b // 선언 + TDZ
// console.log(b)
// b = 10  // 할당 불가 (초기화가 아직 안됨)
// console.log(b)


// ex
if (x != 1) {
  console.log(y) // undefined
  var y = 3
  if (y === 3) {
    var x = 1
  }
  console.log(y) // 3
}

if (x === 1) {
  console.log(y) // 3
}

// JS 가 이해한 코드
var x
var y
if (x !== 1) {
  console.log(y) // undefined
  var y = 3
  if (y === 3) {
    var x = 1
  }
  console.log(y) // 3
}

if (x === 1) {
  console.log(y) // 3
}