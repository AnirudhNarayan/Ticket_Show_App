<template>
  <nav>
    <div class="nav-left">
      <h1>Hello</h1>
    </div>
    <div class="nav-right">
      <router-link to="/display">Home</router-link>
      <router-link to="/export_data">Export data</router-link>
      
      <!-- <router-link to="/booked_shows">Bookings</router-link> -->
      <a href="/" @click.prevent="logout()">Logout</a>
    </div>
  </nav>
</template>

<script>
import axios from "axios";

export default {
  name: "UserNavbar",
  methods: {
    logout() {
      localStorage.removeItem("token");
      this.$router.push("/");
    },
    sendPDF() {
      axios.get("http://localhost:7000/create_pdf_report")
        .then(response => {
          console.log("PDF sent successfully");
        })
        .catch(error => {
          console.error("Failed to send PDF:", error);
        });
    },
  },
};
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
