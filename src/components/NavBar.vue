<template>
  <nav>
    <div class="nav-left">
      <h1>Hello Admin</h1>
    </div>
    <div class="nav-right">
      <router-link to="/admin_dashboard">Home</router-link>
      <!-- <router-link to="/summary">Summary</router-link> -->
      <!-- <router-link to="/search">Search User</router-link> -->
      <!-- <router-link to="/profile">My Profile</router-link> -->
      <a href="/" @click.prevent="logout()">Logout</a>
    </div>
  </nav>
</template>

<script>
import axios from 'axios';
export default {
  name: 'NavBar',
  data() {
    return {
      name: null
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('token'); 
      this.$router.push('/'); 
    }
  }
}
</script>

<style scoped>
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #333;
  color: #fff;
  padding: 10px;
}

.nav-left {
  display: flex;
  align-items: center;
}

.nav-right {
  display: flex;
  align-items: center;
  
}
.right-border{
  border-right: 1px solid #ccc;
}

.nav-right input {
  margin-left: 10px;
  padding: 5px;
  border-radius: 5px;
  border: none;
}

.nav-right a {
  margin-left: 10px;
  color: #f8fdf9;
  text-decoration: none;
}
</style>