<template>
  <div class="add-show">
    <NavBar></NavBar>

    <h1 class="title">Create Show</h1>
    <form @submit.prevent="createShow">
      <!-- Show name input -->
      <div class="form-group">
        <label for="show-name">Show Name:</label>
        <input type="text" id="show-name" v-model="showName" required />
      </div>

      <!-- Ratings input -->
      <div class="form-group">
        <label for="ratings">Ratings:</label>
        <input
          type="number"
          id="ratings"
          v-model="ratings"
          step="0.1"
          min="0"
          required
        />
      </div>

      <!-- Timings input -->
      <div class="form-group">
        <label for="timings">Timings:</label>
        <input type="text" id="timings" v-model="timings" required />
      </div>

      <!-- Tags input -->
      <div class="form-group">
        <label for="tags">Tags:</label>
        <input type="text" id="tags" v-model="tags" required />
      </div>

      <!-- Price input -->
      <div class="form-group">
        <label for="price">Price:</label>
        <input type="number" id="price" v-model="price" required />
      </div>

      <button type="submit">Create Show</button>
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
    createShow() {
      const showData = {
        show_name: this.showName,
        ratings: this.ratings,
        timings: this.timings,
        tags: this.tags,
        price: this.price,
        theatre_id: this.$route.params.id,
      };

      const token = localStorage.getItem("token"); // Retrieve token from local storage

      axios
        .post(`http://localhost:7000/add_show/${this.$route.params.id}`, showData, {
          headers: { Authorization: token },
        })
        .then((response) => {
          console.log("Show created successfully:", response.data);
          this.showName = "";
          this.ratings = null;
          this.timings = "";
          this.tags = "";
          this.price = null;
          this.$router.push(`/shows/${this.$route.params.id}`);
        })
        .catch((error) => {
          console.error("Error creating show:", error);
        });
    },
  },
};
</script>

<style>
.add-show {
  text-align: center;
}

.title {
  margin-top: 2rem;
}

.form-group {
  margin-bottom: 1rem;
}
</style>
