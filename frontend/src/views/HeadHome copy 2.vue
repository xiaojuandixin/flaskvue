<template>
  <div>
    <h1>User Information</h1>
    <p>Name: {{ user.name }}</p>
    <p>Email: {{ user.email }}</p>
    <p>Location: {{ user.location }}</p>
  </div>
</template>

<script>
export default {
  name: 'UserInfo',
  data() {
    return {
      user: {
        name: 'John Doe',
        email: 'john@example.com',
        location: 'New York, NY'
      }
    }
  }
}
</script>
