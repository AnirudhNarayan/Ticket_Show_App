<template>
  <div>
    <NavBar />

    <div class="add-theatre" @click="goToAddTheatre">
      <b-icon-plus>+</b-icon-plus>
    </div>

    <Theatre /> 
  </div>
</template>

<script>
import axios from "axios";
import NavBar from "./NavBar.vue";
import Theatre from "./Theatre.vue";

export default {
  name: "AdminDashboard",
  components: {
    NavBar,
    Theatre, 
  },
  data() {
    return {
      theatres: [],
    };
  },
  methods: {
    fetchTheatres() {
      const token = localStorage.getItem("token");
    },

    goToAddTheatre() {
      this.$router.push("/add_theatre");
    },
  },
};

</script>

<style scoped>
.add-theatre {
  position: fixed;
  top: 35%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #007bff;
  color: white;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}
</style>
