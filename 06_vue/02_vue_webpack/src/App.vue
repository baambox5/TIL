<template>
  <div>
    <h1>여기는 최상위 컴포넌트입니다.</h1>    
    <todo-list category="취업특강"></todo-list>
    <todo-list category="SSAFY"></todo-list>
    <todo-list category="기타"></todo-list>  
  </div>
</template>

<script>
  // 1. 하위 컴포넌트 불러오기
  import TodoList from './components/TodoList.vue'

  // 2. 불러온 컴포넌트를 최상위(부모) 컴포넌트에 등록
  export default {
    components: {
      TodoList
    }
  }
</script>

<style>

</style>