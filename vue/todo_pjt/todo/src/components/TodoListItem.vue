<template>
  <div>
    <span
      @click="updateTodo(todo)"
      :class="{ 'is-completed' : todo.isCompleted }"
    >
      {{ todo.title }}
    </span>
    <button @click="deleteTodo(todo)">x</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'TodoListItem',
  props: {
    todo: Object
  },
  methods: {
    ...mapActions(['deleteTodo', 'updateTodo'])
  }
}
</script>
<style scoped>
.is-completed {
  text-decoration: line-through;
}
div {
  border: 2px solid black;
  margin: 5px 0 5px 0;
}
span {
  cursor: pointer;
}
</style>
