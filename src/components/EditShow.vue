<template>
  <div class="edit-show">
    <NavBar></NavBar>
    <h1 class="title">Edit Show</h1>
    <form @submit.prevent="updateShow">
      <div class="form-group">
        <label for="show-name">Show Name:</label>
        <input type="text" id="show-name" v-model="showName" required />
      </div>
      <div class="form-group">
        <label for="ratings">Ratings:</label>
        <input type="number" id="ratings" v-model="ratings" step="0.1" min="0" required />
      </div>
      <div class="form-group">
        <label for="timings">Timings:</label>
        <input type="text" id="timings" v-model="timings" required />
      </div>
      <div class="form-group">
        <label for="tags">Tags:</label>
        <input type="text" id="tags" v-model="tags" required />
      </div>
      <div class="form-group">
        <label for="price">Price:</label>
        <input type="number" id="price" v-model="price" required />
      </div>
      <button type="submit">Update Show</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import NavBar from "./NavBar.vue";

export default {
  components: {
    NavBar,
  },
  data() {
    return {
      showName: "",
      ratings: null,
      timings: "",
      tags: "",
      price: null,
    };
  },
  methods: {
    updateShow() {
      const showId = this.$route.params.showId;
      const showData = {
        show_name: this.showName,
        ratings: this.ratings,
        timings: this.timings,
        tags: this.tags,
        price: this.price,
      };

      const token = localStorage.getItem("token");

      axios
        .put(`http://localhost:7000/edit_show/${showId}`, showData, {
          headers: { Authorization: token },
        })
        .then((response) => {
          console.log("Show updated successfully:", response.data);
          this.$router.go(-1);
        })
        .catch((error) => {
          console.error("Error updating show:", error);
        });
    },
  },
};
</script>

<style scoped>
.edit-show {
  text-align: center;
}

.title {
  margin-top: 2rem;
}

.form-group {
  margin-bottom: 1rem;
}
</style>
