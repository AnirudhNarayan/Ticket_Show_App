<template>
  <div class="add-theatre">
    <NavBar />

    <h1 class="title">Editing Venue</h1>
    <form @submit.prevent="editVenue">
      <div class="form-group">
        <label for="venue-name">Venue Name:</label>
        <input type="text" id="venue-name" v-model="venueName" required>
      </div>
      <div class="form-group">
        <label for="place">Place:</label>
        <input type="text" id="place" v-model="place" required>
      </div>
      <div class="form-group">
        <label for="location">Location:</label>
        <input type="text" id="location" v-model="location" required>
      </div>
      <div class="form-group">
        <label for="capacity">Capacity:</label>
        <input type="number" id="capacity" v-model="capacity" required>
      </div>
      <button type="submit">Update Venue</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import NavBar from './NavBar.vue';

export default {
  components: {
    NavBar,
  },
  data() {
    return {
      venueName: '',
      place: '',
      location: '',
      capacity: null,
    };
  },
  methods: {
    editVenue() {
      const venueId = this.$route.params.id;
      const token = localStorage.getItem('token');

      const venueData = {
        venueName: this.venueName,
        place: this.place,
        location: this.location,
        capacity: this.capacity,
      };

      axios
        .put(`http://localhost:7000/edit_theatre/${venueId}`, venueData, {
          headers: { Authorization: token },
        })
        .then(response => {
          console.log('Venue updated successfully:', response.data);
          this.$router.push('/admin_dashboard'); 
        })
        .catch(error => {
          console.error('Error updating venue:', error);
        });
    },
  },
};
</script>

<style>
.add-theatre {
  text-align: center;
}

.title {
  margin-top: 2rem;
}

.form-group {
  margin-bottom: 1rem;
}
</style>
