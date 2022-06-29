<template>
  <div class="app">
    <h1>MY TODOS</h1>
    <!-- <h2>전체 : {{ allTodosCount }}</h2>
    <h2>끝난거 : {{ completedTodosCount }}</h2>
    <h2>남은거 : {{ uncompletedTodosCount }}</h2> -->
    <todo-form></todo-form>
    <todo-list></todo-list>
  </div>

</template>

<script>
import TodoList from '@/components/TodoList.vue'
import TodoForm from '@/components/TodoForm.vue'
import { mapMutations } from 'vuex'
export default {
  name: 'app',
  components: {
    TodoList,
    TodoForm
  },
  // computed: {
  //   ...mapGetters([
  //     'allTodosCount',
  //     'completedTodosCount',
  //     'uncompletedTodosCount'])
  // },
  methods: {
    ...mapMutations(['LOAD_TODOS'])
  },
  created () {
    this.LOAD_TODOS()
  }
}
</script>

<style>

</style>
