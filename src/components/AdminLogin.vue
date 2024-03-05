<template>
  <div>
    <img class="logo" src="../assets/blog_logo.png" />
    <h1>Admin Login</h1>
    <div class="Login">
      <input type="text" v-model="username" placeholder="Enter Username" />
      <input type="password" v-model="password" placeholder="Enter Password" />
      <button @click="adminLogin()">Login</button>
      <br />
      <div class="col-md-5 my-1">
        <router-link to="/">
          <a class="btn btn-secondary">Back to Login</a>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "AdminLogin",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    adminLogin() {
      if (this.password === "anirudh123") {
        axios
          .post("http://localhost:7000/admin_login", {
            username: this.username,
            password: this.password,
          })
          .then((response) => {
            console.log(response.data);
            
            if (response.status === 200) {
              localStorage.setItem("token", response.data.token);
              localStorage.setItem("admin_id", response.data.admin_id);
              this.$router.push("/admin_dashboard");
            }
          })
          .catch((error) => {
            console.log(error.response.data);
            
          });
      } else {
        console.log("Incorrect password");
        
      }
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
