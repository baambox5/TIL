<template>
  <div class="todo-list">
    <h2>{{ category }}</h2>
    <input type="text" v-model="newTodo" @keyup.enter="addTodo">
    <button @click="addTodo">+</button>
    <li v-for="todo in todos" :key="todo.id">
      <span>{{ todo.content }}</span>
      <button @click="removeTodo(todo.id)">x</button>
    </li>
  </div>
</template>

<script>
// 내보내기
  export default {
    props: {
      // category는 문자열이면서 반드시 필요한 것이라는 의미
      category: {
        type: String,
        required: true,
        validator: function (value) {
          if (value.length < 5) {
            return true
          } else {
            return false
          }
        },
      },
    },
    // 컴포넌트에서 data는 함수여야 한다.
    // 이제 모든 todos와 newTodo는 각각 고유한 내부 상태가 있다.
    data: function() {
      return {
        todos: [],
        newTodo: '',
      }
    },
    methods: {
      addTodo: function() {
        if (this.newTodo.length !== 0){
          this.todos.push({
            id: Date.now(),
            content: this.newTodo,
            completed: false,
          })
          this.newTodo = ''
        }          
      },
      removeTodo: function(todoId) {
        this.todos = this.todos.filter( todo => {
          // 완료한 todo
          // 완료된 todo를 제외한 나머지 todo만 filter를 통해서
          // 새로운 배열로 return
          return todo.id !== todoId
        })
      },
    },
  }
</script>

<style>
  .todo-list {
    display: inline-block;
    width: 33%;
  }
</style>