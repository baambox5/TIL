const me = {
  name: 'ssafy', // key가 한 단어일 때
  'phone number': '01012345678', // key가 여러단어일 때
  appleProducts: {
    ipad: '2018pro',
    iphone: '7',
    macbook: '2019pro',
  }
}

console.log(me.name) // ssafy
console.log(me['name']) // ssafy
console.log(me['phone number']) // key가 여러 단어인 경우 반드시 []로 접근

console.log(me.appleProducts)
console.log(me.appleProducts.ipad)


// object Literal (객체 표현법)
// ES5
var books = ['Learning JS', 'Eloquent JS']

var comics = {
  'DC': ['Joker', 'Aquaman'],
  'Marvel': ['Captain Marvel', 'Avengers'],
}

var magazines = null

var bookShop = {
  books: books,
  comics: comics,
  magazines: magazines,
}

console.log(bookShop)
console.log(typeof bookShop)
console.log(bookShop.books[0])

// ES6+
// object의 key와 value가 같다면, 마치 배열처럼 한번만 작성 가능
var bookShopTwo = {
  books,
  comics,
  magazines,
}

console.log(bookShopTwo)

////////////////////////////

// JSON
const jsonData = JSON.stringify({ // JSON -> String
  coffee: 'Americano',
  iceCream: 'Mint Choco',
})
console.log(jsonData) // '{"coffee":"Americano","iceCream":"Mint Choco"}'
console.log(typeof jsonData) // string

const parseData = JSON.parse(jsonData)
console.log(parseData) // { coffee: 'Americano', iceCream: 'Mint Choco' }
console.log(typeof parseData) // object