import Vuex from 'vuex'

export default new Vuex.Store({
  state: {
    todos: []
  },
  getters: {
    // allTodosCount (state) {
    //   return state.todos.length
    // },
    // completedTodosCount (state) {
    //   return state.todos.filter(todos => {
    //     return todos.isCompleted
    //   }).length
    // },
    // uncompletedTodosCount (state) {
    //   return state.todos.filter(todos => {
    //     return !todos.isCompleted
    //   }).length
    // }
  },
  mutations: {
    LOAD_TODOS (state) {
      const todoString = localStorage.getItem('todos')
      state.todos = JSON.parse(todoString)
    },
    CREATE_TODO (state, newTodo) {
      state.todos.push(newTodo)
    },
    DELETE_TODO (state, todoItem) {
      const idx = state.todos.indexOf(todoItem)
      state.todos.splice(idx, 1)
    },
    UPDATE_TODO (state, todoItem) {
      state.todos = state.todos.map(todo => {
        if (todo === todoItem) {
          todo.isCompleted = !todo.isCompleted
        }
        return todo
      })
    }
  },
  actions: {
    saveTodos ({ state }) {
      const jsonData = JSON.stringify(state.todos)
      localStorage.setItem('todos', jsonData)
    },
    createTodo ({ commit, dispatch }, newTodo) {
      commit('CREATE_TODO', newTodo)
      dispatch('saveTodos')
    },
    deleteTodo ({ commit, dispatch }, todoItem) {
      if (confirm('Are you sure you want to delete?')) {
        commit('DELETE_TODO', todoItem)
        dispatch('saveTodos')
      }
    },
    updateTodo ({ commit, dispatch }, todoItem) {
      commit('UPDATE_TODO', todoItem)
      dispatch('saveTodos')
    }
  }
})
