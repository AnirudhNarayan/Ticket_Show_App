<template>
  <div>
    <img class="logo" src="../assets/blog_logo.png" />
    <h1>Login</h1>
    <div class="Login">
      <input type="text" v-model="emailid" placeholder="Enter Email" />
      <input type="password" v-model="password" placeholder="Enter Password" />
      <button @click="login">Login</button>
      <br />
      <div class="col-md-5 my-1">
        <router-link to="/register"><a class="btn btn-secondary">New User?</a></router-link>
      </div>
      <br />
      <div class="col-md-5 my-1">
        <router-link to="/admin_login" @click="goToAdminLogin"><a class="btn btn-secondary">Admin Login</a></router-link>
      </div>
      <br />
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Login",
  data() {
    return {
      emailid: "",
      password: "",
    };
  },
  methods: {
    login() {
      axios
        .post("http://localhost:7000/login", {
          emailid: this.emailid,
          password: this.password,
        })
        .then((response) => {
          console.log(response.data);
          if (response.status === 200) {
            localStorage.setItem("token", response.data.token);
            this.$router.push("/display"); 
          }
        })
        .catch((error) => {
          console.log(error.response.data);
        });
    },
    goToAdminLogin() {
      this.$router.push("/admin_login");
    },
  },
};
</script>

<style>
.logo {
  width: 200px;
}

.Login input {
  display: block;
  width: 300px;
  height: 40px;
  margin: 0 auto;
  margin-bottom: 15px;
  padding-left: 20px;
  border: 1px solid skyblue;
  margin-right: auto;
  margin-left: auto;
  border-radius: 5px;
  background-color: #f5f5f5;
  font-size: 16px;
  text-align: center;
}

.Login button {
  display: block;
  width: 15%;
  margin: 0 auto;
  padding: 10px;
  border: none;
  border-radius: 5px;
  background-color: #007bff;
  color: #fff;
  font-size: 16px;
  cursor: pointer;
  text-align: center;
}
</style>
