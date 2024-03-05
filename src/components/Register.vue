<template>
  <div>
    <img class="logo" src="../assets/blog_logo.png" />
    <h1>Register</h1>
    <div class="Login">
      <input type="text" v-model="emailid" placeholder="Enter Email" />
      <input type="text" v-model="password" placeholder="Enter Password" />
      <router-link to="/">
        <button @click="Register">Register</button>
      </router-link>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Register",
  data() {
    return {
      emailid: "",
      password: "",
    };
  },
  methods: {
    Register() {
      axios
        .post("http://localhost:7000/signup", {
          emailid: this.emailid,
          password: this.password,
        })
        .then((response) => {
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error.response.data);
        });
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
  width: 32%;
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
