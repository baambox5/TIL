<template>
  <div>
    <LoginForm></LoginForm>
  </div>
</template>

<script>
  // @ 는 `/src`의 alias
  // 보통 절대경로를 많이 씀
  // import LoginForm from '../components/LoginForm'
  import LoginForm from '@/components/LoginForm'
  export default {
    name: 'login',
    components: {
      LoginForm,
    }
  }
</script>

<style>

</style>