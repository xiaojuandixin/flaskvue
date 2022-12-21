<template>
  <div class="user-info">
    <h1>{{ user.name }}</h1>
    <p>{{ user.email }}</p>
    <button @click="editUser">Edit</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      user: {
        name: 'John Doe',
        email: 'john.doe@example.com'
      }
    }
  },
  methods: {
    editUser() {
      // code to open an edit form for the user goes here
    }
  }
}
</script>

<style>
.user-info {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
